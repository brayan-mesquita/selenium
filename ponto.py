from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://portaldoservidor.sistemas.ro.gov.br/'
ponto = Firefox()
ponto.get(url)
sleep(0.5)

acesarportalservidor = ponto.find_element_by_xpath('/html/body/div/div/main/div[3]/a')
acesarportalservidor.click()
sleep(1)
cpf = ponto.find_element_by_name('Username').send_keys('xxx')
sleep(0.5)
senha = ponto.find_element_by_name('Password').send_keys('xxx')
login = ponto.find_elements_by_xpath('/html/body/div[1]/div/div/div[2]/form/button')
login[0].click()
ponto.get('https://portaldoservidor.sistemas.ro.gov.br/RegistroEletronico/Listar')
ponto.find_element_by_id("criarRegistros").click()
sleep(0.5)
ponto.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[1]').click()
sleep(0.5)
#ponto.find_element_by_xpath('/html/body/div[2]/header/nav/div[2]/ul[2]/li[2]/div/ul/li/a').click()

ponto.quit()
