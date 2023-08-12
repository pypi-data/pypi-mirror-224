#![feature(test)]
#![allow(unused)]
#![feature(associated_const_equality)]
#![feature(auto_traits, negative_impls)]

pub mod prelude;

use prelude::*;

mod particle_swarm_optimization;
mod simulated_annealing;


// mod ant_colony_optimization;
// mod genetic_algorithm;

use array_init;


use core::cmp::{
    Ordering::{self, Equal, Greater, Less},
    PartialOrd,
};

use core::ops::{Add, AddAssign, Div, DivAssign, Mul, MulAssign, Neg, Sub, SubAssign};
use std::cmp::min_by;


use pyo3::types::PyDict;
use pyo3::prelude::*;
use rand::prelude::*;
use rayon::prelude::*;
use rust_decimal::prelude::*;


use num_bigint::BigInt;
use num_complex::{Complex, ComplexDistribution};
use rand::distributions::Uniform;
use rust_decimal::Decimal;
use crate::particle_swarm_optimization::PSO;





/// A Python module implemented in Rust.
#[pymodule]
fn opt_solve(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<PSO>()?;
    Ok(())
}



#[cfg(test)]
mod tests {
    extern crate test;

    use pyo3::types::PyString;
    use test::Bencher;

    use crate::*;

    #[test]
    fn test() {

        Python::with_gil(|py| {

            let one = py.eval("1", None, None).unwrap();
            let two = py.eval("2", None, None).unwrap();
            let res = one.eq(two);

            println!("{:?}", res);
        });
    }

}
