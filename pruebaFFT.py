import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np

# INGRESO
archivo='sonido_femenino_u.wav'
fsonido, sonido = waves.read(archivo)
Time = np.linspace(0, len(sonido) / fsonido, num=len(sonido))
dt1 = 1/(fsonido)
listaDeTransformadas = list()
listaDeTransformadasRecortadasModuladas = list()
#Dividir en 10 rangos el sonido obtenido
unDecimo = np.around(np.trunc(sonido.shape[0]/10)).astype(int)
listaDeRangos = np.array(np.split(sonido,[
    unDecimo*1,
    unDecimo*2,
    unDecimo*3,
    unDecimo*4,
    unDecimo*5,
    unDecimo*6,
    unDecimo*7,
    unDecimo*8,
    unDecimo*9
]))
print(type(listaDeRangos))
for i in range(0,10):
    listaDeTransformadas.append(fourier.fft(listaDeRangos[i])/(len(listaDeRangos[i])))
    listaDeTransformadasRecortadasModuladas.append(abs(listaDeTransformadas[i][0:len(listaDeTransformadas[i])//2]))
    if(i==0):plt.plot((fourier.fftfreq(len(listaDeTransformadas[i]),dt1))[0:len(listaDeTransformadas[i])//2],listaDeTransformadasRecortadasModuladas[i], label="FFT de la Entrada")
#plt.vlines(ftFrec, 0, abs((ft[0:len(ft)])))
plt.legend()
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.title("FFT Prueba")
plt.show() 