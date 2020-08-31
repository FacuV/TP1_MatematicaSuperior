import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
import scipy.fftpack as fourier
import matplotlib.pyplot as plt
# read audio samples
archivo='sonido_femenino_e.wav'
fsonido, sonido = read(archivo)
Decimo = len(sonido)//10
# apply a Hanning window
window = hann(Decimo)
sonido = sonido[0:Decimo] * window
# fft
mags = abs(fourier.rfft(sonido[0:Decimo])/len(sonido[0:Decimo]))
frec = fourier.rfftfreq(Decimo,1/fsonido)
# convert to dB
mags = 20 * scipy.log10(mags)
# plot
plt.plot(frec,mags,label="hola")
# label the axes
plt.ylabel("Magnitude (dB)")
plt.xlabel("Frequency Bin")
# set the title
plt.title("FFT Modulada Prueba")
plt.show()
