use super::*;

pub trait Opt {
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
    ) -> (O, X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>);

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
        self.min(f, x_min, x_max)
    }

    fn min_vec<O: PartialOrd + Clone>(
        &self,
        f: impl Fn(XVec) -> O,
        x_min: XVec,
        x_max: XVec,
    ) -> (O, XVec);

    fn min_vec_par<O: PartialOrd + Clone + Sync + Send>(
        &self,
        f: impl Fn(XVec) -> O + Sync,
        x_min: XVec,
        x_max: XVec,
    ) -> (O, XVec) {
        self.min_vec(f, x_min, x_max)
    }

    fn max<
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
        O: PartialOrd + Neg<Output = NegO>,
        NegO: PartialOrd + Neg<Output = NegNegO> + Clone,
        NegNegO,
    >(
        &self,
        f: impl Fn(X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>) -> O,
        x_min: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
        x_max: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
    ) -> (
        NegNegO,
        X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
    ) {
        let (f_val, x) = self.min(|x| -f(x), x_min, x_max);
        (-f_val, x)
    }

    fn max_par<
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
        O: PartialOrd + Neg<Output = NegO>,
        NegO: PartialOrd + Neg<Output = NegNegO> + Clone + Sync + Send,
        NegNegO,
    >(
        &self,
        f: impl Fn(X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>) -> O + Sync,
        x_min: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
        x_max: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
    ) -> (
        NegNegO,
        X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
    ) {
        let (f_val, x) = self.min_par(|x| -f(x), x_min, x_max);
        (-f_val, x)
    }

    fn max_vec<
        O: PartialOrd + Neg<Output = NegO>,
        NegO: PartialOrd + Neg<Output = NegNegO> + Clone,
        NegNegO,
    >(
        &self,
        f: impl Fn(XVec) -> O,
        x_min: XVec,
        x_max: XVec,
    ) -> (NegNegO, XVec) {
        let (f_val, x) = self.min_vec(|x| -f(x), x_min, x_max);
        (-f_val, x)
    }

    fn max_vec_par<
        O: PartialOrd + Neg<Output = NegO>,
        NegO: PartialOrd + Neg<Output = NegNegO> + Clone + Sync + Send,
        NegNegO,
    >(
        &self,
        f: impl Fn(XVec) -> O + Sync,
        x_min: XVec,
        x_max: XVec,
    ) -> (NegNegO, XVec) {
        let (f_val, x) = self.min_vec_par(|x| -f(x), x_min, x_max);
        (-f_val, x)
    }
}
