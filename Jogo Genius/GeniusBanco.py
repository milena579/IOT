import requests
import pyodbc
import time
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import json, time


def InserirBD(sinal):
    server = 'banco de dados'
    database = 'Milena'
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+'; DATABASE='+database+';Trusted_Connection=yes')
    cursor = cnxn.cursor()
    cursor.execute(f"INSERT Pontuacao_Jogadores (Nome, Pontos) values ('{sinal[0]}',{sinal[1]})")
    cursor.commit()
    print("Inserido com sucesso!")


def apresentar(sinal):
    print(f"Nome: {sinal[0]}")
    print(f"Pontos: {sinal[1]}")

proxies = {'https':}

while True:
    url = "url firebase" 
    nome = json.loads(requests.get(url,proxies=proxies).content)['Nome']
    pontos = json.loads(requests.get(url,proxies=proxies).content)['Pontos']
    valores = (nome, pontos)
    print(valores)
    apresentar(valores)
    InserirBD(valores)

    time.sleep(60)