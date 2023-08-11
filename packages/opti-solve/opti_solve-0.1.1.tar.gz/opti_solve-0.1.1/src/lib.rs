#![feature(test)]
#![allow(unused)]
#![feature(associated_const_equality)]
#![feature(auto_traits, negative_impls)]


pub mod prelude;

use prelude::*;

mod particle_swarm_optimization;
// mod simulated_annealing;
// mod ant_colony_optimization;
// mod genetic_algorithm;

use array_init;
use send_wrapper::SendWrapper;



use core::cmp::{PartialOrd,Ordering::{self, Equal, Greater, Less}};
use core::ops::{Add, AddAssign, Div, DivAssign, Mul, MulAssign, Neg, Sub, SubAssign};



use pyo3::prelude::*;
use rand::prelude::*;
use rayon::prelude::*;
use rust_decimal::prelude::*;

use crate::particle_swarm_optimization::PSO;
use num_bigint::BigInt;
use num_complex::{Complex, ComplexDistribution};
use rand::distributions::Uniform;
use rust_decimal::Decimal;

// #[pyclass(subclass)]
// #[derive(Clone, Copy)]
// pub struct OptiBase {
// 	val1: usize,
// }
//
//
// #[pyclass(extends = OptiBase, subclass)]
// pub struct LZQ {
// 	val: usize,
// }
//
// // #[pymethods]
// // impl OptiBase {
// //     #[staticmethod]
// //     fn println(){
// //         println!("794613")
// //     }
// // }
//
//
// /// n:粒子个数,
// /// c1,c2均为加速常数，通常在区间[0,2]内取值
// /// m:迭代次
// #[pyclass(get_all, set_all)]
// #[derive(Clone, Copy)]
// pub struct LiZiQunSuanFa {
// 	n: usize,
// 	m: usize,
// 	c1: f64,
// 	c2: f64,
// }
//
//
// #[pymethods]
// impl LiZiQunSuanFa {
// 	#[new]
// 	#[pyo3(signature = ( n = 2usize, m = 2usize, c1 = 1.064, c2 = 1.0))]
// 	fn new(n: usize, m: usize, c1: f64, c2: f64) -> Self {
// 		Self { n, m, c1, c2 }
// 	}
// }
//
//
// /// Formats the sum of two numbers as string.
// #[pyfunction]
// fn sum_as_string(x: Complex<f64>, y: Complex<f64>) -> Complex<f64> {
// 	return x + y;
// }
//
//
/// A Python module implemented in Rust.
#[pymodule]
fn opti_solve(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<PSO>()?;
    Ok(())
}

#[cfg(test)]
mod tests {
    extern crate test;

    use test::Bencher;
    use pyo3::types::PyString;

    use crate::*;

    #[test]
    fn test() {
        // use num_bigint::BigInt;
        // use num_complex::Complex;
        // use rust_decimal::Decimal;
        // use rand::Rng;
        // use std::ops::Range;
        // use rust_decimal::prelude::FromPrimitive;
        // use num_bigint::{ToBigInt, RandBigInt};
        // use rand::distributions::{Distribution, Uniform};
        // use std::str::FromStr;
        // use num_complex::ComplexDistribution;
        //
        Python::with_gil(|py| {

            let py1 = unsafe {py.new_pool()};

            let one = py1.python().eval("1", None, None).unwrap();
            let two = py1.python().eval("2", None, None).unwrap();
            let res = 0;

            println!("{:?}", res);
        });


    }

    // #[bench]
    // fn bencher(b: &mut Bencher) {
    // 	use std::mem::size_of_val;
    //
    // 	#[bench]
    // 	fn bencher(b: &mut Bencher) {
    // 		use std::mem::size_of_val;
    // 		let pso = particle_swarm_optimization::PSO::new(
    // 			10000, 1000, 1.0, 1.0,
    // 		);
    // 		b.iter(|| pso.min(
    // 			|x| {
    // 				let x = x.f64;
    // 				(x[0] - 7.0).powi(2) + (x[1] + 3.0).powi(2) + (x[1] - 5.0).powi(2)
    // 			},
    // 			x_new().set_f64([-10.0, -10.0, -10.0]),
    // 			x_new().set_f64([10.0, 10.0, 10.0]),
    // 		));
    // 	}
    // }
}
//
//
// use pyo3::prelude::*;
//
// #[pyclass(subclass)]
// struct BaseClass {
// 	val1: usize,
// }
//
// #[pymethods]
// impl BaseClass {
// 	#[new]
// 	fn new() -> Self {
// 		BaseClass { val1: 10 }
// 	}
//
// 	pub fn method(&self) -> PyResult<usize> {
// 		Ok(self.val1)
// 	}
// }
//
// #[pyclass(extends = BaseClass, subclass)]
// struct SubClass {
// 	val2: usize,
// }
//
// #[pymethods]
// impl SubClass {
// 	#[new]
// 	fn new() -> (Self, BaseClass) {
// 		(SubClass { val2: 15 }, BaseClass::new())
// 	}
//
// 	fn method2(self_: PyRef<'_, Self>) -> PyResult<usize> {
// 		let super_ = self_.as_ref(); // Get &BaseClass
// 		super_.method().map(|x| x * self_.val2)
// 	}
// }
//
//
// #[pyclass(extends = SubClass)]
// struct SubSubClass {
// 	val3: usize,
// }
//
// #[pymethods]
// impl SubSubClass {
// 	#[new]
// 	fn new() -> PyClassInitializer<Self> {
// 		PyClassInitializer::from(SubClass::new()).add_subclass(SubSubClass { val3: 20 })
// 	}
//
// 	fn method3(self_: PyRef<'_, Self>) -> PyResult<usize> {
// 		let v = self_.val3;
// 		let super_ = self_.into_super(); // Get PyRef<'_, SubClass>
// 		SubClass::method2(super_).map(|x| x * v)
// 	}
// }
//
