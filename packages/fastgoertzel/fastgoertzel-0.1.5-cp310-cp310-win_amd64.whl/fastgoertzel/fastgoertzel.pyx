import numpy as np
cimport numpy as np
from scipy.signal import lfilter

cdef class Goertzel:
    """Implements three different Goertzel algorithm methods:
    - Standard Goertzel Algorithm `.goertzel()`
    - Goertzel as the k-th coefficient of an N-point FFT `.goertzelFFT()`
    - Goertzel as an IIR filter `.goertzelIIR()`
    
    Parameters
    ----------
    x : _numpy.ndarray_,
        ndarray of signal to process.
    f : _float_,
        Frequency.
    ----------
    """
    cdef double[:] _x
    cdef public int N
    cdef public int k

    def __init__(self, np.ndarray[np.double_t, ndim=1] x, double f):
        self._x = x
        self.N = len(self._x)
        self.k = int(f * self.N)


    property x:
        def __get__(self):
            return self._x

    cpdef goertzel(self):
        """Standard implementation of Goertzel algorithm

        Returns
        ----------
        amp : _float_
            Amplitude at the given frequency
        phase : _float_
            Phase angle at the given frequency
        """
        cdef int n
        cdef double w = 2 * np.pi * self.k / self.N
        cdef double cw = np.cos(w)
        cdef double c = 2 * cw
        cdef double sw = np.sin(w)
        cdef double z1 = 0, z2 = 0
        cdef double z0

        for n in range(self.N):
            z0 = self._x[n] + c * z1 - z2
            z2 = z1
            z1 = z0

        cdef double ip = cw * z1 - z2
        cdef double qp = sw * z1

        cdef double amp = np.sqrt(ip**2 + qp**2) / (self.N / 2)
        cdef double phase = np.arctan2(qp, ip)
        return amp, phase

    cpdef goertzelFFT(self):
        """Goertzel as the k-th coefficient of an N-point FFT

        Returns
        ----------
        amp : _float_
            Amplitude at the given frequency
        phase : _float_
            Phase angle at the given frequency
        """
        cdef np.ndarray[complex, ndim=1] y = np.fft.fft(self._x)
        cdef double ip = y[self.k].real
        cdef double qp = y[self.k].imag

        cdef double amp = np.sqrt(ip**2 + qp**2) / (self.N / 2)
        cdef double phase = np.arctan2(qp, ip)
        return amp, phase

    cpdef goertzelIIR(self):
        """Goertzel as an IIR filter

        Returns
        ----------
        amp : _float_
            Amplitude at the given frequency
        phase : _float_
            Phase angle at the given frequency
        """
        cdef int i
        cdef double complex W = np.exp(1j * 2 * np.pi * self.k / self.N)
        cdef double complex c = 2 * np.cos(2 * np.pi * self.k / self.N)
        cdef double complex[3] b = [W, -1, 0]
        cdef double complex[3] a = [1, -c, 1]
        cdef np.ndarray[np.complex_t, ndim=1] y = lfilter(b, a, self._x)
        cdef double complex ip = np.real(y[-1])
        cdef double complex qp = np.imag(y[-1])

        cdef double amp = np.sqrt(ip**2 + qp**2) / (self.N / 2)
        cdef double phase = np.arctan2(qp, ip)
        return amp, phase
