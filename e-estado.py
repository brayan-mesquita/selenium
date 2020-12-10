from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://e-estado.ro.gov.br/'
navegador = Firefox()
navegador.get(url)
sleep(1)

class Acesso():
    def __init__(self, cpf, senha, navegador):
        self.cpf = cpf
        self.senha = senha
        self.navegador = navegador

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

    def pesquisar(self, tombo):
        self.navegador.get('https://e-estado.ro.gov.br/patrimonio/bens')
        pesquisa = self.navegador.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div/div/div/form/div/input')
        pesquisa[0].send_keys(str(tombo) + Keys.ENTER)



acesso = Acesso('xxx', 'xxxx!', navegador)
acesso.login_sauron()
acesso.pesquisar('4983')
acesso.pesquisar('4984')


# bens = navegador.get('https://e-estado.ro.gov.br/patrimonio/bens')
# buscar = navegador.find_elements_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/div/div/div/form/div/input')

#criar função com FOR para percorrer os atributos
