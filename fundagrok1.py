"""
fundamentus_scraper.py

Scraper para Fundamentus.
Extrai indicadores financeiros de https://www.fundamentus.com.br/detalhes.php?papel=ITSA4.
Tenta várias classes de tabelas e tags para lidar com mudanças no HTML.
"""

import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

INDICADOR_ALIASES = {
    'ROE': ['ROE', '? ROE', 'Retorno sobre o Patrimônio'],
    'P/L': ['P/L', '? P/L', 'Preço/Lucro'],
    'P/VP': ['P/VP', '? P/VP', 'Preço/Valor Patrimonial'],
    'DY': ['DY', '? DY', 'Dividend Yield'],
    'Margem Líquida': ['Margem Líquida', '? Margem Líquida', 'Margem Liquida'],
    'Dívida Líquida/EBITDA': ['Dívida Líquida/EBITDA', '? Dívida Líquida/EBITDA', 'Divida Liquida/EBITDA'],
    'ROIC': ['ROIC', '? ROIC', 'Retorno sobre Capital Investido'],
    'Margem Bruta': ['Margem Bruta', '? Margem Bruta', 'Gross Margin'],
    'EV/EBITDA': ['EV/EBITDA', '? EV/EBITDA', 'Enterprise Value/EBITDA'],
    'LPA': ['LPA', '? LPA', 'Lucro por Ação', 'Earnings per Share']
}

def limpar_valor(valor_str):
    if not valor_str or valor_str in ['N/A', '-', '']:
        return None
    valor_str = valor_str.replace('%', '').replace(',', '.').strip()
    try:
        return float(valor_str)
    except ValueError:
        return valor_str

def buscar_indicador(driver, nome_indicador, verbose=True):
    aliases = INDICADOR_ALIASES.get(nome_indicador, [nome_indicador])

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        if verbose: print("[INFO] Página carregada (body detectado).")

        html = driver.page_source
        if verbose: print("[INFO] HTML extraído via page_source")
        soup = BeautifulSoup(html, 'html.parser')

        for alias in aliases:
            pattern = re.compile(rf'{re.escape(alias)}', re.IGNORECASE)
            if verbose: print(f"[INFO] Buscando alias: {alias}")

            for class_name in ['w728', 'data', 'table']:
                tables = soup.find_all('table', class_=class_name)
                if verbose: print(f"[INFO] Encontradas {len(tables)} tabelas com class='{class_name}'")
                for table in tables:
                    tds = table.find_all('td', string=pattern)
                    for td in tds:
                        next_td = td.find_next_sibling('td')
                        if next_td:
                            valor_str = next_td.get_text().strip()
                            valor = limpar_valor(valor_str)
                            if verbose: print(f"[OK] '{alias}' encontrado em tabela class='{class_name}': {valor}")
                            return valor

            tds = soup.find_all('td', string=pattern)
            if verbose: print(f"[INFO] Encontrados {len(tds)} tds com texto correspondente")
            for td in tds:
                next_td = td.find_next_sibling('td')
                if next_td:
                    valor_str = next_td.get_text().strip()
                    valor = limpar_valor(valor_str)
                    if verbose: print(f"[OK] '{alias}' encontrado em tabela: {valor}")
                    return valor

        if verbose: print(f"[NOT FOUND] Indicador '{nome_indicador}' não encontrado.")
        return None

    except Exception as e:
        if verbose: print(f"[ERROR] Erro ao buscar '{nome_indicador}': {str(e)}")
        return None

def extrair_todos_indicadores(driver, verbose=True):
    indicadores = {}

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        if verbose: print("[INFO] Página carregada (body detectado).")

        html = driver.page_source
        if verbose: print("[INFO] HTML extraído via page_source")
        soup = BeautifulSoup(html, 'html.parser')

        for class_name in ['w728', 'data', 'table']:
            tables = soup.find_all('table', class_=class_name)
            if verbose: print(f"[INFO] Encontradas {len(tables)} tabelas com class='{class_name}'")
            for table in tables:
                tds = table.find_all('td', string=True)
                for td in tds:
                    texto = td.get_text().strip()
                    next_td = td.find_next_sibling('td')
                    if texto and next_td and texto not in indicadores:
                        valor_str = next_td.get_text().strip()
                        valor = limpar_valor(valor_str)
                        indicadores[texto] = valor
                        if verbose: print(f"[OK] Indicador em tabela: {texto} = {valor}")

        tds = soup.find_all('td', string=True)
        for td in tds:
            texto = td.get_text().strip()
            next_td = td.find_next_sibling('td')
            if texto and next_td and texto not in indicadores:
                valor_str = next_td.get_text().strip()
                valor = limpar_valor(valor_str)
                indicadores[texto] = valor
                if verbose: print(f"[OK] Indicador em tabela: {texto} = {valor}")

        return indicadores

    except Exception as e:
        if verbose: print(f"[ERROR] Erro ao extrair indicadores: {str(e)}")
        return indicadores

if __name__ == "__main__":
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
        driver.get("https://www.fundamentus.com.br/detalhes.php?papel=ITSA4")
        # Teste indicadores específicos
        indicadores = ['ROE', 'P/L', 'P/VP', 'DY', 'Margem Líquida', 'Dívida Líquida/EBITDA', 'ROIC', 'Margem Bruta', 'EV/EBITDA', 'LPA']
        for indicador in indicadores:
            valor = buscar_indicador(driver, indicador)
            print(f"{indicador}: {valor}")
        # Teste todos os indicadores
        todos = extrair_todos_indicadores(driver)
        for nome, valor in todos.items():
            print(f"{nome}: {valor}")