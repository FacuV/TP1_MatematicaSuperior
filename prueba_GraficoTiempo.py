import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np

# INGRESO
archivo='sonido_femenino_a.wav'
fsonido, sonido = waves.read(archivo)
#Time = np.linspace(0, len(sonido) / fsonido, num=len(sonido))
unDecimo = len(sonido)//10
listaDeRangos = list()
#Dividir en 10 rangos el sonido obtenido
for i in range(0,9):
    listaDeRangos.append(sonido[i*unDecimo:(i+1)*unDecimo].copy())
#Para añadir la ultima seccion del archivo de sonido    
listaDeRangos.append(sonido[9*unDecimo:(10*unDecimo)+5].copy())
for i in range(0,10):
    aux = 0
    if(i==9):aux+=5
    Time = np.linspace((unDecimo/fsonido)*i, ((unDecimo+aux)/fsonido)*(i+1), num=unDecimo+aux)
    plt.plot(Time,listaDeRangos[i], label=f"Señal de Entrada parte {i+1}")

plt.legend()
plt.xlabel("Tiempo (S)")
plt.ylabel("Amplitud")
plt.title("Señal Prueba")
plt.show() 