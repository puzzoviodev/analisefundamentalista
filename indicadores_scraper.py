
import re
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

def buscar_indicador(driver, nome_indicador, id_container='main-2', verbose=True):
    """
    Usa Selenium + BeautifulSoup para buscar o valor de um indicador pelo nome,
    com suporte a blocos, irmãos e tabelas. Inclui tratamento de exceções.

    Parâmetros:
        driver (webdriver): instância do navegador Selenium.
        nome_indicador (str): nome do indicador a ser buscado (ex: 'ROE', 'P/ATIVO CIRC LIQ').
        id_container (str): ID do container principal da página (padrão: 'main-2').
        verbose (bool): se True, imprime logs de debug.

    Retorna:
        str ou None: valor do indicador, ou None se não encontrado.
    """
    try:
        try:
            html = driver.find_element(By.ID, id_container).get_attribute('innerHTML')
            if verbose: print(f"[INFO] HTML extraído de #{id_container}")
        except Exception as e:
            html = driver.page_source
            if verbose: print(f"[WARN] ID '{id_container}' não encontrado. Usando page_source. ({e})")

        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all('div', class_='item')
        for item in items:
            title_tag = item.find(['h3', 'span'], string=re.compile(rf'\b{re.escape(nome_indicador)}\b', re.IGNORECASE))
            if title_tag:
                value_tag = item.find(['strong', 'span'], class_=re.compile(r'value'))
                if value_tag:
                    valor = value_tag.get_text().strip()
                    if verbose: print(f"[OK] '{nome_indicador}' encontrado em bloco estruturado: {valor}")
                    return valor

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


def extrair_todos_indicadores(driver, id_container='main-2', verbose=True):
    """
    Extrai todos os indicadores da página e retorna um dicionário com nome: valor.

    Parâmetros:
        driver (webdriver): instância do navegador Selenium.
        id_container (str): ID do container principal da página (padrão: 'main-2').
        verbose (bool): se True, imprime logs de debug.

    Retorna:
        dict: dicionário com indicadores encontrados.
    """
    indicadores = {}

    try:
        try:
            html = driver.find_element(By.ID, id_container).get_attribute('innerHTML')
            if verbose: print(f"[INFO] HTML extraído de #{id_container}")
        except Exception as e:
            html = driver.page_source
            if verbose: print(f"[WARN] ID '{id_container}' não encontrado. Usando page_source. ({e})")

        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all('div', class_='item')
        for item in items:
            title_tag = item.find(['h3', 'span'], class_=re.compile(r'title|uppercase'))
            value_tag = item.find(['strong', 'span'], class_=re.compile(r'value'))
            if title_tag and value_tag:
                nome = title_tag.get_text().strip()
                valor = value_tag.get_text().strip()
                indicadores[nome] = valor
                if verbose: print(f"[OK] Indicador encontrado em bloco: {nome} = {valor}")

        labels = soup.find_all('span')
        for label in labels:
            texto = label.get_text().strip()
            if texto and len(texto) < 50:
                parent = label.find_parent('div')
                if parent:
                    value_div = parent.find_next_sibling('div', class_=re.compile(r'value'))
                    if value_div:
                        value_span = value_div.find(['span', 'strong'])
                        if value_span:
                            valor = value_span.get_text().strip()
                            indicadores[texto] = valor
                            if verbose: print(f"[OK] Indicador encontrado como irmão: {texto} = {valor}")

        tds = soup.find_all('td')
        for i in range(len(tds) - 1):
            nome = tds[i].get_text().strip()
            valor = tds[i + 1].get_text().strip()
            if nome and valor and len(nome) < 50:
                indicadores[nome] = valor
                if verbose: print(f"[OK] Indicador encontrado em tabela: {nome} = {valor}")

        return indicadores

    except Exception as e:
        if verbose: print(f"[ERROR] Erro ao extrair indicadores: {e}")
        return indicadores
