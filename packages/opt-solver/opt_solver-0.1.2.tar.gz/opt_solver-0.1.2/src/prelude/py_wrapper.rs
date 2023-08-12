use super::*;
use pyo3::types::IntoPyDict;
use pyo3::GILPool;

// #[derive(Clone)]
// pub struct PyWrapperRef<'a>(pub &'a PyAny);
//
// impl PartialEq for PyWrapperRef<'_> {
//     fn eq(&self, other: &Self) -> bool {
//         match self.0.eq(other.0) {
//             Ok(x) => x,
//             _ => false,
//         }
//     }
// }
//
// impl PartialOrd for PyWrapperRef<'_> {
//     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
//         if self == other {
//             Some(Equal)
//         } else {
//             let a = self.0;
//             let b = other.0;
//             match a.lt(b) {
//                 Ok(x) => Some(if x { Less } else { Greater }),
//                 _ => match a.gt(b) {
//                     Ok(x) => Some(if x { Greater } else { Less }),
//                     _ => None,
//                 },
//             }
//         }
//     }
// }
//
// impl<'a> Neg for PyWrapperRef<'a> {
//     type Output = Self;
//
//     fn neg(self) -> Self::Output {
//         let a = self.0;
//         Self(
//             a.call_method0("__neg__")
//                 .expect("There is no __neg__ method")
//         )
//     }
// }

#[derive(Clone)]
pub struct PyWrapperObject<'py>(pub PyObject, pub Python<'py>);

impl PartialEq for PyWrapperObject<'_> {
    fn eq(&self, other: &Self) -> bool {
        match self.0.as_ref(self.1).eq(other.0.as_ref(other.1)) {
            Ok(x) => x,
            _ => false,
        }
    }
}

impl PartialOrd for PyWrapperObject<'_> {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        if self == other {
            Some(Equal)
        } else {
            let a = self.0.as_ref(self.1);
            let b = other.0.as_ref(other.1);
            match a.lt(b) {
                Ok(x) => Some(if x { Less } else { Greater }),
                _ => match a.gt(b) {
                    Ok(x) => Some(if x { Greater } else { Less }),
                    _ => None,
                },
            }
        }
    }
}

impl<'py> Neg for PyWrapperObject<'py> {
    type Output = Self;

    fn neg(self) -> Self::Output {
        let a = self.0.as_ref(self.1);
        Self(
            a.call_method0("__neg__")
                .expect("There is no __neg__ method")
                .into(),
            self.1,
        )
    }
}

//
// pub struct PyWrapperPool(pub PyObject, pub GILPool);
//
// impl PartialEq for PyWrapperPool {
//     fn eq(&self, other: &Self) -> bool {
//         let py = self.1.python();
//
//         match self.0.as_ref(py).eq(other.0.as_ref(py)) {
//             Ok(x) => x,
//             _ => false,
//         }
//     }
// }
//
// impl PartialOrd for PyWrapperPool {
//     fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
//         let py = self.1.python();
//
//         if {
//             match self.0.as_ref(py).eq(other.0.as_ref(py)) {
//                 Ok(x) => x,
//                 _ => false,
//             }
//         } {
//             Some(Equal)
//         } else {
//             let a = self.0.as_ref(py);
//             let b = other.0.as_ref(py);
//             match a.lt(b) {
//                 Ok(x) => Some(if x { Less } else { Greater }),
//                 _ => match a.gt(b) {
//                     Ok(x) => Some(if x { Greater } else { Less }),
//                     _ => None,
//                 },
//             }
//         }
//     }
// }
//
// impl Neg for PyWrapperPool {
//     type Output = Self;
//
//     fn neg(self) -> Self::Output {
//         let py = self.1.python();
//         let a = self.0.as_ref(py);
//         Self(
//             a.call_method0("__neg__")
//                 .expect("There is no __neg__ method")
//                 .into(),
//             self.1,
//         )
//     }
// }
//
// unsafe impl Send for PyWrapperPool {}
// unsafe impl Sync for PyWrapperPool {}
//
// impl Clone  for PyWrapperPool{
//     fn clone(&self) -> Self {
//         let py = self.1.python();
//             Self(self.0.clone(),unsafe{ py.new_pool()})
//     }
// }
