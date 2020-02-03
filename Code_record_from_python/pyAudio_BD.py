# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:14:15 2019

@author: DULCE
"""

import pyaudio
import wave
import time
#EJEMPLO DE GRABADORA DE SONIDO CON "pyaudio".
#IMPORTAMOS LIBRERIAS NECESARIAS

"ESTE PROGRMA GRABA UN AUDIO DE 3s Y LO GUARDA"

#DEFINIMOS PARAMETROS
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=44100
CHUNK=1024
duracion=3
C=4 #total de comandos
G=1 #Grabaciones por comando
Total_g = G*C
P=input("Ingresa el # de persona: ") 
#for grabacion in range (1,Total_g):   
for comando in range(1,C+1):
    for grabacion1 in range (1,G+1):
        name="C" + str(comando) + "_" + "P" + str(P) + "_" + "G" + str(grabacion1)
        archivo= name + ".wav"
        print(name)
        #INICIAMOS "pyaudio"
        audio=pyaudio.PyAudio()
    
        #INICIAMOS GRABACIÓN
        stream=audio.open(format=FORMAT,channels=CHANNELS,
                          rate=RATE, input=True,
                          frames_per_buffer=CHUNK)
        time.sleep(3)
        print("Comienza a hablar cuando veas la leyenda _grabando_ ")
        time.sleep(2)
        print("grabando...")
        frames=[]       
        for i in range(0, int(RATE/CHUNK*duracion)):
            data=stream.read(CHUNK)
            frames.append(data)
        print("grabación terminada")
        print('\n')
    
        #DETENEMOS GRABACIÓN
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        #CREAMOS/GUARDAMOS EL ARCHIVO DE AUDIO
        waveFile = wave.open(archivo, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        