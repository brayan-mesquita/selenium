from selenium.webdriver import Firefox
from time import sleep

url = 'https://www.rondoniagora.com/'


navegador = Firefox()

navegador.get(url)

sleep(1)



links = navegador.find_elements_by_tag_name('li')

print()




 


