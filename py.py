from selenium.webdriver import Firefox
from time import sleep

url = 'https://www.rondoniagora.com/'


navegador = Firefox()

navegador.get(url)

sleep(1)


#FAZER UM FOR EM UMA LISTA DE ELEMENTOS

#a = navegador.find_elements_by_tag_name('a')
#for link in a:
#   print(link.text)



#ENCONTRANDO ELEMENTOS HTML

#lista = navegador.find_element_by_tag_name('li') #primeiro elements
listas = navegador.find_elements_by_tag_name('li') # todos elementos
# print(lista.text)

#DENTRO DA LISTA DE LI PROCURANDO A PRIMEIRA ANCORA
print(listas[2].find_element_by_tag_name('a').text)

#PERCORRENDO TEXTOS DE UMA LISTA
for texto in listas:
    print(texto.text)

