from selenium.webdriver import Firefox
from time import sleep

url = 'https://www.rondoniagora.com/'


navegador = Firefox()

navegador.get(url)

sleep(1)



a = navegador.find_elements_by_tag_name('a')

for link in a:
    print(link.text)



# lista = navegador.find_element_by_tag_name('li') #primeiro elements
# listas = navegador.find_elements_by_tag_name('li') # todos elementos
# print(lista.tex)

# print(listas[1].find_element_by_tag_name('a').text)


# print(lista.text)
# print(listas[1].text)
# print(len(listas))



 


