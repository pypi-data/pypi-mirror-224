<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/0zean/fastgoertzel/blob/3914dd4f13ab07226e26ff5ff5cbe83da364789d/docs/_static/dark%20logo.png">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/0zean/fastgoertzel/blob/3914dd4f13ab07226e26ff5ff5cbe83da364789d/docs/_static/light%20logo.png">
    <img alt="Shows a black logo in light color mode and a white one in dark color mode." src="https://github.com/0zean/fastgoertzel/blob/3914dd4f13ab07226e26ff5ff5cbe83da364789d/docs/_static/light%20logo.png">
</picture>

<!-- start here -->

fastgoertzel
============

A Python implementation of the Goertzel algorithm in three different variations built using cython to improve run time on large datasets and/or for multiple frequencies.


## To-Do:

1. Improved speed.
2. Add support for sampling rate.
3. Support for shared memory multiprocessing during fitting

## Installation

You can install using two methods:

Using pip install:
```bash
$ pip install fastgoertzel
```

Using setuptools after cloning repository:
```bash
$ git clone git://github.com/0zean/fastgoertzel.git
$ cd fastgoertzel
$ python setup.py install
```

## Usage
```python
import numpy as np
from fastgoertzel import Goertzel as G


def wave(amp, freq, phase, x):
    return amp * np.sin(2*np.pi * freq * x + phase)


x = np.arange(0, 512)
y = wave(1, 1/128, 0, x)

G = Goertzel(y, 1/128)

amp, phase = G.goertzel()
print(f'Goertzel Amp: {amp:.4f}, phase: {phase:.4f}')

amp, phase = G.goertzelFFT()
print(f'GoertzelFFT Amp: {amp:.4f}, phase: {phase:.4f}')

amp, phase = G.goertzelIIR()
print(f'GoertzelIIR Amp: {amp:.4f}, phase: {phase:.4f}')

# Compared to max amplitude FFT output 
ft = np.fft.fft(y)
FFT = pd.DataFrame()
FFT['amp'] = np.sqrt(ft.real**2 + ft.imag**2) / (len(y) / 2)
FFT['freq'] = np.fft.fftfreq(ft.size, d=1)
FFT['phase'] = np.arctan2(ft.imag, ft.real)

max_ = FFT.iloc[FFT['amp'].idxmax()]
print(f'FFT amp: {max_["amp"]:.4f}, '
        f'phase: {max_["phase"]:.4f}, '
        f'freq: {max_["freq"]:.4f}')
```
