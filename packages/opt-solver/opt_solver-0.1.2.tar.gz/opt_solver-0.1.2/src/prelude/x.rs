use super::*;

#[derive(Debug, Clone, PartialEq)]
pub struct X<
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
    pub i8: [i8; I8],
    pub i16: [i16; I16],
    pub i32: [i32; I32],
    pub i64: [i64; I64],
    pub i128: [i128; I128],
    pub i: [BigInt; I],
    pub f32: [f32; F32],
    pub f64: [f64; F64],
    pub c64: [Complex<f32>; C64],
    pub c128: [Complex<f64>; C128],
    pub d: [Decimal; D],
}

pub const fn x_new() -> X<0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0> {
    X {
        i8: [],
        i16: [],
        i32: [],
        i64: [],
        i128: [],
        i: [],
        f32: [],
        f64: [],
        c64: [],
        c128: [],
        d: [],
    }
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
    > Send for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
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
    > Sync for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
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
    > Neg for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    type Output = Self;
    fn neg(self) -> Self::Output {
        macro_rules! array_neg {
            ($a:expr) => {
                array_init::array_init(|i| unsafe { -$a.get_unchecked(i) })
            };
        }

        X {
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
    > Add for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    type Output = Self;

    fn add(self, other: Self) -> Self {
        macro_rules! array_add {
            ($a:expr, $b:expr) => {
                array_init::array_init(|i| unsafe { $a.get_unchecked(i) + $b.get_unchecked(i) })
            };
        }

        X {
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
    > AddAssign for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
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
    > Sub for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        macro_rules! array_sub {
            ($a:expr, $b:expr ) => {
                array_init::array_init(|i| unsafe { $a.get_unchecked(i) - $b.get_unchecked(i) })
            };
        }
        X {
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
    > SubAssign for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    fn sub_assign(&mut self, other: Self) {
        macro_rules! array_sub_assign {
            ($a:expr, $b:expr) => {
                $a.iter_mut().zip($b.iter()).for_each(|(a, b)| {
                    *a -= b;
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
    > Mul for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    type Output = Self;

    fn mul(self, other: Self) -> Self {
        macro_rules! array_mul {
            ($a:expr, $b:expr ) => {
                array_init::array_init(|i| unsafe { $a.get_unchecked(i) * $b.get_unchecked(i) })
            };
        }
        X {
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
    > MulAssign for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    fn mul_assign(&mut self, other: Self) {
        macro_rules! array_mul_assign {
            ($a:expr, $b:expr) => {
                $a.iter_mut().zip($b.iter()).for_each(|(a, b)| {
                    *a *= b;
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
    > Div for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    type Output = Self;

    fn div(self, other: Self) -> Self {
        macro_rules! array_div {
            ($a:expr, $b:expr ) => {
                array_init::array_init(|i| unsafe { $a.get_unchecked(i) / $b.get_unchecked(i) })
            };
        }
        X {
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
    > DivAssign for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    fn div_assign(&mut self, other: Self) {
        macro_rules! array_div_assign {
            ($a:expr, $b:expr) => {
                $a.iter_mut().zip($b.iter()).for_each(|(a, b)| {
                    *a /= b;
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
    for X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
    fn sample<R: Rng + ?Sized>(
        &self,
        rng: &mut R,
    ) -> X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D> {
        macro_rules! choice_0_to_x {
            ($t:tt) => {
                self.$t.map(|x| match x.cmp(&0) {
                    Less => rng.gen_range(x..0),
                    Equal => 0,
                    Greater => rng.gen_range(0..x),
                })
            };

            ($t:tt,$zero:expr) => {
                self.$t.map(|x| match x.cmp(&$zero) {
                    Less => rng.gen_range(x..$zero),
                    Equal => $zero,
                    Greater => rng.gen_range($zero..x),
                })
            };
        }

        macro_rules! choice_0_to_x_float {
			($($t:tt)*) =>{
				match $($t)*.partial_cmp(&0.0).unwrap_or_else(
					||panic!("NaN values cannot be used in this range!")){
					Less=> rng.gen_range($($t)*..0.0),
					Equal=> 0.0,
					Greater=> rng.gen_range(0.0..$($t)*),
				}
			}
		}

        X {
            i8: choice_0_to_x!(i8),
            i16: choice_0_to_x!(i16),
            i32: choice_0_to_x!(i32),
            i64: choice_0_to_x!(i64),
            i128: choice_0_to_x!(i128),
            i: array_init::array_init(|index| unsafe {
                let zero = BigInt::from(0);
                let x = unsafe { self.i.get_unchecked(index) };
                match x.cmp(&zero) {
                    Less => rng.gen_range(x.clone()..zero),
                    Equal => zero,
                    Greater => rng.gen_range(zero..x.clone()),
                }
            }),
            f32: self.f32.map(|x| choice_0_to_x_float!(x)),
            f64: self.f64.map(|x| choice_0_to_x_float!(x)),
            c64: self
                .c64
                .map(|x| Complex::new(choice_0_to_x_float!(x.im), choice_0_to_x_float!(x.re))),
            c128: self
                .c128
                .map(|x| Complex::new(choice_0_to_x_float!(x.im), choice_0_to_x_float!(x.re))),
            d: choice_0_to_x!(d, Decimal::from(0)),
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
    > X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>
{
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

    pub fn zero() -> Self {
        Self {
            i8: [0; I8],
            i16: [0; I16],
            i32: [0; I32],
            i64: [0; I64],
            i128: [0; I128],
            i: [(); I].map(|_| BigInt::from(0)),
            f32: [0.0; F32],
            f64: [0.0; F64],
            c64: [Complex::new(0.0, 0.0); C64],
            c128: [Complex::new(0.0, 0.0); C128],
            d: [Decimal::from(0); D],
        }
    }

    pub fn set_i8<const N: usize>(
        self,
        x: [i8; N],
    ) -> X<N, I16, I32, I64, I128, I, F32, F64, C64, C128, D> {
        X {
            i8: x,
            i16: self.i16,
            i32: self.i32,
            i64: self.i64,
            i128: self.i128,
            i: self.i,
            f32: self.f32,
            f64: self.f64,
            c64: self.c64,
            c128: self.c128,
            d: self.d,
        }
    }

    pub fn set_i16<const N: usize>(
        self,
        x: [i16; N],
    ) -> X<I8, N, I32, I64, I128, I, F32, F64, C64, C128, D> {
        X {
            i8: self.i8,
            i16: x,
            i32: self.i32,
            i64: self.i64,
            i128: self.i128,
            i: self.i,
            f32: self.f32,
            f64: self.f64,
            c64: self.c64,
            c128: self.c128,
            d: self.d,
        }
    }
    pub fn set_i32<const N: usize>(
        self,
        x: [i32; N],
    ) -> X<I8, I16, N, I64, I128, I, F32, F64, C64, C128, D> {
        X {
            i8: self.i8,
            i16: self.i16,
            i32: x,
            i64: self.i64,
            i128: self.i128,
            i: self.i,
            f32: self.f32,
            f64: self.f64,
            c64: self.c64,
            c128: self.c128,
            d: self.d,
        }
    }

    pub fn set_i64<const N: usize>(
        self,
        x: [i64; N],
    ) -> X<I8, I16, I32, N, I128, I, F32, F64, C64, C128, D> {
        X {
            i8: self.i8,
            i16: self.i16,
            i32: self.i32,
            i64: x,
            i128: self.i128,
            i: self.i,
            f32: self.f32,
            f64: self.f64,
            c64: self.c64,
            c128: self.c128,
            d: self.d,
        }
    }

    pub fn set_i128<const N: usize>(
        self,
        x: [i128; N],
    ) -> X<I8, I16, I32, I64, N, I, F32, F64, C64, C128, D> {
        X {
            i8: self.i8,
            i16: self.i16,
            i32: self.i32,
            i64: self.i64,
            i128: x,
            i: self.i,
            f32: self.f32,
            f64: self.f64,
            c64: self.c64,
            c128: self.c128,
            d: self.d,
        }
    }

    pub fn set_i<const N: usize>(
        self,
        x: [BigInt; N],
    ) -> X<I8, I16, I32, I64, I128, N, F32, F64, C64, C128, D> {
        X {
            i8: self.i8,
            i16: self.i16,
            i32: self.i32,
            i64: self.i64,
            i128: self.i128,
            i: x,
            f32: self.f32,
            f64: self.f64,
            c64: self.c64,
            c128: self.c128,
            d: self.d,
        }
    }

    pub fn set_f32<const N: usize>(
        self,
        x: [f32; N],
    ) -> X<I8, I16, I32, I64, I128, I, N, F64, C64, C128, D> {
        X {
            i8: self.i8,
            i16: self.i16,
            i32: self.i32,
            i64: self.i64,
            i128: self.i128,
            i: self.i,
            f32: x,
            f64: self.f64,
            c64: self.c64,
            c128: self.c128,
            d: self.d,
        }
    }

    pub fn set_f64<const N: usize>(
        self,
        x: [f64; N],
    ) -> X<I8, I16, I32, I64, I128, I, F32, N, C64, C128, D> {
        X {
            i8: self.i8,
            i16: self.i16,
            i32: self.i32,
            i64: self.i64,
            i128: self.i128,
            i: self.i,
            f32: self.f32,
            f64: x,
            c64: self.c64,
            c128: self.c128,
            d: self.d,
        }
    }

    pub fn set_c64<const N: usize>(
        self,
        x: [Complex<f32>; N],
    ) -> X<I8, I16, I32, I64, I128, I, F32, F64, N, C128, D> {
        X {
            i8: self.i8,
            i16: self.i16,
            i32: self.i32,
            i64: self.i64,
            i128: self.i128,
            i: self.i,
            f32: self.f32,
            f64: self.f64,
            c64: x,
            c128: self.c128,
            d: self.d,
        }
    }

    pub fn set_c128<const N: usize>(
        self,
        x: [Complex<f64>; N],
    ) -> X<I8, I16, I32, I64, I128, I, F32, F64, C64, N, D> {
        X {
            i8: self.i8,
            i16: self.i16,
            i32: self.i32,
            i64: self.i64,
            i128: self.i128,
            i: self.i,
            f32: self.f32,
            f64: self.f64,
            c64: self.c64,
            c128: x,
            d: self.d,
        }
    }

    pub fn set_d<const N: usize>(
        self,
        x: [Decimal; N],
    ) -> X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, N> {
        X {
            i8: self.i8,
            i16: self.i16,
            i32: self.i32,
            i64: self.i64,
            i128: self.i128,
            i: self.i,
            f32: self.f32,
            f64: self.f64,
            c64: self.c64,
            c128: self.c128,
            d: x,
        }
    }
}
