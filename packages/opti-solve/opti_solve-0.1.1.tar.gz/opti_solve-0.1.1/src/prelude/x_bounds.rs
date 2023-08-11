use super::*;

pub struct XBounds<
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
> {
    pub i8: [Uniform<i8>; I8],
    pub i16: [Uniform<i16>; I16],
    pub i32: [Uniform<i32>; I32],
    pub i64: [Uniform<i64>; I64],
    pub i128: [Uniform<i128>; I128],
    pub i: [Uniform<BigInt>; I],
    pub f32: [Uniform<f32>; F32],
    pub f64: [Uniform<f64>; F64],
    pub c64: [ComplexDistribution<Uniform<f32>>; C64],
    pub c128: [ComplexDistribution<Uniform<f64>>; C128],
    pub d: [Uniform<Decimal>; D],
}

impl<
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
    > Distribution<X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>>
    for XBounds<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    fn sample<R: Rng + ?Sized>(
        &self,
        rng: &mut R,
    ) -> X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D> {
        X {
            i8: self.i8.map(|uniform| rng.sample(uniform)),
            i16: self.i16.map(|uniform| rng.sample(uniform)),
            i32: self.i32.map(|uniform| rng.sample(uniform)),
            i64: self.i64.map(|uniform| rng.sample(uniform)),
            i128: self.i128.map(|uniform| rng.sample(uniform)),
            i: self.i.clone().map(|uniform| rng.sample(uniform)),
            f32: self.f32.map(|uniform| rng.sample(uniform)),
            f64: self.f64.map(|uniform| rng.sample(uniform)),
            c64: self.c64.map(|uniform| rng.sample(uniform)),
            c128: self.c128.map(|uniform| rng.sample(uniform)),
            d: self.d.map(|uniform| rng.sample(uniform)),
        }
    }
}

impl<
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
    > XBounds<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    pub fn new(
        x_min: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
        x_max: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
    ) -> Self {
        Self {
            i8: array_init::array_init(|i| unsafe {
                Uniform::from(*x_min.i8.get_unchecked(i)..*x_max.i8.get_unchecked(i))
            }),
            i16: array_init::array_init(|i| unsafe {
                Uniform::from(*x_min.i16.get_unchecked(i)..*x_max.i16.get_unchecked(i))
            }),
            i32: array_init::array_init(|i| unsafe {
                Uniform::from(*x_min.i32.get_unchecked(i)..*x_max.i32.get_unchecked(i))
            }),
            i64: array_init::array_init(|i| unsafe {
                Uniform::from(*x_min.i64.get_unchecked(i)..*x_max.i64.get_unchecked(i))
            }),
            i128: array_init::array_init(|i| unsafe {
                Uniform::from(*x_min.i128.get_unchecked(i)..*x_max.i128.get_unchecked(i))
            }),
            i: array_init::array_init(|i| unsafe {
                Uniform::from(x_min.i.get_unchecked(i).clone()..x_max.i.get_unchecked(i).clone())
            }),
            f32: array_init::array_init(|i| unsafe {
                Uniform::from(*x_min.f32.get_unchecked(i)..*x_max.f32.get_unchecked(i))
            }),
            f64: array_init::array_init(|i| unsafe {
                Uniform::from(*x_min.f64.get_unchecked(i)..*x_max.f64.get_unchecked(i))
            }),
            c64: array_init::array_init(|i| unsafe {
                ComplexDistribution::new(
                    Uniform::from(x_min.c64[i].re..x_max.c64[i].re),
                    Uniform::from(x_min.c64[i].im..x_max.c64[i].im),
                )
            }),
            c128: array_init::array_init(|i| unsafe {
                ComplexDistribution::new(
                    Uniform::from(x_min.c128[i].re..x_max.c128[i].re),
                    Uniform::from(x_min.c128[i].im..x_max.c128[i].im),
                )
            }),
            d: array_init::array_init(|i| unsafe {
                Uniform::from(x_min.d[i].clone()..x_max.d[i].clone())
            }),
        }
    }
}
