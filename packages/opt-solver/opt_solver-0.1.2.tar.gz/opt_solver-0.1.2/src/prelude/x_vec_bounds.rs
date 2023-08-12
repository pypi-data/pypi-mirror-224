use super::*;

pub struct XVecBounds {
    pub i8: Vec<Uniform<i8>>,
    pub i16: Vec<Uniform<i16>>,
    pub i32: Vec<Uniform<i32>>,
    pub i64: Vec<Uniform<i64>>,
    pub i128: Vec<Uniform<i128>>,
    pub i: Vec<Uniform<BigInt>>,
    pub f32: Vec<Uniform<f32>>,
    pub f64: Vec<Uniform<f64>>,
    pub c64: Vec<ComplexDistribution<Uniform<f32>>>,
    pub c128: Vec<ComplexDistribution<Uniform<f64>>>,
    pub d: Vec<Uniform<Decimal>>,
}

impl Distribution<XVec> for XVecBounds {
    fn sample<R: Rng + ?Sized>(&self, rng: &mut R) -> XVec {
        XVec {
            i8: self.i8.iter().map(|uniform| rng.sample(uniform)).collect(),
            i16: self.i16.iter().map(|uniform| rng.sample(uniform)).collect(),
            i32: self.i32.iter().map(|uniform| rng.sample(uniform)).collect(),
            i64: self.i64.iter().map(|uniform| rng.sample(uniform)).collect(),
            i128: self
                .i128
                .iter()
                .map(|uniform| rng.sample(uniform))
                .collect(),
            i: self
                .i
                .iter()
                .clone()
                .map(|uniform| rng.sample(uniform))
                .collect(),
            f32: self.f32.iter().map(|uniform| rng.sample(uniform)).collect(),
            f64: self.f64.iter().map(|uniform| rng.sample(uniform)).collect(),
            c64: self.c64.iter().map(|uniform| rng.sample(uniform)).collect(),
            c128: self
                .c128
                .iter()
                .map(|uniform| rng.sample(uniform))
                .collect(),
            d: self.d.iter().map(|uniform| rng.sample(uniform)).collect(),
        }
    }
}

impl XVecBounds {
    pub fn new(x_min: XVec, x_max: XVec) -> Self {
        Self {
            i8: x_min
                .i8
                .iter()
                .zip(x_max.i8.iter())
                .map(|(min, max)| Uniform::from(*min..*max))
                .collect(),
            i16: x_min
                .i16
                .iter()
                .zip(x_max.i16.iter())
                .map(|(min, max)| Uniform::from(*min..*max))
                .collect(),
            i32: x_min
                .i32
                .iter()
                .zip(x_max.i32.iter())
                .map(|(min, max)| Uniform::from(*min..*max))
                .collect(),
            i64: x_min
                .i64
                .iter()
                .zip(x_max.i64.iter())
                .map(|(min, max)| Uniform::from(*min..*max))
                .collect(),
            i128: x_min
                .i128
                .iter()
                .zip(x_max.i128.iter())
                .map(|(min, max)| Uniform::from(*min..*max))
                .collect(),
            i: x_min
                .i
                .iter()
                .zip(x_max.i.iter())
                .map(|(min, max)| Uniform::from(min.clone()..max.clone()))
                .collect(),
            f32: x_min
                .f32
                .iter()
                .zip(x_max.f32.iter())
                .map(|(min, max)| Uniform::from(*min..*max))
                .collect(),
            f64: x_min
                .f64
                .iter()
                .zip(x_max.f64.iter())
                .map(|(min, max)| Uniform::from(*min..*max))
                .collect(),
            c64: x_min
                .c64
                .iter()
                .zip(x_max.c64.iter())
                .map(|(min, max)| {
                    ComplexDistribution::new(
                        Uniform::from(min.re..max.re),
                        Uniform::from(min.im..max.im),
                    )
                })
                .collect(),
            c128: x_min
                .c128
                .iter()
                .zip(x_max.c128.iter())
                .map(|(min, max)| {
                    ComplexDistribution::new(
                        Uniform::from(min.re..max.re),
                        Uniform::from(min.im..max.im),
                    )
                })
                .collect(),
            d: x_min
                .d
                .iter()
                .zip(x_max.d.iter())
                .map(|(min, max)| Uniform::from(*min..*max))
                .collect(),
        }
    }
}
