from numpy import abs, mean
from scipy.fft import fft as spfft, fftfreq as spfftfreq

def fft(t, x):
    N = len(t)
    dt = (t[-1] - t[0]) / N
    x_ft = spfft(x-mean(x))
    freqs = spfftfreq(N, d=dt)[:N//2]
    magn = abs(x_ft)[:N//2] * 2 / N

    return freqs, magn