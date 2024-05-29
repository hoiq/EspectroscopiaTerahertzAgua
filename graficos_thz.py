import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# input data
ref = np.loadtxt('ref.txt')   # reference
ref2 = ref[:, 1]
data = np.loadtxt('spec.txt') # sample
signal = data[:, 1]

# data parameters
dt = ref[1, 0] - ref[0, 0] # É O MEU tstep
n = ref.shape[0]
timeps = np.arange(1, n + 1) * dt
time = timeps * 1e-12

# raw data
plt.figure(1)
plt.plot(timeps, ref2, timeps, signal)
plt.xlabel('Time (ps)')
plt.ylabel('Amplitude(a.u.)')
plt.legend(['ref', 'sample'])

# begin FFT
# number of samples
bits = 14 #teste amostragem FFT, de 10 a 14
nfft = 2**bits
fsample = n / (time[-1] - time[0])

fn = np.arange(nfft//2, nfft)
freqaxis = fsample * (fn - nfft/2) / nfft
freq = freqaxis * 1e-12

# ref
refw = np.fft.fft(ref2, nfft)
refw = np.fft.fftshift(refw)
amp_refwa = refw[fn]
abs_refwa = np.abs(amp_refwa)

# signal
signalw = np.fft.fft(signal, nfft)
signalw = np.fft.fftshift(signalw)
amp_signalw = signalw[fn]
abs_signalw = np.abs(amp_signalw)

# plot the fft of the sample signal
f = [0.01, 5]
plt.figure(2)
plt.semilogy(freq, abs_refwa, 'r', freq, abs_signalw, 'b')
plt.axis([f[0], f[1], 0, max(abs_refwa)])
plt.xlabel('Frequency (THz)')
plt.legend(['ref', 'sample'])

T_thz = np.abs(amp_signalw) / np.abs(abs_refwa) * 100
abs_thz = -np.log10(np.abs(amp_signalw) / np.abs(abs_refwa))
plt.figure(3)
plt.plot(freq, T_thz)
plt.xlim([0.5, 1])
plt.ylim([80, 100])
plt.xlabel('Frequency (THz)')
plt.ylabel('Transmittance (%)')
plt.figure(4)
f1 = [0.5, 1.05]
plt.plot(freq, abs_thz)
plt.axis([f1[0], f1[1], 0, 0.35])
plt.xlabel('Frequency (THz)')
plt.ylabel('Absorbance (a.u.)')


# Encontrar picos apenas no gráfico de absorbância
#peaks, _ = find_peaks(abs_thz, height=0.1)  # Encontrar picos no gráfico de absorbância
#for peak in peaks:
#    plt.text(freq[peak], abs_thz[peak], f'{freq[peak]:.2f}', fontsize=8, ha='center', va='bottom', rotation=90)

# Salvar a figura com alta resolução e transparencia
plt.savefig('absorbancia.png', dpi=300, bbox_inches='tight', transparent=True)

plt.show()