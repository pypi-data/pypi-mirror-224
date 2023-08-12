use crate::*;


mod min;


// simulated_annealing 模拟退火算法
#[derive(Clone, Copy, Debug, PartialEq, Default)]
#[pyclass(get_all, set_all)]
pub struct GaoSA{
    pub n_iter: usize,
    pub t_max: f64,
    pub t_min: f64,
    pub alpha: f64
}

#[derive(Clone, Copy, Debug, PartialEq, Default)]
#[pyclass(get_all, set_all)]
pub struct LinSA {
    pub n_iter: usize,
    pub t_max: f64,
    pub t_min: f64,
    pub dt : f64
}

#[derive(Clone, Copy, Debug, PartialEq, Default)]
#[pyclass(get_all, set_all)]
pub struct LogSA {
    pub n_iter: usize,
    pub t_max: f64,
    pub t_min: f64,
}