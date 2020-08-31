import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
import numpy as np
import scipy
from scipy.signal import argrelextrema
from scipy.signal import hann
# INGRESO
vocales = np.array(['','a','e','i','o','u'])
plt.ylim(0,6)
plt.yticks(np.arange(6),vocales)
labels = np.array([['Rango Formante 1 - a','Rango Formante 2 - a'],['Rango Formante 1 - e','Rango Formante 2 - e'],['Rango Formante 1 - i','Rango Formante 2 - i'],['Rango Formante 1 - o','Rango Formante 2 - o'],['Rango Formante 1 - u','Rango Formante 2 - u']])
colores = np.array([['red','brown'],['blue','darkblue'],['green','darkgreen'],['orange','darkorange'],['hotpink','deeppink']])
archivos= np.array([['sonido_femenino_a.wav','sonido_masculino_a.wav'],['sonido_femenino_e.wav','sonido_masculino_e.wav'],['sonido_femenino_i.wav','sonido_masculino_i.wav'],['sonido_femenino_o.wav','sonido_masculino_o.wav'],['sonido_femenino_u.wav','sonido_masculino_u.wav']])
formantesFinal = np.empty((len(archivos),2,20))
for it in range(0,len(archivos)):
    formantesPorVocal = np.empty((len(archivos[it]),2,10))
    for it2 in range(0,len(archivos[it])):
        fsonido, sonido = waves.read(archivos[it][it2])
        listaDeTransformadas = list()
        listaDeTransformadasModuladas = list()
        unDecimo = np.around(np.trunc(sonido.shape[0]/10)).astype(int)
        #construir hann window
        window = hann(len(sonido))
        sonido = sonido*window
        #Dividir la señal en 10 rangos
        listaDeRangos = np.array(np.split(sonido,[unDecimo*1,unDecimo*2,unDecimo*3,unDecimo*4,unDecimo*5,unDecimo*6,unDecimo*7,unDecimo*8,unDecimo*9]))
        dt = 1/(fsonido)
        df = (fsonido/unDecimo)/2
        subRango = int(300/df)
        formantes = np.zeros((10,2))
        #Aplicar FFT a cada rango
        for i in range(0,10):
            listaDeTransformadas.append(abs(fourier.rfft(listaDeRangos[i])/len(listaDeRangos[i])))
            listaDeTransformadasModuladas.append(20 * scipy.log10(listaDeTransformadas[i]))
            aux = np.copy(listaDeTransformadasModuladas[i])
            j = 0
            while(j < 2):
                maximo = np.max(aux[int(200/df):int(3000/df)])
                indice = ((list(aux)).index(maximo))
                #print(maximo, indice)
                if(j == 0 or (j > 0 and (indice <= formantes[i][j-1]-subRango or indice >= formantes[i][j-1]+subRango))): 
                    if(formantes[i][j] == 0): formantes[i][j] = indice 
                    else: formantes[i][j+1] = indice
                    j+=1
                aux[indice] = 0
            
        #ordenar formantes            
        for i in range(0,10):
            if(formantes[i][0] > formantes[i][1]):
                auxSwap = formantes[i][0]
                formantes[i][0] = formantes[i][1]
                formantes[i][1] = auxSwap
        #Modular los indices a la frecuencia real
            #formantes = formantes*df
        for i in range(0,10):
            formantesPorVocal[it2][0][i] = formantes[i][0]
            formantesPorVocal[it2][1][i] = formantes[i][1]
    
    #Union de rangos de frecuencia de formantes femeninos y masculinos     
    rangosUnidosF1 = np.concatenate((formantesPorVocal[0][0][0:10],formantesPorVocal[1][0][0:10]))
    rangosUnidosF2 = np.concatenate((formantesPorVocal[0][1][0:10],formantesPorVocal[1][1][0:10]))
    #ordenar
    rangosUnidosF1 = sorted(rangosUnidosF1)
    rangosUnidosF2 = sorted(rangosUnidosF2)
    
    
    arregloPltF1 = np.zeros(len(listaDeTransformadasModuladas[9]))
    arregloPltF2 = np.zeros(len(listaDeTransformadasModuladas[9]))
    
    arregloPltF1[int(rangosUnidosF1[0]):int(rangosUnidosF1[19])] = it+1
    arregloPltF2[int(rangosUnidosF2[0]):int(rangosUnidosF2[19])] = it+1
    plt.plot(fourier.rfftfreq(len(listaDeTransformadas[9]),dt),arregloPltF1,colores[it][0],label=labels[it][0])
    plt.plot(fourier.rfftfreq(len(listaDeTransformadas[9]),dt),arregloPltF2,colores[it][1],label=labels[it][1])
    formantesFinal[it][0][0:20] = rangosUnidosF1[0:20]
    formantesFinal[it][1][0:20] = rangosUnidosF2[0:20]   

plt.legend()   
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Vocal")
plt.title("Rangos para Formantes 1 y 2 de las vocales")
plt.show() 

#Para visualizar las transformadas en el bucle donde se calculan
    #plt.vlines(fourier.rfftfreq(len(listaDeTransformadas[i]),dt),0,listaDeTransformadasModuladas[i])
    #plt.plot((fourier.rfftfreq(len(listaDeTransformadas[i]),dt)),listaDeTransformadasModuladas[i], label=f"FFT de la Entrada {i+1}")
    #plt.legend()
    #plt.xlabel("Frecuencia (Hz)")
    #plt.ylabel("Amplitud (dB)")
    #plt.title("Señal Prueba")
    #plt.show() 