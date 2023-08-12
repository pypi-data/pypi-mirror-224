use super::*;

#[inline]
pub fn min<
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
    pso: &PSO,
    f: impl Fn(X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>) -> O,
    x_min: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
    x_max: X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
) -> (O, X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>) {
    let mut rng: ThreadRng = thread_rng();

    let x_bounds = XBounds::new(x_min.clone(), x_max.clone());

    let mut v_max = x_max.clone() - x_min.clone();
    v_max.mul_assign_f64(pso.max_v);
    let mut v_min = -v_max.clone();

    let mut status: Vec<(
        // xt
        X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
        // vt
        X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
        // x_best_pso
        X<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>,
        // out_best_pso
        O,
    )> = x_bounds
        .sample_iter(&mut rng)
        .take(pso.n_particles)
        .map(|x| {
            (
                x.clone(),
                X::<I8, I16, I32, I64, I128, I, F32, F64, C64, C128, D>::zero(),
                x.clone(),
                f(x),
            )
        })
        .collect();

    let (mut x_best, mut out_best) = {
        let best = status
            .iter()
            .min_by(|a, b| a.3.partial_cmp(&b.3).expect("failed to compare"))
            .expect("n_particles is 0!");
        (best.2.clone(), best.3.clone())
    };

    for _ in 0..pso.n_iters {
        status
            .iter_mut()
            .for_each(|(xt, vt, ref mut x_best_pso, ref mut out_best_pso)| {
                *vt = (x_best.clone() - xt.clone()).mul_f64(pso.c1)
                    + (x_best_pso.clone() - xt.clone()).mul_f64(pso.c2);

                *xt += vt.clone();

                macro_rules! if_out_off_bounds {
                    ($t:tt) => {
                        xt.$t
                            .iter_mut()
                            .zip(vt.$t.iter_mut())
                            .zip(x_min.$t.into_iter())
                            .zip(x_max.$t.into_iter())
                            .zip(v_min.$t.into_iter())
                            .zip(v_max.$t.into_iter())
                            .for_each(|(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                                if *xt_i < x_min_i {
                                    *xt_i = x_min_i;
                                    *vt_i = 0;
                                } else if *xt_i > x_max_i {
                                    *xt_i = x_max_i;
                                    *vt_i = 0;
                                } else if *vt_i < v_min_i {
                                    *vt_i = v_min_i;
                                } else if *xt_i > v_max_i {
                                    *vt_i = v_max_i;
                                }
                            })
                    };
                    ($t:tt,$zero:expr) => {
                        xt.$t
                            .iter_mut()
                            .zip(vt.$t.iter_mut())
                            .zip(x_min.$t.into_iter())
                            .zip(x_max.$t.into_iter())
                            .zip(v_min.$t.into_iter())
                            .zip(v_max.$t.into_iter())
                            .for_each(|(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                                if *xt_i < x_min_i {
                                    *xt_i = x_min_i;
                                    *vt_i = $zero;
                                } else if *xt_i > x_max_i {
                                    *xt_i = x_max_i;
                                    *vt_i = $zero;
                                } else if *vt_i < v_min_i {
                                    *vt_i = v_min_i;
                                } else if *xt_i > v_max_i {
                                    *vt_i = v_max_i;
                                }
                            })
                    };
                }
                if_out_off_bounds!(i8);
                if_out_off_bounds!(i16);
                if_out_off_bounds!(i32);
                if_out_off_bounds!(i64);
                if_out_off_bounds!(i128);
                xt.i.iter_mut()
                    .zip(vt.i.iter_mut())
                    .zip(x_min.i.iter())
                    .zip(x_max.i.iter())
                    .zip(v_min.i.iter())
                    .zip(v_max.i.iter())
                    .for_each(|(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
                        if *xt_i < *x_min_i {
                            *xt_i = x_min_i.clone();
                            *vt_i = BigInt::from(0);
                        } else if *xt_i > *x_max_i {
                            *xt_i = x_max_i.clone();
                            *vt_i = BigInt::from(0);
                        } else if *vt_i < *v_min_i {
                            *vt_i = v_max_i.clone();
                        } else if *xt_i > *v_max_i {
                            *vt_i = v_max_i.clone();
                        }
                    });
                if_out_off_bounds!(f32, 0.0);
                if_out_off_bounds!(f64, 0.0);
                if_out_off_bounds!(d, Decimal::from(0));
                let out_t = f(xt.clone());
                if out_t < *out_best_pso {
                    if out_t < out_best {
                        *out_best_pso = out_t.clone();
                        *x_best_pso = xt.clone();
                        out_best = out_t;
                        x_best = xt.clone();
                    } else {
                        *out_best_pso = out_t;
                        *x_best_pso = xt.clone();
                    }
                }
            });
        status
            .iter_mut()
            .for_each(|state| state.1.mul_assign_f64(pso.inertia))
    }

    (out_best, x_best)
}
