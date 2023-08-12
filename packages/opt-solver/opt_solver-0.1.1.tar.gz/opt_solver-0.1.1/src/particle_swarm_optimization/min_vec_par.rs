

use super::*;

#[inline]
pub fn min_vec_par<O: PartialOrd + Clone + Sync + Send>(
        pso:&PSO,
        f: impl Fn(XVec) -> O + Sync,
        x_min: XVec,
        x_max: XVec,
    ) -> (O, XVec) {
        let mut rng: ThreadRng = thread_rng();

        let x_bounds = XVecBounds::new(x_min.clone(), x_max.clone());

        let mut v_max = x_max.clone() - x_min.clone();
        v_max.mul_assign_f64(pso.max_v);
        let mut v_min = -v_max.clone();

        struct ParState<O>(pub XVec, pub XVec, pub XVec, pub O);

        unsafe impl<O> Send for ParState<O> {}
        unsafe impl<O> Sync for ParState<O> {}

        let mut status: Vec<ParState<O>> = x_bounds
            .sample_iter(&mut rng)
            .take(pso.n_particles)
            .map(|x| ParState(x.clone(), x.zero(), x.clone(), f(x)))
            .collect();

        let (mut x_best, mut out_best) = {
            let best = status
                .par_iter()
                .min_by(|a, b| a.3.partial_cmp(&b.3).unwrap_or(Equal))
                .expect("n_particles is 0!");
            (best.2.clone(), best.3.clone())
        };

        for _ in 0..pso.n_iters {
            (x_best, out_best) = status
                .par_iter_mut()
                .fold(
                    || (x_best.clone(), out_best.clone()),
                    |(mut x_best, mut out_best), ParState(xt, vt, x_best_pso, out_best_pso)| {
                        *vt = (x_best.clone() - xt.clone()).mul_f64(pso.c1)
                            + (x_best_pso.clone() - xt.clone()).mul_f64(pso.c2);

                        *xt += vt.clone();

                        macro_rules! if_out_off_bounds {
                            ($t:tt) => {
                                xt.$t
                                    .iter_mut()
                                    .zip(vt.$t.iter_mut())
                                    .zip(x_min.$t.iter())
                                    .zip(x_max.$t.iter())
                                    .zip(v_min.$t.iter())
                                    .zip(v_max.$t.iter())
                                    .for_each(
                                        |(
                                            ((((xt_i, vt_i), x_min_i), x_max_i), v_min_i),
                                            v_max_i,
                                        )| {
                                            if *xt_i < *x_min_i {
                                                *xt_i = *x_min_i;
                                                *vt_i = 0;
                                            } else if *xt_i > *x_max_i {
                                                *xt_i = *x_max_i;
                                                *vt_i = 0;
                                            } else if *vt_i < *v_min_i {
                                                *vt_i = *v_min_i;
                                            } else if *xt_i > *v_max_i {
                                                *vt_i = *v_max_i;
                                            }
                                        },
                                    )
                            };
                            ($t:tt,$zero:expr) => {
                                xt.$t
                                    .iter_mut()
                                    .zip(vt.$t.iter_mut())
                                    .zip(x_min.$t.iter())
                                    .zip(x_max.$t.iter())
                                    .zip(v_min.$t.iter())
                                    .zip(v_max.$t.iter())
                                    .for_each(
                                        |(
                                            ((((xt_i, vt_i), x_min_i), x_max_i), v_min_i),
                                            v_max_i,
                                        )| {
                                            if *xt_i < *x_min_i {
                                                *xt_i = *x_min_i;
                                                *vt_i = $zero;
                                            } else if *xt_i > *x_max_i {
                                                *xt_i = *x_max_i;
                                                *vt_i = $zero;
                                            } else if *vt_i < *v_min_i {
                                                *vt_i = *v_min_i;
                                            } else if *xt_i > *v_max_i {
                                                *vt_i = *v_max_i;
                                            }
                                        },
                                    )
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
                            .for_each(
                                |(((((xt_i, vt_i), x_min_i), x_max_i), v_min_i), v_max_i)| {
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
                                },
                            );
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
                        (x_best, out_best)
                    },
                )
                .min_by(|a, b| a.1.partial_cmp(&b.1).expect("failed to compare"))
                .expect("n_particles is 0!");
            status
                .par_iter_mut()
                .for_each(|state| state.1.mul_assign_f64(pso.inertia))
        }

        (out_best, x_best)
    }