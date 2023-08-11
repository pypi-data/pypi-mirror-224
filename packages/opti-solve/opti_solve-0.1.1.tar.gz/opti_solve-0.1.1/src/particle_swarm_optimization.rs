// use std::collections::BTreeMap;

use crate::*;
use pyo3::types::PyDict;
use std::cmp::min_by;

/// Particle Swarm Optimization (PSO) algorithm.
/// 粒子群优化算法。
///
/// Represents the configuration parameters for the Particle Swarm Optimization algorithm.
/// 表示粒子群优化算法的配置参数。
///
/// * `particle_count`: Number of particles in the swarm.
///                    群体中的粒子数量。
/// * `iteration_count`: Number of iterations for the optimization process.
///                     优化过程的迭代次数。
/// * `cognitive_coefficient`: Acceleration coefficient for a particle's adjustment towards its own best position. Typically in the range [0, 2].
///                           粒子朝向其自身最佳位置调整的加速系数。通常在范围 [0, 2] 内。
/// * `social_coefficient`: Acceleration coefficient for a particle's adjustment towards the swarm's best position. Typically in the range [0, 2].
///                        粒子朝向群体最佳位置调整的加速系数。通常在范围 [0, 2] 内。
/// * `max_velocity_ratio`: Maximum velocity ratio for particle movement.
///                        粒子移动的最大速度比率。
/// * `inertia_coefficient`: Coefficient representing the influence of the particle's current velocity on its next position update.
///                         表示粒子当前速度对其下一个位置更新的影响系数。
///
/// # Example
///
/// ```
/// use your_crate::PSO;
///
/// let pso = PSO {
///     particle_count: 100,
///     iteration_count: 100,
///     cognitive_coefficient: 1.0,
///     social_coefficient: 1.0,
///     max_velocity_ratio: 0.5,
///     inertia_coefficient: 0.5,
/// };
/// ```
#[derive(Clone, Copy, Debug, PartialEq, PartialOrd, Default)]
#[pyclass(get_all, set_all)]
pub struct PSO {
    pub particle_count: usize,
    pub iteration_count: usize,
    pub cognitive_coefficient: f64,
    pub social_coefficient: f64,
    pub max_velocity_ratio: f64,
    pub inertia_coefficient: f64,
}

impl Opti for PSO {
    fn min<
        const I8: usize,
        const I16: usize,
        const I32: usize,
        const I64: usize,
        const I128: usize,
        const I: usize,
        const F32: usize,
        const F64: usize,
        const C64: usize,
        const C128: usize,
        const D: usize,
        O: PartialOrd + Clone,
    >(
        &self,
        f: impl Fn(X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>) -> O,
        x_min: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
        x_max: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
    ) -> (O, X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>) {
        let mut rng: ThreadRng = thread_rng();

        let x_bounds = XBounds::new(x_min.clone(), x_max.clone());

        let mut v_max = x_max.clone() - x_min.clone();
        v_max.mul_assign_f64(self.max_velocity_ratio);
        let mut v_min = -v_max.clone();

        let mut status: Vec<(
            // xt
            X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
            // vt
            X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
            // x_best_self
            X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
            // out_best_self
            O,
        )> = x_bounds
            .sample_iter(&mut rng)
            .take(self.particle_count)
            .map(|x| {
                (
                    x.clone(),
                    X::<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>::zero(),
                    x.clone(),
                    f(x),
                )
            })
            .collect();

        let (mut x_best, mut out_best) = {
            let best = status
                .iter()
                .min_by(|a, b| a.3.partial_cmp(&b.3).expect("failed to compare"))
                .expect("particle_count is 0!");
            (best.2.clone(), best.3.clone())
        };

        for _ in 0..self.iteration_count {
            status
                .iter_mut()
                .for_each(|(xt, vt, ref mut x_best_self, ref mut out_best_self)| {
                    *vt = (x_best.clone() - xt.clone()).mul_f64(self.cognitive_coefficient)
                        + (x_best_self.clone() - xt.clone()).mul_f64(self.social_coefficient);

                    *xt += vt.clone();

                    macro_rules! if_out_off_bounds {
                        ($t:tt) => {
                            xt.$t
                                .iter_mut()
                                .zip(vt.$t.iter_mut())
                                .zip(x_min.$t.into_iter())
                                .zip(x_max.$t.into_iter())
                                .zip(v_min.$t.into_iter())
                                .zip(v_max.$t.into_iter())
                                .for_each(
                                    |(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                                        if *xt_i < x_min_i {
                                            *xt_i = x_min_i;
                                            *vt_i = 0;
                                        } else if *xt_i > x_max_i {
                                            *xt_i = x_max_i;
                                            *vt_i = 0;
                                        } else if *vt_i < v_min_i {
                                            *vt_i = v_min_i;
                                        } else if *xt_i > v_max_i {
                                            *vt_i = v_max_i;
                                        }
                                    },
                                )
                        };
                        ($t:tt,$zero:expr) => {
                            xt.$t
                                .iter_mut()
                                .zip(vt.$t.iter_mut())
                                .zip(x_min.$t.into_iter())
                                .zip(x_max.$t.into_iter())
                                .zip(v_min.$t.into_iter())
                                .zip(v_max.$t.into_iter())
                                .for_each(
                                    |(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                                        if *xt_i < x_min_i {
                                            *xt_i = x_min_i;
                                            *vt_i = $zero;
                                        } else if *xt_i > x_max_i {
                                            *xt_i = x_max_i;
                                            *vt_i = $zero;
                                        } else if *vt_i < v_min_i {
                                            *vt_i = v_min_i;
                                        } else if *xt_i > v_max_i {
                                            *vt_i = v_max_i;
                                        }
                                    },
                                )
                        };
                    }
                    if_out_off_bounds!(i8);
                    if_out_off_bounds!(i16);
                    if_out_off_bounds!(i32);
                    if_out_off_bounds!(i64);
                    if_out_off_bounds!(i128);
                    xt.i.iter_mut()
                        .zip(vt.i.iter_mut())
                        .zip(x_min.i.iter())
                        .zip(x_max.i.iter())
                        .zip(v_min.i.iter())
                        .zip(v_max.i.iter())
                        .for_each(|(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                            if *xt_i < *x_min_i {
                                *xt_i = x_min_i.clone();
                                *vt_i = BigInt::from(0);
                            } else if *xt_i > *x_max_i {
                                *xt_i = x_max_i.clone();
                                *vt_i = BigInt::from(0);
                            } else if *vt_i < *v_min_i {
                                *vt_i = v_max_i.clone();
                            } else if *xt_i > *v_max_i {
                                *vt_i = v_max_i.clone();
                            }
                        });
                    if_out_off_bounds!(f32, 0.0);
                    if_out_off_bounds!(f64, 0.0);
                    if_out_off_bounds!(d, Decimal::from(0));
                    let out_t = f(xt.clone());
                    if out_t < *out_best_self {
                        if out_t < out_best {
                            *out_best_self = out_t.clone();
                            *x_best_self = xt.clone();
                            out_best = out_t;
                            x_best = xt.clone();
                        } else {
                            *out_best_self = out_t;
                            *x_best_self = xt.clone();
                        }
                    }
                });
            status
                .iter_mut()
                .for_each(|state| state.1.mul_assign_f64(self.inertia_coefficient))
        }

        (out_best, x_best)
    }

    fn min_vec<O: PartialOrd + Clone>(
        &self,
        f: impl Fn(XVec) -> O,
        x_min: XVec,
        x_max: XVec,
    ) -> (O, XVec) {
        let mut rng: ThreadRng = thread_rng();

        let x_bounds = XVecBounds::new(x_min.clone(), x_max.clone());

        let mut v_max = x_max.clone() - x_min.clone();
        v_max.mul_assign_f64(self.max_velocity_ratio);
        let mut v_min = -v_max.clone();

        let mut status: Vec<(
            // xt
            XVec,
            // vt
            XVec,
            // x_best_self
            XVec,
            // out_best_self
            O,
        )> = x_bounds
            .sample_iter(&mut rng)
            .take(self.particle_count)
            .map(|x| (x.clone(), x.zero(), x.clone(), f(x)))
            .collect();

        let (mut x_best, mut out_best) = {
            let best = status
                .iter()
                .min_by(|a, b| a.3.partial_cmp(&b.3).expect("failed to compare"))
                .expect("particle_count is 0!");
            (best.2.clone(), best.3.clone())
        };

        for _ in 0..self.iteration_count {
            status
                .iter_mut()
                .for_each(|(xt, vt, ref mut x_best_self, ref mut out_best_self)| {
                    *vt = (x_best.clone() - xt.clone()).mul_f64(self.cognitive_coefficient)
                        + (x_best_self.clone() - xt.clone()).mul_f64(self.social_coefficient);

                    *xt += vt.clone();

                    macro_rules! if_out_off_bounds {
                        ($t:tt) => {
                            xt.$t
                                .iter_mut()
                                .zip(vt.$t.iter_mut())
                                .zip(x_min.$t.iter())
                                .zip(x_max.$t.iter())
                                .zip(v_min.$t.iter())
                                .zip(v_max.$t.iter())
                                .for_each(
                                    |(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                                        if *xt_i < *x_min_i {
                                            *xt_i = *x_min_i;
                                            *vt_i = 0;
                                        } else if *xt_i > *x_max_i {
                                            *xt_i = *x_max_i;
                                            *vt_i = 0;
                                        } else if *vt_i < *v_min_i {
                                            *vt_i = *v_min_i;
                                        } else if *xt_i > *v_max_i {
                                            *vt_i = *v_max_i;
                                        }
                                    },
                                )
                        };
                        ($t:tt,$zero:expr) => {
                            xt.$t
                                .iter_mut()
                                .zip(vt.$t.iter_mut())
                                .zip(x_min.$t.iter())
                                .zip(x_max.$t.iter())
                                .zip(v_min.$t.iter())
                                .zip(v_max.$t.iter())
                                .for_each(
                                    |(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                                        if *xt_i < *x_min_i {
                                            *xt_i = *x_min_i;
                                            *vt_i = $zero;
                                        } else if *xt_i > *x_max_i {
                                            *xt_i = *x_max_i;
                                            *vt_i = $zero;
                                        } else if *vt_i < *v_min_i {
                                            *vt_i = *v_min_i;
                                        } else if *xt_i > *v_max_i {
                                            *vt_i = *v_max_i;
                                        }
                                    },
                                )
                        };
                    }
                    if_out_off_bounds!(i8);
                    if_out_off_bounds!(i16);
                    if_out_off_bounds!(i32);
                    if_out_off_bounds!(i64);
                    if_out_off_bounds!(i128);
                    xt.i.iter_mut()
                        .zip(vt.i.iter_mut())
                        .zip(x_min.i.iter())
                        .zip(x_max.i.iter())
                        .zip(v_min.i.iter())
                        .zip(v_max.i.iter())
                        .for_each(|(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                            if *xt_i < *x_min_i {
                                *xt_i = x_min_i.clone();
                                *vt_i = BigInt::from(0);
                            } else if *xt_i > *x_max_i {
                                *xt_i = x_max_i.clone();
                                *vt_i = BigInt::from(0);
                            } else if *vt_i < *v_min_i {
                                *vt_i = v_max_i.clone();
                            } else if *xt_i > *v_max_i {
                                *vt_i = v_max_i.clone();
                            }
                        });
                    if_out_off_bounds!(f32, 0.0);
                    if_out_off_bounds!(f64, 0.0);
                    if_out_off_bounds!(d, Decimal::from(0));
                    let out_t = f(xt.clone());
                    if out_t < *out_best_self {
                        if out_t < out_best {
                            *out_best_self = out_t.clone();
                            *x_best_self = xt.clone();
                            out_best = out_t;
                            x_best = xt.clone();
                        } else {
                            *out_best_self = out_t;
                            *x_best_self = xt.clone();
                        }
                    }
                });
            status
                .iter_mut()
                .for_each(|state| state.1.mul_assign_f64(self.inertia_coefficient))
        }

        (out_best, x_best)
    }

    fn min_par<
        const I8: usize,
        const I16: usize,
        const I32: usize,
        const I64: usize,
        const I128: usize,
        const I: usize,
        const F32: usize,
        const F64: usize,
        const C64: usize,
        const C128: usize,
        const D: usize,
        O: PartialOrd + Clone + Sync + Send,
    >(
        &self,
        f: impl Fn(X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>) -> O + Sync,
        x_min: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
        x_max: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
    ) -> (O, X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>) {
        let mut rng: ThreadRng = thread_rng();

        let x_bounds = XBounds::new(x_min.clone(), x_max.clone());

        let mut v_max = x_max.clone() - x_min.clone();
        v_max.mul_assign_f64(self.max_velocity_ratio);
        let mut v_min = -v_max.clone();

        struct ParState<
            const I8: usize,
            const I16: usize,
            const I32: usize,
            const I64: usize,
            const I128: usize,
            const I: usize,
            const F32: usize,
            const F64: usize,
            const C64: usize,
            const C128: usize,
            const D: usize,
            O: PartialOrd + Clone,
        >(
            pub X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
            pub X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
            pub X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
            pub O,
        );
        unsafe impl<
                const I8: usize,
                const I16: usize,
                const I32: usize,
                const I64: usize,
                const I128: usize,
                const I: usize,
                const F32: usize,
                const F64: usize,
                const C64: usize,
                const C128: usize,
                const D: usize,
                O: PartialOrd + Clone,
            > Send for ParState<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D, O>
        {
        }

        unsafe impl<
                const I8: usize,
                const I16: usize,
                const I32: usize,
                const I64: usize,
                const I128: usize,
                const I: usize,
                const F32: usize,
                const F64: usize,
                const C64: usize,
                const C128: usize,
                const D: usize,
                O: PartialOrd + Clone,
            > Sync for ParState<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D, O>
        {
        }
        let mut status: Vec<ParState<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D, O>> =
            x_bounds
                .sample_iter(&mut rng)
                .take(self.particle_count)
                .map(|x| {
                    ParState(
                        x.clone(),
                        X::<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>::zero(),
                        x.clone(),
                        f(x),
                    )
                })
                .collect();

        let (mut x_best, mut out_best) = {
            let best = status
                .par_iter()
                .min_by(|&a, &b| a.3.partial_cmp(&b.3).expect("failed to compare"))
                .expect("particle_count is 0!");
            (best.2.clone(), best.3.clone())
        };

        for _ in 0..self.iteration_count {
            (x_best, out_best) = status
                .par_iter_mut()
                .fold(
                    || (x_best.clone(), out_best.clone()),
                    |(mut x_best, mut out_best), ParState(xt, vt, x_best_self, out_best_self)| {
                        *vt = (x_best.clone() - xt.clone()).mul_f64(self.cognitive_coefficient)
                            + (x_best_self.clone() - xt.clone()).mul_f64(self.social_coefficient);

                        *xt += vt.clone();

                        macro_rules! if_out_off_bounds {
                            ($t:tt) => {
                                xt.$t
                                    .iter_mut()
                                    .zip(vt.$t.iter_mut())
                                    .zip(x_min.$t.into_iter())
                                    .zip(x_max.$t.into_iter())
                                    .zip(v_min.$t.into_iter())
                                    .zip(v_max.$t.into_iter())
                                    .for_each(
                                        |(
                                            ((((xt_i, vt_i), x_min_i), x_max_i), v_min_i),
                                            v_max_i,
                                        )| {
                                            if *xt_i < x_min_i {
                                                *xt_i = x_min_i;
                                                *vt_i = 0;
                                            } else if *xt_i > x_max_i {
                                                *xt_i = x_max_i;
                                                *vt_i = 0;
                                            } else if *vt_i < v_min_i {
                                                *vt_i = v_min_i;
                                            } else if *xt_i > v_max_i {
                                                *vt_i = v_max_i;
                                            }
                                        },
                                    )
                            };
                            ($t:tt,$zero:expr) => {
                                xt.$t
                                    .iter_mut()
                                    .zip(vt.$t.iter_mut())
                                    .zip(x_min.$t.into_iter())
                                    .zip(x_max.$t.into_iter())
                                    .zip(v_min.$t.into_iter())
                                    .zip(v_max.$t.into_iter())
                                    .for_each(
                                        |(
                                            ((((xt_i, vt_i), x_min_i), x_max_i), v_min_i),
                                            v_max_i,
                                        )| {
                                            if *xt_i < x_min_i {
                                                *xt_i = x_min_i;
                                                *vt_i = $zero;
                                            } else if *xt_i > x_max_i {
                                                *xt_i = x_max_i;
                                                *vt_i = $zero;
                                            } else if *vt_i < v_min_i {
                                                *vt_i = v_min_i;
                                            } else if *xt_i > v_max_i {
                                                *vt_i = v_max_i;
                                            }
                                        },
                                    )
                            };
                        }
                        if_out_off_bounds!(i8);
                        if_out_off_bounds!(i16);
                        if_out_off_bounds!(i32);
                        if_out_off_bounds!(i64);
                        if_out_off_bounds!(i128);
                        xt.i.iter_mut()
                            .zip(vt.i.iter_mut())
                            .zip(x_min.i.iter())
                            .zip(x_max.i.iter())
                            .zip(v_min.i.iter())
                            .zip(v_max.i.iter())
                            .for_each(
                                |(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                                    if *xt_i < *x_min_i {
                                        *xt_i = x_min_i.clone();
                                        *vt_i = BigInt::from(0);
                                    } else if *xt_i > *x_max_i {
                                        *xt_i = x_max_i.clone();
                                        *vt_i = BigInt::from(0);
                                    } else if *vt_i < *v_min_i {
                                        *vt_i = v_max_i.clone();
                                    } else if *xt_i > *v_max_i {
                                        *vt_i = v_max_i.clone();
                                    }
                                },
                            );
                        if_out_off_bounds!(f32, 0.0);
                        if_out_off_bounds!(f64, 0.0);
                        if_out_off_bounds!(d, Decimal::from(0));
                        let out_t = f(xt.clone());
                        if out_t < *out_best_self {
                            if out_t < out_best {
                                *out_best_self = out_t.clone();
                                *x_best_self = xt.clone();
                                out_best = out_t;
                                x_best = xt.clone();
                            } else {
                                *out_best_self = out_t;
                                *x_best_self = xt.clone();
                            }
                        }
                        (x_best, out_best)
                    },
                )
                .min_by(|a, b| a.1.partial_cmp(&b.1).expect("failed to compare"))
                .expect("particle_count is 0!");
            status
                .par_iter_mut()
                .for_each(|state| state.1.mul_assign_f64(self.inertia_coefficient))
        }

        (out_best, x_best)
    }

    fn min_vec_par<O: PartialOrd + Clone + Sync + Send>(
        &self,
        f: impl Fn(XVec) -> O + Sync,
        x_min: XVec,
        x_max: XVec,
    ) -> (O, XVec) {
        let mut rng: ThreadRng = thread_rng();

        let x_bounds = XVecBounds::new(x_min.clone(), x_max.clone());

        let mut v_max = x_max.clone() - x_min.clone();
        v_max.mul_assign_f64(self.max_velocity_ratio);
        let mut v_min = -v_max.clone();

        struct ParState<O>(
            pub XVec,
            pub XVec,
            pub XVec,
            pub O,
        );

        unsafe impl<O> Send for ParState<O>
        {
        }
        unsafe impl<O> Sync for ParState<O>
        {
        }

        let mut status: Vec<ParState<O>> = x_bounds
            .sample_iter(&mut rng)
            .take(self.particle_count)
            .map(|x| ParState(x.clone(), x.zero(), x.clone(), f(x)))
            .collect();


        let (mut x_best, mut out_best) = {
            let best = status
                .par_iter()
                .min_by(|a, b| a.3.partial_cmp(&b.3).unwrap_or(Equal))
                .expect("particle_count is 0!");
            (best.2.clone(), best.3.clone())
        };

        for _ in 0..self.iteration_count {
            (x_best, out_best) = status
                .par_iter_mut()
                .fold(
                    || (x_best.clone(), out_best.clone()),
                    |(mut x_best, mut out_best), ParState(xt, vt, x_best_self, out_best_self)| {
                        *vt = (x_best.clone() - xt.clone()).mul_f64(self.cognitive_coefficient)
                            + (x_best_self.clone() - xt.clone()).mul_f64(self.social_coefficient);

                        *xt += vt.clone();

                        macro_rules! if_out_off_bounds {
                            ($t:tt) => {
                                xt.$t
                                    .iter_mut()
                                    .zip(vt.$t.iter_mut())
                                    .zip(x_min.$t.iter())
                                    .zip(x_max.$t.iter())
                                    .zip(v_min.$t.iter())
                                    .zip(v_max.$t.iter())
                                    .for_each(
                                        |(
                                            ((((xt_i, vt_i), x_min_i), x_max_i), v_min_i),
                                            v_max_i,
                                        )| {
                                            if *xt_i < *x_min_i {
                                                *xt_i = *x_min_i;
                                                *vt_i = 0;
                                            } else if *xt_i > *x_max_i {
                                                *xt_i = *x_max_i;
                                                *vt_i = 0;
                                            } else if *vt_i < *v_min_i {
                                                *vt_i = *v_min_i;
                                            } else if *xt_i > *v_max_i {
                                                *vt_i = *v_max_i;
                                            }
                                        },
                                    )
                            };
                            ($t:tt,$zero:expr) => {
                                xt.$t
                                    .iter_mut()
                                    .zip(vt.$t.iter_mut())
                                    .zip(x_min.$t.iter())
                                    .zip(x_max.$t.iter())
                                    .zip(v_min.$t.iter())
                                    .zip(v_max.$t.iter())
                                    .for_each(
                                        |(
                                            ((((xt_i, vt_i), x_min_i), x_max_i), v_min_i),
                                            v_max_i,
                                        )| {
                                            if *xt_i < *x_min_i {
                                                *xt_i = *x_min_i;
                                                *vt_i = $zero;
                                            } else if *xt_i > *x_max_i {
                                                *xt_i = *x_max_i;
                                                *vt_i = $zero;
                                            } else if *vt_i < *v_min_i {
                                                *vt_i = *v_min_i;
                                            } else if *xt_i > *v_max_i {
                                                *vt_i = *v_max_i;
                                            }
                                        },
                                    )
                            };
                        }
                        if_out_off_bounds!(i8);
                        if_out_off_bounds!(i16);
                        if_out_off_bounds!(i32);
                        if_out_off_bounds!(i64);
                        if_out_off_bounds!(i128);
                        xt.i.iter_mut()
                            .zip(vt.i.iter_mut())
                            .zip(x_min.i.iter())
                            .zip(x_max.i.iter())
                            .zip(v_min.i.iter())
                            .zip(v_max.i.iter())
                            .for_each(
                                |(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                                    if *xt_i < *x_min_i {
                                        *xt_i = x_min_i.clone();
                                        *vt_i = BigInt::from(0);
                                    } else if *xt_i > *x_max_i {
                                        *xt_i = x_max_i.clone();
                                        *vt_i = BigInt::from(0);
                                    } else if *vt_i < *v_min_i {
                                        *vt_i = v_max_i.clone();
                                    } else if *xt_i > *v_max_i {
                                        *vt_i = v_max_i.clone();
                                    }
                                },
                            );
                        if_out_off_bounds!(f32, 0.0);
                        if_out_off_bounds!(f64, 0.0);
                        if_out_off_bounds!(d, Decimal::from(0));
                        let out_t = f(xt.clone());
                        if out_t < *out_best_self {
                            if out_t < out_best {
                                *out_best_self = out_t.clone();
                                *x_best_self = xt.clone();
                                out_best = out_t;
                                x_best = xt.clone();
                            } else {
                                *out_best_self = out_t;
                                *x_best_self = xt.clone();
                            }
                        }
                        (x_best, out_best)
                    },
                )
                .min_by(|a, b| a.1.partial_cmp(&b.1).expect("failed to compare"))
                .expect("particle_count is 0!");
            status
                .par_iter_mut()
                .for_each(|state| state.1.mul_assign_f64(self.inertia_coefficient))
        }

        (out_best, x_best)
    }



}

#[pymethods]
impl PSO {
    #[new]
    #[pyo3(signature = (particle_count = 100, iteration_count = 100, cognitive_coefficient = 1.0, social_coefficient = 1.0, max_velocity_ratio = 0.5, inertia_coefficient = 0.5))]
    pub fn new(
        particle_count: usize,
        iteration_count: usize,
        cognitive_coefficient: f64,
        social_coefficient: f64,
        max_velocity_ratio: f64,
        inertia_coefficient: f64,
    ) -> Self {
        Self {
            particle_count,
            iteration_count,
            cognitive_coefficient,
            social_coefficient,
            max_velocity_ratio,
            inertia_coefficient,
        }
    }

    #[pyo3(name = "min", signature = (
	f,
	i8_min = vec ! [], i8_max = vec ! [],
	i16_min = vec ! [], i16_max = vec ! [],
	i32_min = vec ! [], i32_max = vec ! [],
	i64_min = vec ! [], i64_max = vec ! [],
	i128_min = vec ! [], i128_max = vec ! [],
	i_min = vec ! [], i_max = vec ! [],
	f32_min = vec ! [], f32_max = vec ! [],
	f64_min = vec ! [], f64_max = vec ! [],
	c64_min = vec ! [], c64_max = vec ! [],
	c128_min = vec ! [], c128_max = vec ! [],
	d_min = vec ! [], d_max = vec ! []
	))]
    fn py_min(
        &self,
        f: PyObject,
        i8_min: Vec<i8>,
        i8_max: Vec<i8>,
        i16_min: Vec<i16>,
        i16_max: Vec<i16>,
        i32_min: Vec<i32>,
        i32_max: Vec<i32>,
        i64_min: Vec<i64>,
        i64_max: Vec<i64>,
        i128_min: Vec<i128>,
        i128_max: Vec<i128>,
        i_min: Vec<BigInt>,
        i_max: Vec<BigInt>,
        f32_min: Vec<f32>,
        f32_max: Vec<f32>,
        f64_min: Vec<f64>,
        f64_max: Vec<f64>,
        c64_min: Vec<Complex<f32>>,
        c64_max: Vec<Complex<f32>>,
        c128_min: Vec<Complex<f64>>,
        c128_max: Vec<Complex<f64>>,
        d_min: Vec<Decimal>,
        d_max: Vec<Decimal>,
    ) -> (PyObject, Py<PyDict>) {
        let x_min = XVec {
            i8: i8_min,
            i16: i16_min,
            i32: i32_min,
            i64: i64_min,
            i128: i128_min,
            i: i_min,
            f32: f32_min,
            f64: f64_min,
            c64: c64_min,
            c128: c128_min,
            d: d_min,
        };

        let x_max = XVec {
            i8: i8_max,
            i16: i16_max,
            i32: i32_max,
            i64: i64_max,
            i128: i128_max,
            i: i_max,
            f32: f32_max,
            f64: f64_max,
            c64: c64_max,
            c128: c128_max,
            d: d_max,
        };

        let (f_val, x) = Python::with_gil(|py| {
            let (f_val, x) = self.min_vec(
                move |x| {
                    let binding = x.into_py(py);
                    let x_py = binding.as_ref(py);
                    let res = f.call(py, (), Some(x_py)).expect("failed to call f");
                    PyWrapperObject(res, py)
                },
                x_min,
                x_max,
            );
            (f_val.0, x.into_py(py))
        });

        (f_val, x)
    }


    #[pyo3(name = "max", signature = (
        f,
        i8_min = vec ! [], i8_max = vec ! [],
        i16_min = vec ! [], i16_max = vec ! [],
        i32_min = vec ! [], i32_max = vec ! [],
        i64_min = vec ! [], i64_max = vec ! [],
        i128_min = vec ! [], i128_max = vec ! [],
        i_min = vec ! [], i_max = vec ! [],
        f32_min = vec ! [], f32_max = vec ! [],
        f64_min = vec ! [], f64_max = vec ! [],
        c64_min = vec ! [], c64_max = vec ! [],
        c128_min = vec ! [], c128_max = vec ! [],
        d_min = vec ! [], d_max = vec ! []
	))]
    fn py_max<'py>(
        &self,
        f: PyObject,
        i8_min: Vec<i8>,
        i8_max: Vec<i8>,
        i16_min: Vec<i16>,
        i16_max: Vec<i16>,
        i32_min: Vec<i32>,
        i32_max: Vec<i32>,
        i64_min: Vec<i64>,
        i64_max: Vec<i64>,
        i128_min: Vec<i128>,
        i128_max: Vec<i128>,
        i_min: Vec<BigInt>,
        i_max: Vec<BigInt>,
        f32_min: Vec<f32>,
        f32_max: Vec<f32>,
        f64_min: Vec<f64>,
        f64_max: Vec<f64>,
        c64_min: Vec<Complex<f32>>,
        c64_max: Vec<Complex<f32>>,
        c128_min: Vec<Complex<f64>>,
        c128_max: Vec<Complex<f64>>,
        d_min: Vec<Decimal>,
        d_max: Vec<Decimal>,
    ) -> (PyObject, Py<PyDict>) {

        let x_min = XVec {
            i8: i8_min,
            i16: i16_min,
            i32: i32_min,
            i64: i64_min,
            i128: i128_min,
            i: i_min,
            f32: f32_min,
            f64: f64_min,
            c64: c64_min,
            c128: c128_min,
            d: d_min,
        };

        let x_max = XVec {
            i8: i8_max,
            i16: i16_max,
            i32: i32_max,
            i64: i64_max,
            i128: i128_max,
            i: i_max,
            f32: f32_max,
            f64: f64_max,
            c64: c64_max,
            c128: c128_max,
            d: d_max,
        };

        let (f_val, x) = Python::with_gil(|py| {
            let (f_val, x) = self.max_vec(
                move |x| {
                    let binding = x.into_py(py);
                    let x_py = binding.as_ref(py);
                    let res = f.call(py, (), Some(x_py)).expect("failed to call f");
                    PyWrapperObject(res, py)
                },
                x_min,
                x_max,
            );
            (f_val.0, x.into_py(py))
        });

        (f_val, x)
    }

}

#[cfg(test)]
mod tests {

    use super::*;

    extern crate test;

    use test::Bencher;

    #[test]
    fn it_works() {
        let f = |x: X<0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0>| {
            (x.f64[0] - 7.0).powi(2) + (x.f64[1] + 3.0).powi(2) + (x.f64[2] + 5.0).powi(2)
        };

        let x_min = x_new().set_f64([-10.0, -10.0, -10.0]);
        let x_max = x_new().set_f64([10.0, 10.0, 10.0]);

        let pso = PSO::new(10000, 1000, 1.0, 1.0, 0.2, 0.5);

        let (out_best, x_best) = pso.min(f, x_min.clone(), x_max.clone());

        println!("{:?}\n{:?}", out_best, x_best);

        assert!(out_best < 0.5);
        assert!((x_best.f64[0] - 7.0).abs() < 1.0);
        assert!((x_best.f64[1] + 3.0).abs() < 1.0);
        assert!((x_best.f64[2] + 5.0).abs() < 1.0);
        let (out_best, x_best) = pso.min_par(f, x_min, x_max);

        println!("{:?}\n{:?}", out_best, x_best);

        assert!(out_best < 0.5);
        assert!((x_best.f64[0] - 7.0).abs() < 1.0);
        assert!((x_best.f64[1] + 3.0).abs() < 1.0);
        assert!((x_best.f64[2] + 5.0).abs() < 1.0);
    }

    #[bench]
    fn bencher(b: &mut Bencher) {
        let pso = PSO::new(10000, 100, 1.0, 1.0, 0.5, 1.0);

        b.iter(|| {
            pso.min(
                |x| (x.f64[0] - 7.0).powi(2) + (x.f64[1] + 3.0).powi(2) + (x.f64[2] + 5.0).powi(2),
                x_new().set_f64([-10.0, -10.0, -10.0]),
                x_new().set_f64([10.0, 10.0, 10.0]),
            );
        });
    }

    #[bench]
    fn bencher_par(b: &mut Bencher) {
        let pso = PSO::new(10000, 100, 1.0, 1.0, 0.5, 1.0);

        b.iter(|| {
            pso.min_par(
                |x| (x.f64[0] - 7.0).powi(2) + (x.f64[1] + 3.0).powi(2) + (x.f64[2] + 5.0).powi(2),
                x_new().set_f64([-10.0, -10.0, -10.0]),
                x_new().set_f64([10.0, 10.0, 10.0]),
            );
        });
    }
}
