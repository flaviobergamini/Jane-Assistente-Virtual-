from firebase import firebase
import RPi.GPIO as GPIO
import time
import os
from gtts import gTTS
import serial

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(37,GPIO.OUT) #BANHEIRO
GPIO.setup(13,GPIO.OUT) #COZINHA
GPIO.setup(29,GPIO.OUT) #SALA
GPIO.setup(33,GPIO.OUT) #JARDIM
GPIO.setup(35,GPIO.OUT) #TOMADA
GPIO.setup(15,GPIO.OUT) #QUARTO
GPIO.setup(31,GPIO.IN)  #SENSOR

#tts=gTTS(text="Oi! Eu sou Dieine, sua assistente virtual", lang='pt')
#tts.save("/tmp/audio.mp3")
#os.system("mpg321 /tmp/audio.mp3")



firebase = firebase.FirebaseApplication('https://janevirtualassistence.firebaseio.com')

auxib=0
auxob=1
auxic=0
auxoc=1
auxij=1
auxoj=0
auxiq=0
auxoq=1
auxis=0
auxos=1

GPIO.output(37,1)
GPIO.output(13,1)
GPIO.output(29,1)
GPIO.output(15,1)

permissao = "true"

while (permissao == "true"):
    boasvindas = firebase.get('/BoasVindas',None)
    boasvindas2 = firebase.get('/BoasVindas2',None)
    
    if boasvindas2 == "true":
        tts=gTTS(text="Oi! Eu sou Dieine, sua assistente virtual, seja bem vindo " + boasvindas, lang='pt')
        tts.save("/tmp/audio.mp3")
        os.system("mpg321 /tmp/audio.mp3")
        
        permissao = "false"
    
    
while True:


    
    #comando = serial.Serial('/dev/ttyACM0',9600)
    banheiro = firebase.get('/Banheiro',None)
    cozinha = firebase.get('/Cozinha',None)
    jardim = firebase.get('/Jardim',None)
    quarto = firebase.get('/Quarto',None)
    sala = firebase.get('/Sala',None)
    tomada = firebase.get('/Tomada',None)

    if sala=="1":
        sala="0"
    else:
        sala="1"

    if cozinha=="1":
        cozinha="0"
    else:
        cozinha="1"

    if quarto=="1":
        quarto="0"
    else:
        quarto="1"

    if banheiro=="1":
        banheiro="0"
    else:
        banheiro="1"
   
    if banheiro=="1":
    
        GPIO.output(37,1)
        if auxib==1:
            tts=gTTS(text="Luz do banheiro desligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxib=0
            auxob=1
    else:
        GPIO.output(37,0)
        if auxob==1:
            tts=gTTS(text="Luz do banheiro ligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxib=1
            auxob=0

            

    if cozinha=="1":
    
        GPIO.output(13,1)
        if auxic==1:
            tts=gTTS(text="Luz da cozinha desligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxic=0
            auxoc=1
    else:
        GPIO.output(13,0)
        if auxoc==1:
            tts=gTTS(text="Luz da cozinha ligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxic=1
            auxoc=0



    if (jardim=="1") or (GPIO.input(31) == 1):
    
        GPIO.output(33,1)
        if auxij==1:
            tts=gTTS(text="Luz do jardim ligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxij=0
            auxoj=1
    else:
        GPIO.output(33,0)
        if auxoj==1:
            tts=gTTS(text="Luz do jardim Desligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxij=1
            auxoj=0



    if quarto=="1":
    
        GPIO.output(15,1)
        if auxiq==1:
            tts=gTTS(text="Luz do quarto desligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxiq=0
            auxoq=1
    else:
        GPIO.output(15,0)
        if auxoq==1:
            tts=gTTS(text="Luz do quarto ligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxiq=1
            auxoq=0



    if sala=="1":
    
        GPIO.output(29,1)
        if auxis==1:
            tts=gTTS(text="Luz da sala desligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxis=0
            auxos=1
    else:
        GPIO.output(29,0)
        if auxos==1:
            tts=gTTS(text="Luz da sala ligada", lang='pt')
            tts.save("/tmp/audio.mp3")
            os.system("mpg321 /tmp/audio.mp3")
            auxis=1
            auxos=0

            

    if tomada=="1":
        GPIO.output(35,1)
        
    else:
        GPIO.output(35,0)

  
        


   
    
    


    
