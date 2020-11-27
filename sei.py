from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from time import sleep

url = 'https://sei.sistemas.ro.gov.br/'

sei = Firefox()
sei.get(url)
sleep(1)

cpf = sei.find_elements_by_id("txtUsuario")
cpf[0].send_keys("01606363298")
senha = sei.find_elements_by_id("pwdSenha")
senha[0].send_keys("Nayarb13!")
senha[0].send_keys(Keys.TAB)
orgao = sei.find_element_by_id("selOrgao")
orgao.send_keys("P")
acessar = sei.find_element_by_xpath('//*[@id="sbmLogin"]')
acessar.click()
 


