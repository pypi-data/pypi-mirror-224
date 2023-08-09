use pyo3::{intern, prelude::*, types::PyString};
use slog::*;
use slog_async::OverflowStrategy;

use crate::implement_type_conversion;
use crate::utils::reference::{RefMutContainer, RefMutOwner};
use std::sync::{Arc, Mutex};

#[pyclass(name = "OverflowStrategy")]
pub struct PyOverflowStrategy(pub OverflowStrategy);

impl From<OverflowStrategy> for PyOverflowStrategy {
    fn from(x: OverflowStrategy) -> Self {
        match x {
            OverflowStrategy::Block => PyOverflowStrategy(OverflowStrategy::Block),
            OverflowStrategy::Drop => PyOverflowStrategy(OverflowStrategy::Drop),
            OverflowStrategy::DropAndReport => PyOverflowStrategy(OverflowStrategy::DropAndReport),
            _ => todo!(),
        }
    }
}

#[pymethods]
impl PyOverflowStrategy {
    pub fn __hash__(&self) -> u64 {
        self.0 as u64
    }

    pub fn __repr__(&self) -> String {
        match self.0 {
            OverflowStrategy::Block => "Block".to_string(),
            OverflowStrategy::Drop => "Drop".to_string(),
            OverflowStrategy::DropAndReport => "DropAndReport".to_string(),
            _ => todo!(),
        }
    }

    #[classattr]
    pub fn Block() -> Self {
        PyOverflowStrategy(OverflowStrategy::Block)
    }

    #[classattr]
    pub fn Drop() -> Self {
        PyOverflowStrategy(OverflowStrategy::Drop)
    }

    #[classattr]
    pub fn DropAndReport() -> Self {
        PyOverflowStrategy(OverflowStrategy::DropAndReport)
    }
}

#[derive(Clone)]
#[pyclass(name = "Logger")]
pub struct PyLogger {
    pub inner: RefMutOwner<Logger>,
}

#[derive(Clone)]
#[pyclass(name = "LoggerRef")]
pub struct PyLoggerRef {
    pub inner: RefMutContainer<Logger>,
    lock: Arc<Mutex<()>>,
    #[pyo3(get, set)]
    pub thread_safe: bool,
}

#[derive(FromPyObject)]
pub enum PyLoggerMut<'p> {
    Owned(PyRefMut<'p, PyLogger>),
    RefMut(PyLoggerRef),
}

implement_type_conversion!(Logger, PyLoggerMut);

#[pymethods]
impl PyLogger {
    #[new]
    pub fn new(chan_size: usize, overflow_strategy: &PyOverflowStrategy) -> Self {
        let decorator = slog_term::TermDecorator::new().build();
        let drain = slog_term::FullFormat::new(decorator).build().fuse();
        let drain = slog_async::Async::new(drain)
            .chan_size(chan_size)
            .overflow_strategy(overflow_strategy.0)
            .build()
            .fuse();

        let logger = slog::Logger::root(drain, o!());

        PyLogger {
            inner: RefMutOwner::new(logger),
        }
    }

    pub fn make_ref(&mut self) -> PyLoggerRef {
        PyLoggerRef {
            inner: RefMutContainer::new(&mut self.inner),
            lock: Arc::new(Mutex::new(())),
            thread_safe: false,
        }
    }

    fn __getattr__(this: PyObject, py: Python, attr: &str) -> PyResult<PyObject> {
        let reference = this.call_method0(py, intern!(py, "make_ref"))?;
        reference.getattr(py, attr)
    }
}

#[pymethods]
impl PyLoggerRef {
    pub fn info(&mut self, s: &PyString) -> PyResult<()> {
        self.inner.map_as_ref(|inner| {
            if self.thread_safe {
                let _lock = self.lock.lock().unwrap();
                info!(inner, "{}", format!("{}", s))
            } else {
                info!(inner, "{}", format!("{}", s))
            }
        })
    }

    pub fn debug(&mut self, s: &PyString) -> PyResult<()> {
        self.inner.map_as_ref(|inner| {
            if self.thread_safe {
                let _lock = self.lock.lock().unwrap();
                debug!(inner, "{}", format!("{}", s))
            } else {
                debug!(inner, "{}", format!("{}", s))
            }
        })
    }

    pub fn trace(&mut self, s: &PyString) -> PyResult<()> {
        self.inner.map_as_ref(|inner| {
            if self.thread_safe {
                let _lock = self.lock.lock().unwrap();
                trace!(inner, "{}", format!("{}", s))
            } else {
                trace!(inner, "{}", format!("{}", s))
            }
        })
    }

    pub fn error(&mut self, s: &PyString) -> PyResult<()> {
        self.inner.map_as_ref(|inner| {
            if self.thread_safe {
                let _lock = self.lock.lock().unwrap();
                error!(inner, "{}", format!("{}", s))
            } else {
                error!(inner, "{}", format!("{}", s))
            }
        })
    }

    pub fn crit(&mut self, s: &PyString) -> PyResult<()> {
        self.inner.map_as_ref(|inner| {
            if self.thread_safe {
                let _lock = self.lock.lock().unwrap();
                crit!(inner, "{}", format!("{}", s))
            } else {
                crit!(inner, "{}", format!("{}", s))
            }
        })
    }
}
