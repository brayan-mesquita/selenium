from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://meuacesso.sistemas.ro.gov.br//'
navegador = Firefox()
navegador.get(url)
sleep(1)

class Sistemas():
    def __init__(self, cpf, senha):
        self.cpf = cpf
        self.senha = senha

    def login_sauron(self):
        cpf = navegador.find_element_by_name('Username')
        cpf.send_keys(self.cpf)
        sleep(1)
        senha = navegador.find_element_by_name('Password')
        senha.send_keys(self.senha)
        login = navegador.find_elements_by_xpath('/html/body/div[1]/div/div/div[2]/form/button')
        login[0].click()
        sleep(1) 
        Keys.ENTER


buscar = Sistemas('xx', 'xx!')
buscar.login_sauron()

# bens = navegador.get('https://e-estado.ro.gov.br/patrimonio/bens')
# buscar = navegador.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div/div/div/form/div/input')

#criar função com FOR para percorrer os atributos
buscar[0].send_keys('60792' + Keys.ENTER)