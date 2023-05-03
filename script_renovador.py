from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import time
from time import gmtime, strftime

import os
import getpass

path = os.environ['PATH']
usuario = os.environ['USER']
senha = os.environ['SENHA']

ohrome_options = Options()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://portal.ufsm.br/biblioteca/login.html")

campo_usuario = driver.find_element(By.XPATH, '//*[@id="login"]')
campo_senha = driver.find_element(By.XPATH, '//*[@id="senha"]')

campo_usuario.send_keys(f"{usuario}")
campo_senha.send_keys(f"{senha}")
campo_senha.send_keys(Keys.RETURN)

pagina_renovacao = driver.find_element(By.XPATH, '//*[@id="app_top"]/nav/div/ul/li[4]/a')
pagina_renovacao.click()

data_atual = strftime("%d/%m/%Y", time.localtime())


numero_de_livros = 0
i = 0
try:
    while True:
        data_limite = driver.find_element(By.XPATH, f'//*[@id="emprestimos"]/tbody/tr[{i+1}]/td[6]').text
        numero_de_livros += 1
        i += 1

except NoSuchElementException:
    print(f"Número de livros: {numero_de_livros}")


for i in range(numero_de_livros):

    data_limite = driver.find_element(By.XPATH, f'//*[@id="emprestimos"]/tbody/tr[{i+1}]/td[6]').text

    print(f"Data limite: {data_limite}")
    print(f"Data atual: {data_atual}")

    if data_atual == data_limite:
        botao_renovacao = driver.find_element(By.XPATH, f'//*[@id="emprestimos"]/tbody/tr[{i+1}]/td[1]/button')
        botao_renovacao.click()
        print(f"Livro número {i+1} renovado")

    else:
        print(f"Livro número {i+1} não foi renovado (está antes ou depois do prazo)")

driver.quit()

input("ENTER")
