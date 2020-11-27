from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui, time
from time import sleep


opcao= pyautogui.confirm(text='Ponto Eletrônico para Servidor Ocupado', title='Portal do Servidor', buttons=['Marcar Entrada/Saida', 'Cancelar'])
print(opcao)
if opcao == "Marcar Entrada/Saida":
    url = 'https://portaldoservidor.sistemas.ro.gov.br/'
    ponto = Firefox()
    ponto.get(url)
    sleep(2)
    acesarportalservidor = ponto.find_element_by_xpath('/html/body/div/div/main/div[3]/a')
    acesarportalservidor.click()
    sleep(1)
    cpf = ponto.find_element_by_name('Username')
    cpf.send_keys('016.063.632-98')
    sleep(0.5)
    senha = ponto.find_element_by_name('Password')
    senha.send_keys('Nayarb13!')
    login = ponto.find_elements_by_xpath('/html/body/div[1]/div/div/div[2]/form/button')
    login[0].click()
    ponto = ponto.get('https://portaldoservidor.sistemas.ro.gov.br/RegistroEletronico/Listar')
