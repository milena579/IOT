from machine import Pin
import time
import random

import urequests
import ujson
import network

#Credenciais do WIFI
nome = ""
senha = ""

# Endereço do firebase
FIREBASE_URL = "" 
SECRET_KEY = ""


#FUNÇÕES DO WIFI
def conectarWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando no WiFi...")
        wlan.connect(nome, senha)
        while not wlan.isconnected():
            pass
    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))


def enviarFire(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SECRET_KEY
    }
    
    url = FIREBASE_URL + "/Milena.json"  # Coloque o seu nome

    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()


#PROGRAMAÇÃO DO JOGO
    
# CONFIGURAÇÃO DOS Leds
led_azul = Pin(15, Pin.OUT)
led_vermelho = Pin(2, Pin.OUT)
led_amarelo = Pin(4, Pin.OUT)
led_verde = Pin(5, Pin.OUT)

# CONFIGURAÇÃO DOS BOTÕES
btn_azul = Pin(13, Pin.IN)
btn_vermelho = Pin(12, Pin.IN)
btn_amarelo = Pin(14, Pin.IN)
btn_verde = Pin(27, Pin.IN)

#BUZZER
buzzer = Pin(26,Pin.OUT)

def acender_led(led):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)

def Leds():
    while btn_azul.value() == 0 and btn_vermelho.value() == 0 and btn_amarelo.value() == 0 and btn_verde.value() == 0:
        a = 0
        
    if btn_azul.value() == 1:
        acender_led(led_azul)
        led = led_azul
        return led
         
    if btn_vermelho.value() == 1:
        acender_led(led_vermelho)
        led = led_vermelho
        return led
        
        
    if btn_amarelo.value() == 1:
        acender_led(led_amarelo)
        led = led_amarelo
        return led
        
    if btn_verde.value() == 1:
        acender_led(led_verde)
        led = led_verde
        return led
           
def random_Leds():
    random_led = random.choice([led_azul, led_vermelho, led_amarelo, led_verde])
    
    return random_led
 

def ligar_buzzer():
    buzzer.on()
    time.sleep(0.5)
    buzzer.off()
    
    buzzer.on()
    time.sleep(0.5)
    buzzer.off()
    
    buzzer.on()
    time.sleep(1)
    buzzer.off()

def game_over():
  ligar_buzzer()
  for i in range(3):
    led_azul.on()
    led_vermelho.on()
    led_amarelo.on()
    led_verde.on()
    
    time.sleep(0.5)
    
    led_azul.off()
    led_vermelho.off()
    led_amarelo.off()
    led_verde.off()
    
    time.sleep(0.5)
    
conectarWifi()

#GENIUS 
cont = 0
acabou = False
leds_sort = []

nome = input("Insira o nome do jogador: ")
while True:
    cont = cont  + 1
    respostas = []
    
    print(f"ROUND {cont}")
    time.sleep(2)
    
    led_sort = random_Leds()
    leds_sort.append(led_sort)
        
    for j in range(cont):
        acender_led(leds_sort[j])
        #print(leds_sort[j])
        
    for j in range(cont):
        resposta = Leds()
        
        if leds_sort[j] !=  resposta:
            acabou = True
            print("GAME OVER")
            game_over()
            break
        
        
        print(f"Resposta: {resposta}")
    
    time.sleep(1)
                            
    if(acabou):
        print(f"PONTOS: {cont-1}")
        break
                
    informacao = {
        "Nome": nome,
        "Pontos": cont               
    }
            
enviarFire(informacao)
    

        
        