from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://e-estado.ro.gov.br/'
navegador = Firefox()
navegador.get(url)
sleep(2)


#FAZER UM FOR EM UMA LISTA DE ELEMENTOS

#a = navegador.find_elements_by_tag_name('a')
#for link in a:
#   print(link.text)




cpf = navegador.find_element_by_name('Username')
cpf.send_keys('016.063.632-98')
sleep(1)
senha = navegador.find_element_by_name('Password')
senha.send_keys('Nayarb13!')
login = navegador.find_elements_by_xpath('/html/body/div[1]/div/div/div[2]/form/button')
login[0].click()
sleep(1) 
Keys.ENTER
eestado = navegador.get(navegador.current_url)

