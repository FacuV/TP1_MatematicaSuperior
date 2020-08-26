import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np

# INGRESO
archivo='sonido_masculino_a.wav'
fsonido, sonido = waves.read(archivo)
#  Obtencion de un canal
tamano = np.shape(sonido)
muestras = tamano[0]
m = len(tamano)
canales = 1  # monofónico
if (m>1):  # estéreo
    canales = tamano[1]
# experimento con un canal
if (canales>1):
    canal = 0
    uncanal = sonido[:,canal] 
else:
    uncanal = sonido

ft = fourier.fft(uncanal)
print(type(ft))
#plt.plot(time, data[:, 0], label="Left channel")
plt.plot(ft, label="Left channel")
plt.legend()
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.show() 