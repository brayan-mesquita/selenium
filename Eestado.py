# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import json
from difflib import SequenceMatcher
from selenium import webdriver
import time
from datetime import date
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

link = 'file:///home/brayan/PROJETOS/SPYDER/pegarlink.html'
navegador = webdriver.Firefox()
navegador.get(link)

url = navegador.page_source
soup = BeautifulSoup(url, 'lxml')
a = soup.find("class" == "container-view")
lista = []
for link in a.find_all('a', href=True):
    lista.append(link['href'])


url = 'https://e-estado.ro.gov.br/'
navegador = webdriver.Firefox()
navegador.get(url)
cpf = navegador.find_element_by_name('Username').send_keys('')
#sleep(1)
#cpf.send_keys('')
#sleep(1)
senha = navegador.find_element_by_name('Password').send_keys('')
#senha.send_keys('')
login = navegador.find_elements_by_xpath('/html/body/div[1]/div/div/div[2]/form/button')
login[0].click()
Keys.ENTER
navegador.get('https://e-estado.ro.gov.br/definir-escopo/2')

departamento = []
descricao = []
incorporacao = []
tomboeestado = []
tomboantigo = []

def buscarTombos():
    for x in lista:
        try:
            navegador.get(x)
            url = navegador.page_source
            soup = BeautifulSoup(url, 'lxml')
            departamento.append(soup.find_all("p", {"class": "m-0"})[3].text[15:])
            descricao.append(soup.find_all("h3")[1].text)
            incorporacao.append(soup.find_all("p", {"class": "m-0 font-mono"})[0].text)
            tomboeestado.append(soup.find_all("td", {"class": "font-mono align-middle"})[0].text)
            tomboantigo.append(soup.find_all("td", {"class": "font-mono align-middle"})[1].text)
            sleep(2)
        except:
            print('erro')

buscarTombos()

df = pd.DataFrame({
    'Departamento': departamento,
    'Descrição': descricao,
    'Incorporação': incorporacao,
    'Tombo-Eestado': tomboeestado,
    'Tombo Antigo': tomboantigo
    })
df.to_csv('eestado.csv')
