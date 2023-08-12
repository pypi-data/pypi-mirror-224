use crate::prelude::X;
use num_bigint::BigInt;
use num_complex::Complex;
use pyo3::types::PyDict;
use std::ops::Neg;

use super::*;

#[derive(Debug, Clone)]
pub struct XVec {
    pub i8: Vec<i8>,
    pub i16: Vec<i16>,
    pub i32: Vec<i32>,
    pub i64: Vec<i64>,
    pub i128: Vec<i128>,
    pub i: Vec<BigInt>,
    pub f32: Vec<f32>,
    pub f64: Vec<f64>,
    pub c64: Vec<Complex<f32>>,
    pub c128: Vec<Complex<f64>>,
    pub d: Vec<Decimal>,
}

impl IntoPy<Py<PyDict>> for XVec {
    fn into_py(self, py: Python<'_>) -> Py<PyDict> {
        let dict = PyDict::new(py);
        macro_rules! set_item {
            ($x:ident) => {
                if self.$x.len() != 0 {
                    dict.set_item(stringify!($x), self.$x.into_py(py)).unwrap();
                }
            };
        }
        set_item!(i8);
        set_item!(i16);
        set_item!(i32);
        set_item!(i64);
        set_item!(i128);
        set_item!(i);
        set_item!(f32);
        set_item!(f64);
        set_item!(c64);
        set_item!(c128);
        set_item!(d);

        dict.into()
    }
}

impl Neg for XVec {
    type Output = Self;
    fn neg(self) -> Self::Output {
        macro_rules! array_neg {
            ($a:expr) => {
                $a.into_iter().map(|i| -i).collect()
            };
        }

        XVec {
            i8: array_neg!(self.i8),
            i16: array_neg!(self.i16),
            i32: array_neg!(self.i32),
            i64: array_neg!(self.i64),
            i128: array_neg!(self.i128),
            i: array_neg!(self.i),
            f32: array_neg!(self.f32),
            f64: array_neg!(self.f64),
            c64: array_neg!(self.c64),
            c128: array_neg!(self.c128),
            d: array_neg!(self.d),
        }
    }
}

impl Add for XVec {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        macro_rules! array_add {
            ($a:expr, $b:expr) => {
                $a.into_iter()
                    .zip($b.into_iter())
                    .map(|(a, b)| a + b)
                    .collect()
            };
        }

        XVec {
            i8: array_add!(self.i8, other.i8),
            i16: array_add!(self.i16, other.i16),
            i32: array_add!(self.i32, other.i32),
            i64: array_add!(self.i64, other.i64),
            i128: array_add!(self.i128, other.i128),
            i: array_add!(self.i, other.i),
            f32: array_add!(self.f32, other.f32),
            f64: array_add!(self.f64, other.f64),
            c64: array_add!(self.c64, other.c64),
            c128: array_add!(self.c128, other.c128),
            d: array_add!(self.d, other.d),
        }
    }
}

impl Sub for XVec {
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        macro_rules! array_sub {
            ($a:expr, $b:expr) => {
                $a.into_iter()
                    .zip($b.into_iter())
                    .map(|(a, b)| a - b)
                    .collect()
            };
        }

        XVec {
            i8: array_sub!(self.i8, other.i8),
            i16: array_sub!(self.i16, other.i16),
            i32: array_sub!(self.i32, other.i32),
            i64: array_sub!(self.i64, other.i64),
            i128: array_sub!(self.i128, other.i128),
            i: array_sub!(self.i, other.i),
            f32: array_sub!(self.f32, other.f32),
            f64: array_sub!(self.f64, other.f64),
            c64: array_sub!(self.c64, other.c64),
            c128: array_sub!(self.c128, other.c128),
            d: array_sub!(self.d, other.d),
        }
    }
}

impl Mul for XVec {
    type Output = Self;

    fn mul(self, other: Self) -> Self {
        macro_rules! array_mul {
            ($a:expr, $b:expr) => {
                $a.into_iter()
                    .zip($b.into_iter())
                    .map(|(a, b)| a * b)
                    .collect()
            };
        }

        XVec {
            i8: array_mul!(self.i8, other.i8),
            i16: array_mul!(self.i16, other.i16),
            i32: array_mul!(self.i32, other.i32),
            i64: array_mul!(self.i64, other.i64),
            i128: array_mul!(self.i128, other.i128),
            i: array_mul!(self.i, other.i),
            f32: array_mul!(self.f32, other.f32),
            f64: array_mul!(self.f64, other.f64),
            c64: array_mul!(self.c64, other.c64),
            c128: array_mul!(self.c128, other.c128),
            d: array_mul!(self.d, other.d),
        }
    }
}

impl Div for XVec {
    type Output = Self;

    fn div(self, other: Self) -> Self {
        macro_rules! array_div {
            ($a:expr, $b:expr) => {
                $a.into_iter()
                    .zip($b.into_iter())
                    .map(|(a, b)| a / b)
                    .collect()
            };
        }

        XVec {
            i8: array_div!(self.i8, other.i8),
            i16: array_div!(self.i16, other.i16),
            i32: array_div!(self.i32, other.i32),
            i64: array_div!(self.i64, other.i64),
            i128: array_div!(self.i128, other.i128),
            i: array_div!(self.i, other.i),
            f32: array_div!(self.f32, other.f32),
            f64: array_div!(self.f64, other.f64),
            c64: array_div!(self.c64, other.c64),
            c128: array_div!(self.c128, other.c128),
            d: array_div!(self.d, other.d),
        }
    }
}

impl AddAssign for XVec {
    fn add_assign(&mut self, other: Self) {
        macro_rules! array_add_assign {
            ($a:expr, $b:expr) => {
                $a.iter_mut().zip($b.iter()).for_each(|(a, b)| {
                    *a += b;
                })
            };
        }
        array_add_assign!(self.i8, other.i8);
        array_add_assign!(self.i16, other.i16);
        array_add_assign!(self.i32, other.i32);
        array_add_assign!(self.i64, other.i64);
        array_add_assign!(self.i128, other.i128);
        array_add_assign!(self.i, other.i);
        array_add_assign!(self.f32, other.f32);
        array_add_assign!(self.f64, other.f64);
        array_add_assign!(self.c64, other.c64);
        array_add_assign!(self.c128, other.c128);
        array_add_assign!(self.d, other.d);
    }
}

impl SubAssign for XVec {
    fn sub_assign(&mut self, other: Self) {
        macro_rules! array_sub_assign {
            ($a:expr, $b:expr) => {
                $a.iter_mut().zip($b.iter()).for_each(|(a, b)| {
                    *a += b;
                })
            };
        }
        array_sub_assign!(self.i8, other.i8);
        array_sub_assign!(self.i16, other.i16);
        array_sub_assign!(self.i32, other.i32);
        array_sub_assign!(self.i64, other.i64);
        array_sub_assign!(self.i128, other.i128);
        array_sub_assign!(self.i, other.i);
        array_sub_assign!(self.f32, other.f32);
        array_sub_assign!(self.f64, other.f64);
        array_sub_assign!(self.c64, other.c64);
        array_sub_assign!(self.c128, other.c128);
        array_sub_assign!(self.d, other.d);
    }
}

impl MulAssign for XVec {
    fn mul_assign(&mut self, other: Self) {
        macro_rules! array_mul_assign {
            ($a:expr, $b:expr) => {
                $a.iter_mut().zip($b.iter()).for_each(|(a, b)| {
                    *a += b;
                })
            };
        }
        array_mul_assign!(self.i8, other.i8);
        array_mul_assign!(self.i16, other.i16);
        array_mul_assign!(self.i32, other.i32);
        array_mul_assign!(self.i64, other.i64);
        array_mul_assign!(self.i128, other.i128);
        array_mul_assign!(self.i, other.i);
        array_mul_assign!(self.f32, other.f32);
        array_mul_assign!(self.f64, other.f64);
        array_mul_assign!(self.c64, other.c64);
        array_mul_assign!(self.c128, other.c128);
        array_mul_assign!(self.d, other.d);
    }
}

impl DivAssign for XVec {
    fn div_assign(&mut self, other: Self) {
        macro_rules! array_div_assign {
            ($a:expr, $b:expr) => {
                $a.iter_mut().zip($b.iter()).for_each(|(a, b)| {
                    *a += b;
                })
            };
        }
        array_div_assign!(self.i8, other.i8);
        array_div_assign!(self.i16, other.i16);
        array_div_assign!(self.i32, other.i32);
        array_div_assign!(self.i64, other.i64);
        array_div_assign!(self.i128, other.i128);
        array_div_assign!(self.i, other.i);
        array_div_assign!(self.f32, other.f32);
        array_div_assign!(self.f64, other.f64);
        array_div_assign!(self.c64, other.c64);
        array_div_assign!(self.c128, other.c128);
        array_div_assign!(self.d, other.d);
    }
}

impl Distribution<XVec> for XVec {
    fn sample<R: Rng + ?Sized>(&self, rng: &mut R) -> XVec {
        macro_rules! choice_0_to_x {
            ($t:tt) => {
                self.$t
                    .iter()
                    .map(|&x| match x.cmp(&0) {
                        Less => rng.gen_range(x..0),
                        Equal => 0,
                        Greater => rng.gen_range(0..x),
                    })
                    .collect()
            };

            ($t:tt,$zero:expr) => {
                self.$t
                    .iter()
                    .map(|&x| match x.cmp(&$zero) {
                        Less => rng.gen_range(x..$zero),
                        Equal => $zero,
                        Greater => rng.gen_range($zero..x),
                    })
                    .collect()
            };
        }

        macro_rules! choice_0_to_x_float {
			($($t:tt)*) =>{
				match $($t)*.partial_cmp(&0.0).expect("NaN values cannot be used in this range!"){
					Less=> rng.gen_range($($t)*..0.0),
					Equal=> 0.0,
					Greater=> rng.gen_range(0.0..$($t)*),
				}
			}
		}

        XVec {
            i8: choice_0_to_x!(i8),
            i16: choice_0_to_x!(i16),
            i32: choice_0_to_x!(i32),
            i64: choice_0_to_x!(i64),
            i128: choice_0_to_x!(i128),
            i: self
                .i
                .clone()
                .into_iter()
                .map(|x| {
                    let zero = BigInt::from(0);
                    match x.cmp(&zero) {
                        Less => rng.gen_range(x..zero),
                        Equal => zero,
                        Greater => rng.gen_range(zero..x),
                    }
                })
                .collect(),
            f32: self.f32.iter().map(|&x| choice_0_to_x_float!(x)).collect(),
            f64: self.f64.iter().map(|&x| choice_0_to_x_float!(x)).collect(),
            c64: self
                .c64
                .iter()
                .map(|x| Complex::new(choice_0_to_x_float!(x.im), choice_0_to_x_float!(x.re)))
                .collect(),
            c128: self
                .c128
                .iter()
                .map(|x| Complex::new(choice_0_to_x_float!(x.im), choice_0_to_x_float!(x.re)))
                .collect(),
            d: choice_0_to_x!(d, Decimal::from(0)),
        }
    }
}

impl XVec {
    pub fn new() -> Self {
        Self {
            i8: Vec::new(),
            i16: Vec::new(),
            i32: Vec::new(),
            i64: Vec::new(),
            i128: Vec::new(),
            i: Vec::new(),
            f32: Vec::new(),
            f64: Vec::new(),
            c64: Vec::new(),
            c128: Vec::new(),
            d: Vec::new(),
        }
    }

    pub fn new_with_capacity(
        capacity_i8: usize,
        capacity_i16: usize,
        capacity_i32: usize,
        capacity_i64: usize,
        capacity_i128: usize,
        capacity_i: usize,
        capacity_f32: usize,
        capacity_f64: usize,
        capacity_c64: usize,
        capacity_c128: usize,
        capacity_d: usize,
    ) -> Self {
        Self {
            i8: Vec::with_capacity(capacity_i8),
            i16: Vec::with_capacity(capacity_i16),
            i32: Vec::with_capacity(capacity_i32),
            i64: Vec::with_capacity(capacity_i64),
            i128: Vec::with_capacity(capacity_i128),
            i: Vec::with_capacity(capacity_i),
            f32: Vec::with_capacity(capacity_f32),
            f64: Vec::with_capacity(capacity_f64),
            c64: Vec::with_capacity(capacity_c64),
            c128: Vec::with_capacity(capacity_c128),
            d: Vec::with_capacity(capacity_d),
        }
    }

    pub fn zero(&self) -> Self {
        Self {
            i8: vec![0; self.i8.len()],
            i16: vec![0; self.i16.len()],
            i32: vec![0; self.i32.len()],
            i64: vec![0; self.i64.len()],
            i128: vec![0; self.i128.len()],
            i: (0..self.i.len()).map(|_| BigInt::from(0)).collect(),
            f32: vec![0.0; self.f32.len()],
            f64: vec![0.0; self.f64.len()],
            c64: vec![Complex::new(0.0, 0.0); self.c64.len()],
            c128: vec![Complex::new(0.0, 0.0); self.c128.len()],
            d: vec![Decimal::from(0); self.d.len()],
        }
    }

    pub fn mul_assign_f64(&mut self, other: f64) {
        let other_f32 = other as f32;
        mul_assign_float!(self, other_f32, other);
    }

    pub fn mul_f64(mut self, other: f64) -> Self {
        self.mul_assign_f64(other);
        self
    }

    pub fn mul_assign_f32(&mut self, other: f32) {
        let other_f64 = other as f64;
        mul_assign_float!(self, other, other_f64);
    }

    pub fn mul_f32(mut self, other: f32) -> Self {
        self.mul_assign_f32(other);
        self
    }
}
