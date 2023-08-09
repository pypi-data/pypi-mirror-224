use super::slog::PyOverflowStrategy;
use crate::utils::reference::RefMutOwner;
use pyo3::{prelude::*, types::PyString};
use slog::*;
use std::sync::{Arc, Mutex};

#[derive(Clone)]
#[pyclass(name = "ThreadSafeLogger")]
pub struct PyThreadSafeLogger {
    pub inner: RefMutOwner<Logger>,
    lock: Arc<Mutex<()>>,
}

#[pymethods]
impl PyThreadSafeLogger {
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

        PyThreadSafeLogger {
            inner: RefMutOwner::new(logger),
            lock: Arc::new(Mutex::new(())),
        }
    }
}

#[pymethods]
impl PyThreadSafeLogger {
    pub fn info(&mut self, s: &PyString) -> PyResult<()> {
        let _guard = self.lock.lock().unwrap();
        Ok(info!(self.inner, "{}", format!("{}", s)))
    }

    pub fn debug(&mut self, s: &PyString) -> PyResult<()> {
        let _guard = self.lock.lock().unwrap();
        Ok(debug!(self.inner, "{}", format!("{}", s)))
    }

    pub fn trace(&mut self, s: &PyString) -> PyResult<()> {
        let _guard = self.lock.lock().unwrap();
        Ok(trace!(self.inner, "{}", format!("{}", s)))
    }

    pub fn error(&mut self, s: &PyString) -> PyResult<()> {
        let _guard = self.lock.lock().unwrap();
        Ok(error!(self.inner, "{}", format!("{}", s)))
    }

    pub fn crit(&mut self, s: &PyString) -> PyResult<()> {
        let _guard = self.lock.lock().unwrap();
        Ok(crit!(self.inner, "{}", format!("{}", s)))
    }
}
