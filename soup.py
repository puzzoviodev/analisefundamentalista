
import re
from bs4 import BeautifulSoup

# Supondo que você já tenha o HTML carregado em `soup`
# Procura todos os blocos que têm título ROE
items = soup.find_all('div', class_='item')

for item in items:
    title_tag = item.find('h3', string=re.compile(r'\bROE\b', re.IGNORECASE))
    if title_tag:
        value_tag = item.find('strong', class_=re.compile(r'value'))
        if value_tag:
            roe_value = value_tag.get_text().strip()
            print("ROE:", roe_value)
            break
==========================invstor10============


import re

# Supondo que você já tenha o HTML carregado em `soup`
# Procura todos os blocos que contêm o nome do indicador
labels = soup.find_all('span', string=re.compile(r'P/ATIVO CIRC LIQ', re.IGNORECASE))

for label in labels:
    # Navega para o próximo <div> com a classe 'value'
    parent = label.find_parent('div')
    if parent:
        value_div = parent.find_next_sibling('div', class_=re.compile(r'value'))
        if value_div:
            value_span = value_div.find('span')
            if value_span:
                value = value_span.get_text().strip()
                print("P/ATIVO CIRC LIQ:", value)
                break

================================== ====genericpath

import re
from bs4 import BeautifulSoup


def buscar_indicador(soup, nome_indicador):
    """
    Busca o valor de um indicador pelo nome, mesmo com variações estruturais no HTML.

    Parâmetros:
        soup (BeautifulSoup): objeto BeautifulSoup com o HTML carregado.
        nome_indicador (str): nome do indicador a ser buscado (ex: 'ROE', 'P/ATIVO CIRC LIQ').

    Retorna:
        str: valor do indicador, ou None se não encontrado.
    """

    # 1. Tenta encontrar o indicador dentro de blocos bem estruturados (como <div class="item">)
    items = soup.find_all('div', class_='item')
    for item in items:
        title_tag = item.find(['h3', 'span'], string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
        if title_tag:
            value_tag = item.find(['strong', 'span'], class_=re.compile(r'value'))
            if value_tag:
                return value_tag.get_text().strip()

    # 2. Se não encontrar, tenta localizar o nome do indicador em qualquer <span>
    labels = soup.find_all('span', string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
    for label in labels:
        parent = label.find_parent('div')
        if parent:
            value_div = parent.find_next_sibling('div', class_=re.compile(r'value'))
            if value_div:
                value_span = value_div.find(['span', 'strong'])
                if value_span:
                    return value_span.get_text().strip()

    # 3. Se ainda não encontrar, retorna None
    return None


=======     como seleniun



import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def buscar_indicador(driver, nome_indicador, id_container='main-2'):
    """
    Usa Selenium + BeautifulSoup para buscar o valor de um indicador pelo nome.

    Parâmetros:
        driver (webdriver): instância do navegador Selenium.
        nome_indicador (str): nome do indicador a ser buscado (ex: 'ROE', 'P/ATIVO CIRC LIQ').
        id_container (str): ID do container principal da página (padrão: 'main-2').

    Retorna:
        str: valor do indicador, ou None se não encontrado.
    """

    # Extrai o HTML da seção principal da página
    html = driver.find_element(By.ID, id_container).get_attribute('innerHTML')
    soup = BeautifulSoup(html, 'html.parser')

    # 1. Tenta encontrar o indicador dentro de blocos bem estruturados
    items = soup.find_all('div', class_='item')
    for item in items:
        title_tag = item.find(['h3', 'span'], string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
        if title_tag:
            value_tag = item.find(['strong', 'span'], class_=re.compile(r'value'))
            if value_tag:
                return value_tag.get_text().strip()

    # 2. Tenta localizar o nome do indicador em qualquer <span>
    labels = soup.find_all('span', string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
    for label in labels:
        parent = label.find_parent('div')
        if parent:
            value_div = parent.find_next_sibling('div', class_=re.compile(r'value'))
            if value_div:
                value_span = value_div.find(['span', 'strong'])
                if value_span:
                    return value_span.get_text().strip()

    return None
=========================    generico  full  ====


import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def buscar_indicador(driver, nome_indicador, id_container='main-2'):
    """
    Usa Selenium + BeautifulSoup para buscar o valor de um indicador pelo nome,
    com suporte a estruturas de blocos, irmãos e tabelas.

    Parâmetros:
        driver (webdriver): instância do navegador Selenium.
        nome_indicador (str): nome do indicador a ser buscado (ex: 'ROE', 'P/ATIVO CIRC LIQ').
        id_container (str): ID do container principal da página (padrão: 'main-2').

    Retorna:
        str: valor do indicador, ou None se não encontrado.
    """

    # Extrai o HTML da seção principal da página
    try:
        html = driver.find_element(By.ID, id_container).get_attribute('innerHTML')
    except:
        html = driver.page_source  # fallback se o ID não existir
    soup = BeautifulSoup(html, 'html.parser')

    # 1. Busca em blocos estruturados (ex: StatusInvest)
    items = soup.find_all('div', class_='item')
    for item in items:
        title_tag = item.find(['h3', 'span'], string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
        if title_tag:
            value_tag = item.find(['strong', 'span'], class_=re.compile(r'value'))
            if value_tag:
                return value_tag.get_text().strip()

    # 2. Busca por elementos irmãos (ex: Investidor10)
    labels = soup.find_all('span', string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
    for label in labels:
        parent = label.find_parent('div')
        if parent:
            value_div = parent.find_next_sibling('div', class_=re.compile(r'value'))
            if value_div:
                value_span = value_div.find(['span', 'strong'])
                if value_span:
                    return value_span.get_text().strip()

    # 3. Busca em tabelas (ex: Fundamentus)
    tds = soup.find_all('td', string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
    for td in tds:
        next_td = td.find_next_sibling('td')
        if next_td:
            return next_td.get_text().strip()

    return None


============================  exemplo teste =======


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get("https://statusinvest.com.br/acoes/ITSA4")

print("ROE:", buscar_indicador(driver, 'ROE'))
print("P/ATIVO CIRC LIQ:", buscar_indicador(driver, 'P/ATIVO CIRC LIQ'))

driver.quit()

