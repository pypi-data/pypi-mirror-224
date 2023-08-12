mod min;
mod min_par;
mod min_vec;
mod min_vec_par;

use std::cmp::min;

use crate::*;
use crate::particle_swarm_optimization::min_par::min_par;
use crate::particle_swarm_optimization::min_vec_par::min_vec_par;

#[doc=include_str!("PSO.md")]
#[derive(Clone, Copy, Debug, PartialEq, Default)]
#[pyclass(get_all, set_all)]
pub struct PSO {
    pub n_iters: usize,
    pub n_particles: usize,
    pub c1: f64,
    pub c2: f64,
    pub inertia: f64,
    pub max_v: f64,
}

impl Opt for PSO {
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
        min::min(self, f, x_min, x_max)
    }

    fn min_vec<O: PartialOrd + Clone>(
        &self,
        f: impl Fn(XVec) -> O,
        x_min: XVec,
        x_max: XVec,
    ) -> (O, XVec) {
        min_vec::min_vec(self, f, x_min, x_max)
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
        min_par(self, f, x_min, x_max)
    }

    fn min_vec_par<O: PartialOrd + Clone + Sync + Send>(
        &self,
        f: impl Fn(XVec) -> O + Sync,
        x_min: XVec,
        x_max: XVec,
    ) -> (O, XVec) {
        min_vec_par(self, f, x_min, x_max)
    }
}

#[pymethods]
impl PSO {
    #[new]
    #[pyo3(signature = (n_iters = 1000, n_particles = 30, c1 = 2.0, c2 = 2.0,   inertia = 0.5 , max_v = 0.2, ))]
    pub fn new(
        n_iters: usize,
        n_particles: usize,
        c1: f64,
        c2: f64,
        inertia: f64,
        max_v: f64,
    ) -> Self {
        Self {
            n_iters,
            n_particles,
            c1,
            c2,

            inertia,
            max_v,
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

    fn f(x: X<0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0>) -> f64 {
        (x.f64[0] - 7.0).powi(2) + (x.f64[1] + 3.0).powi(2) + (x.f64[2] + 5.0).powi(2)
    }

    #[test]
    fn it_works() {
        let x_min = x_new().set_f64([-10.0, -10.0, -10.0]);
        let x_max = x_new().set_f64([10.0, 10.0, 10.0]);

        let pso = PSO::new(1000, 10000, 2.0, 2.0, 0.2, 0.2);

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
        let pso = PSO::new(1000, 10000, 2.0, 2.0, 0.2, 0.2);

        b.iter(|| {
            pso.min(
                f,
                x_new().set_f64([-10.0, -10.0, -10.0]),
                x_new().set_f64([10.0, 10.0, 10.0]),
            );
        });
    }

    #[bench]
    fn bencher_par(b: &mut Bencher) {
        let pso = PSO::new(1000, 10000, 2.0, 2.0, 0.2, 0.2);

        b.iter(|| {
            pso.min_par(
                f,
                x_new().set_f64([-10.0, -10.0, -10.0]),
                x_new().set_f64([10.0, 10.0, 10.0]),
            );
        });
    }
}
