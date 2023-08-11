// use std::ops::Neg;
// use crate::Opti;
// use pyo3::prelude::*;
//
// /// genetic_algorithm 遗传算法
// #[derive(Clone, Copy)]
// #[pyclass]
// pub struct GA{
// 	#[pyo3(get, set)]
//     n: usize,
//     #[pyo3(get, set)]
//     m: usize,
//     #[pyo3(get, set)]
//     c1: f64,
//     #[pyo3(get, set)]
//     c2: f64,
// }
//
//
//
// // impl Opti for GA {
// // 	fn min<const F: usize, O: PartialOrd + Neg<Output=O>>(self, f: impl Fn([f64; F]) -> f64, x_min: [f64; F], x_max: [f64; F]) -> ([f64; F], O) {
// // 		todo!()
// // 	}
// // 	fn min_gin<const F: usize, const I: usize, O: PartialOrd + Neg<Output=O>>(self, f: impl Fn([f64; F], [isize; I]) -> f64, xf_min: [f64; F], xf_max: [f64; F], xi_min: [isize; I], xi_max: [isize; I]) -> ([f64; F], [isize; I], O) {
// // 		todo!()
// // 	}
// // 	fn min_bin<const F: usize, const B: usize, O: PartialOrd + Neg<Output=O>>(self, f: impl Fn([f64; F], [bool; B]) -> f64, x_min: [f64; F], x_max: [f64; F]) -> ([f64; F], [bool; B], O) {
// // 		todo!()
// // 	}
// // 	fn min_gin_bin<const F: usize, const I: usize, const B: usize, O: PartialOrd + Neg<Output=O>>(self, f: impl Fn([f64; F], [isize; I], [bool; B]) -> f64, xf_min: [f64; F], xf_max: [f64; F], xi_min: [isize; I], xi_max: [isize; I]) -> ([f64; F], [isize; I], [bool; B], O) {
// // 		todo!()
// // 	}
// // }
