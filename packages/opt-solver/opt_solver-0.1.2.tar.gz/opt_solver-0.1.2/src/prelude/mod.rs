mod optimization;
pub use optimization::*;
mod x;
pub use x::*;
mod x_vec;
pub use x_vec::*;
mod x_bounds;
pub use x_bounds::*;
mod x_vec_bounds;
pub use x_vec_bounds::*;
mod py_wrapper;
pub use py_wrapper::*;

pub use crate::*;

#[macro_export]
macro_rules! mul_assign_float {
    ($self:tt,$other_f32:expr,$other_f64:expr) => {
        $self
            .i8
            .iter_mut()
            .for_each(|x| *x = ((*x as f32) * $other_f32) as i8);
        $self
            .i16
            .iter_mut()
            .for_each(|x| *x = ((*x as f32) * $other_f32) as i16);
        $self
            .i32
            .iter_mut()
            .for_each(|x| *x = ((*x as f64) * $other_f64) as i32);
        $self
            .i64
            .iter_mut()
            .for_each(|x| *x = ((*x as f64) * $other_f64) as i64);
        $self
            .i128
            .iter_mut()
            .for_each(|x| *x = ((*x as f64) * $other_f64) as i128);
        $self.i.iter_mut().for_each(|x| {
            *x = BigInt::from_f64(x.to_f64().expect("BigInt can not to f64") * $other_f64)
                .expect("f64 can not to BigInt")
        });
        $self.f32.iter_mut().for_each(|x| *x = *x * $other_f32);
        $self.f64.iter_mut().for_each(|x| *x = *x * $other_f64);
        $self.c64.iter_mut().for_each(|x| *x = *x * $other_f32);
        $self.c128.iter_mut().for_each(|x| *x = *x * $other_f64);
        $self.d.iter_mut().for_each(|x| {
            *x = *x * Decimal::from_f64($other_f64).expect("Failed to convert to Decimal")
        });
    };
}
