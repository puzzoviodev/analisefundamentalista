"""
indicadores_scraper.py

Este módulo é compatível com os sites:
- StatusInvest
- Investidor10
- Fundamentus

Ele utiliza Selenium e BeautifulSoup para extrair indicadores financeiros de páginas web,
tratando diferentes estruturas HTML como:
- Blocos estruturados (ex: <div class="item">)
- Elementos irmãos (ex: <span> seguido de <div class="value">)
- Tabelas (ex: <td> com nome seguido de <td> com valor)

Funções principais:
- buscar_indicador(driver, nome_indicador): busca um indicador específico.
- extrair_todos_indicadores(driver): extrai todos os indicadores da página.
"""

import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# Função para buscar um indicador específico pelo nome
def buscar_indicador(driver, nome_indicador, id_container='main-2', verbose=True):
    try:
        # Tenta extrair apenas o HTML da seção principal da página
        try:
            html = driver.find_element(By.ID, id_container).get_attribute('innerHTML')
            if verbose: print(f"[INFO] HTML extraído de #{id_container}")
        except Exception as e:
            # Se o ID não for encontrado, usa o HTML completo da página
            html = driver.page_source
            if verbose: print(f"[WARN] ID '{id_container}' não encontrado. Usando page_source. ({e})")

        # Cria o objeto BeautifulSoup para fazer o parsing do HTML
        soup = BeautifulSoup(html, 'html.parser')

        # 1. Busca em blocos estruturados (ex: StatusInvest)
        items = soup.find_all('div', class_='item')
        for item in items:
            # Procura o nome do indicador dentro do bloco
            title_tag = item.find(['h3', 'span'], string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
            if title_tag:
                # Procura o valor associado ao indicador
                value_tag = item.find(['strong', 'span'], class_=re.compile(r'value'))
                if value_tag:
                    valor = value_tag.get_text().strip()
                    if verbose: print(f"[OK] '{nome_indicador}' encontrado em bloco estruturado: {valor}")
                    return valor

        # 2. Busca por elementos irmãos (ex: Investidor10)
        labels = soup.find_all('span', string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
        for label in labels:
            parent = label.find_parent('div')
            if parent:
                value_div = parent.find_next_sibling('div', class_=re.compile(r'value'))
                if value_div:
                    value_span = value_div.find(['span', 'strong'])
                    if value_span:
                        valor = value_span.get_text().strip()
                        if verbose: print(f"[OK] '{nome_indicador}' encontrado como irmão: {valor}")
                        return valor

        # 3. Busca em tabelas (ex: Fundamentus)
        tds = soup.find_all('td', string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
        for td in tds:
            next_td = td.find_next_sibling('td')
            if next_td:
                valor = next_td.get_text().strip()
                if verbose: print(f"[OK] '{nome_indicador}' encontrado em tabela: {valor}")
                return valor

        if verbose: print(f"[NOT FOUND] Indicador '{nome_indicador}' não encontrado.")
        return None

    except Exception as e:
        if verbose: print(f"[ERROR] Erro ao buscar '{nome_indicador}': {e}")
        return None

# Função para extrair todos os indicadores da página como um dicionário
def extrair_todos_indicadores(driver, id_container='main-2', verbose=True):
    indicadores = {}

    try:
        # Tenta extrair o HTML da seção principal da página
        try:
            html = driver.find_element(By.ID, id_container).get_attribute('innerHTML')
            if verbose: print(f"[INFO] HTML extraído de #{id_container}")
        except Exception as e:
            html = driver.page_source
            if verbose: print(f"[WARN] ID '{id_container}' não encontrado. Usando page_source. ({e})")

        soup = BeautifulSoup(html, 'html.parser')

        # 1. Blocos estruturados
        items = soup.find_all('div', class_='item')
        for item in items:
            title_tag = item.find(['h3', 'span'], class_=re.compile(r'title|uppercase'))
            value_tag = item.find(['strong', 'span'], class_=re.compile(r'value'))
            if title_tag and value_tag:
                nome = title_tag.get_text().strip()
                valor = value_tag.get_text().strip()
                indicadores[nome] = valor
                if verbose: print(f"[OK] Indicador encontrado: {nome} = {valor}")

        # 2. Elementos irmãos
        labels = soup.find_all('span', string=True)
        for label in labels:
            texto = label.get_text().strip()
            if texto and texto not in indicadores:
                parent = label.find_parent('div')
                if parent:
                    value_div = parent.find_next_sibling('div', class_=re.compile(r'value'))
                    if value_div:
                        value_span = value_div.find(['span', 'strong'])
                        if value_span:
                            valor = value_span.get_text().strip()
                            indicadores[texto] = valor
                            if verbose: print(f"[OK] Indicador irmão: {texto} = {valor}")

        # 3. Tabelas
        tds = soup.find_all('td', string=True)
        for td in tds:
            texto = td.get_text().strip()
            next_td = td.find_next_sibling('td')
            if texto and next_td and texto not in indicadores:
                valor = next_td.get_text().strip()
                indicadores[texto] = valor
                if verbose: print(f"[OK] Indicador em tabela: {texto} = {valor}")

        return indicadores

    except Exception as e:
        if verbose: print(f"[ERROR] Erro ao extrair indicadores: {e}")
        return indicadores

# =========================
# EXEMPLO DE USO
# =========================
if __name__ == "__main__":
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    # Configura o navegador em modo headless (sem abrir janela)
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Acessa a página desejada
    driver.get("https://statusinvest.com.br/acoes/ITSA4")

    # Busca um indicador específico
    roe = buscar_indicador(driver, 'ROE')
    print("ROE:", roe)

    # Extrai todos os indicadores da página
    todos = extrair_todos_indicadores(driver)
    for nome, valor in todos.items():
        print(f"{nome}: {valor}")

    # Encerra o navegador
    driver.quit()
