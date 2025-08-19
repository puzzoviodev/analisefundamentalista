"""
statusinvest_scraper.py

Scraper para StatusInvest.
Extrai indicadores financeiros de https://statusinvest.com.br/acoes/ITSA4.
Inclui indicadores solicitados e adicionais comuns do site.
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
    'Giro Ativos': ['Giro Ativos', 'Giro dos Ativos', 'Asset Turnover'],
    'Dív. Líquida/PL': ['Dív. Líquida/PL', 'Divida Liquida/PL', 'Dívida Líquida/Patrimônio Líquido', 'Net Debt/Equity'],
    'Dív. Líquida/EBITDA': ['Dív. Líquida/EBITDA', 'Divida Liquida/EBITDA', 'Dívida Líquida/EBITDA', 'Net Debt/EBITDA'],
    'Dív. Líquida/EBIT': ['Dív. Líquida/EBIT', 'Divida Liquida/EBIT', 'Dívida Líquida/EBIT', 'Net Debt/EBIT'],
    'PL/Ativos': ['PL/Ativos', 'Patrimônio Líquido/Ativos', 'Equity/Assets'],
    'Passivos/Ativos': ['Passivos/Ativos', 'Passivo/Ativo', 'Liabilities/Assets'],
    'Liq. Corrente': ['Liq. Corrente', 'Liquidez Corrente', 'Current Ratio'],
    'P/L': ['P/L', 'Preço/Lucro', 'P/E', 'Preco/Lucro'],
    'PEG Ratio': ['PEG Ratio', 'PEG', 'Price/Earnings to Growth'],
    'P/VP': ['P/VP', 'Preço/Valor Patrimonial', 'Price/Book', 'P/VPA'],
    'EV/EBITDA': ['EV/EBITDA', 'Enterprise Value/EBITDA', 'EV/Ebitda'],
    'EV/EBIT': ['EV/EBIT', 'Enterprise Value/EBIT', 'EV/Ebit'],
    'P/EBITDA': ['P/EBITDA', 'Preço/EBITDA', 'Price/EBITDA'],
    'P/EBIT': ['P/EBIT', 'Preço/EBIT', 'Price/EBIT'],
    'VPA': ['VPA', 'Valor Patrimonial por Ação', 'Book Value per Share'],
    'P/Ativo': ['P/Ativo', 'Preço/Ativo', 'Price/Assets'],
    'LPA': ['LPA', 'Lucro por Ação', 'Lucro Por Acao', 'Earnings per Share'],
    'P/SR': ['P/SR', 'Preço/Sales', 'Price/Sales', 'P/Receita'],
    'P/Ativo Circ. Líq.': ['P/Ativo Circ. Líq.', 'Preço/Ativo Circulante Líquido', 'Price/Net Current Assets'],
    'Disponibilidade': ['Disponibilidade', 'Caixa e Equivalentes', 'Cash and Equivalents'],
    'Patrimônio Líquido': ['Patrimônio Líquido', 'Patrimonio Liquido', 'Equity', 'Patrimônio'],
    'Dívida Bruta': ['Dívida Bruta', 'Divida Bruta', 'Gross Debt'],
    'Dívida Líquida': ['Dívida Líquida', 'Divida Liquida', 'Net Debt'],
    'Ativos': ['Ativos', 'Ativo Total', 'Total Assets'],
    'Ativo Circulante': ['Ativo Circulante', 'Ativos Circulantes', 'Current Assets'],
    'Liquidez Média Diária': ['Liquidez Média Diária', 'Liquidez Media Diaria', 'Average Daily Liquidity'],
    # Indicadores adicionais comuns no StatusInvest
    'ROE': ['ROE', 'Retorno sobre o Patrimônio', 'Return on Equity', 'ROE format_quote'],
    'ROIC': ['ROIC', 'Retorno sobre Capital Investido', 'Return on Invested Capital'],
    'Margem Bruta': ['Margem Bruta', 'Gross Margin', 'Margem bruta'],
    'Margem Líquida': ['Margem Líquida', 'Margem Liquida', 'Net Margin'],
    'Margem EBITDA': ['Margem EBITDA', 'Ebitda Margin', 'Margem Ebitda'],
    'Cresc. Receita 5 Anos': ['Cresc. Receita 5 Anos', 'Crescimento Receita 5 Anos', 'Revenue Growth 5 Years'],
    'Dívida Bruta/EBITDA': ['Dívida Bruta/EBITDA', 'Divida Bruta/EBITDA', 'Gross Debt/EBITDA']
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
        driver.get("https://statusinvest.com.br/acoes/ITSA4")
        # Teste indicadores solicitados
        indicadores = [
            'Giro Ativos', 'Dív. Líquida/PL', 'Dív. Líquida/EBITDA', 'Dív. Líquida/EBIT',
            'PL/Ativos', 'Passivos/Ativos', 'Liq. Corrente', 'P/L', 'PEG Ratio', 'P/VP',
            'EV/EBITDA', 'EV/EBIT', 'P/EBITDA', 'P/EBIT', 'VPA', 'P/Ativo', 'LPA',
            'P/SR', 'P/Ativo Circ. Líq.', 'Disponibilidade', 'Patrimônio Líquido',
            'Dívida Bruta', 'Dívida Líquida', 'Ativos', 'Ativo Circulante',
            'Liquidez Média Diária','ROE'
        ]
        for indicador in indicadores:
            valor = buscar_indicador(driver, indicador)
            print(f"{indicador}: {valor}")
        # Teste todos os indicadores (inclui adicionais)
        todos = extrair_todos_indicadores(driver)
        print("\nTodos os indicadores encontrados:")
        for nome, valor in todos.items():
            print(f"{nome}: {valor}")