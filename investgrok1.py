"""
investidor10_scraper.py

Scraper para Investidor10.
Extrai indicadores financeiros de https://investidor10.com.br/acoes/ITSA4/.
Tenta várias classes e tags para lidar com mudanças no HTML.
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
    'ROE': ['ROE', 'Retorno sobre o Patrimônio', 'Return on Equity'],
    'P/L': ['P/L', 'Preço/Lucro', 'P/E', 'Preco/Lucro'],
    'P/VP': ['P/VP', 'Preço/Valor Patrimonial', 'Price/Book'],
    'DY': ['DY', 'Dividend Yield', 'Rendimento de Dividendos'],
    'Margem Líquida': ['Margem Líquida', 'Margem Liquida', 'Net Margin'],
    'Dívida Líquida/EBITDA': ['Dívida Líquida/EBITDA', 'Divida Liquida/EBITDA', 'Debt/EBITDA'],
    'ROIC': ['ROIC', 'Retorno sobre Capital Investido', 'Return on Invested Capital'],
    'Margem Bruta': ['Margem Bruta', 'Gross Margin', 'Margem bruta'],
    'EV/EBITDA': ['EV/EBITDA', 'Enterprise Value/EBITDA', 'EV/Ebitda'],
    'LPA': ['LPA', 'Lucro por Ação', 'Lucro Por Acao', 'Earnings per Share']
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

            for class_name in ['indicator-item', 'item', 'card', 'data']:
                items = soup.find_all('div', class_=class_name)
                if verbose: print(f"[INFO] Encontrados {len(items)} divs com class='{class_name}'")
                for item in items:
                    title_tag = item.find(['span', 'h3', 'div'], string=pattern)
                    if title_tag:
                        value_tag = item.find(['span', 'strong', 'div'], class_=re.compile(r'value|amount|data'))
                        if value_tag:
                            valor_str = value_tag.get_text().strip()
                            valor = limpar_valor(valor_str)
                            if verbose: print(f"[OK] '{alias}' encontrado em div class='{class_name}': {valor}")
                            return valor

            labels = soup.find_all(['span', 'div'], string=pattern)
            if verbose: print(f"[INFO] Encontrados {len(labels)} spans/divs com texto correspondente")
            for label in labels:
                parent = label.find_parent('div')
                if parent:
                    value_tag = parent.find_next_sibling('div') or parent.find(['span', 'strong'], class_=re.compile(r'value|amount|data'))
                    if value_tag:
                        valor_str = value_tag.get_text().strip()
                        valor = limpar_valor(valor_str)
                        if verbose: print(f"[OK] '{alias}' encontrado como irmão: {valor}")
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

        for class_name in ['indicator-item', 'item', 'card', 'data']:
            items = soup.find_all('div', class_=class_name)
            if verbose: print(f"[INFO] Encontrados {len(items)} divs com class='{class_name}'")
            for item in items:
                title_tag = item.find(['span', 'h3', 'div'])
                value_tag = item.find(['span', 'strong', 'div'], class_=re.compile(r'value|amount|data'))
                if title_tag and value_tag:
                    nome = title_tag.get_text().strip()
                    valor_str = value_tag.get_text().strip()
                    valor = limpar_valor(valor_str)
                    if nome and nome not in indicadores:
                        indicadores[nome] = valor
                        if verbose: print(f"[OK] Indicador encontrado: {nome} = {valor}")

        labels = soup.find_all(['span', 'div'], string=True)
        for label in labels:
            texto = label.get_text().strip()
            if texto and texto not in indicadores:
                parent = label.find_parent('div')
                if parent:
                    value_tag = parent.find_next_sibling('div') or parent.find(['span', 'strong'], class_=re.compile(r'value|amount|data'))
                    if value_tag:
                        valor_str = value_tag.get_text().strip()
                        valor = limpar_valor(valor_str)
                        indicadores[texto] = valor
                        if verbose: print(f"[OK] Indicador irmão: {texto} = {valor}")

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
        driver.get("https://investidor10.com.br/acoes/ITSA4/")
        # Teste indicadores específicos
        indicadores = ['ROE', 'P/L', 'P/VP', 'DY', 'Margem Líquida', 'Dívida Líquida/EBITDA', 'ROIC', 'Margem Bruta', 'EV/EBITDA', 'LPA']
        for indicador in indicadores:
            valor = buscar_indicador(driver, indicador)
            print(f"{indicador}: {valor}")
        # Teste todos os indicadores
        todos = extrair_todos_indicadores(driver)
        for nome, valor in todos.items():
            print(f"{nome}: {valor}")