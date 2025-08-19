"""
investidor10_scraper.py

Scraper para Investidor10.
Extrai indicadores financeiros de https://investidor10.com.br/acoes/ITSA4/.
Ajustado para capturar indicadores da seção 'INDICADORES FUNDAMENTALISTAS ITSA4' e 'DADOS SOBRE A EMPRESA'.
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
    'Giro Ativos': ['Giro Ativos', 'GIRO ATIVOS', 'Asset Turnover'],
    'Dív. Líquida/PL': ['Dív. Líquida/PL', 'DÍVIDA LÍQUIDA / PATRIMÔNIO', 'Divida Liquida/PL', 'Net Debt/Equity'],
    'Dív. Líquida/EBITDA': ['Dív. Líquida/EBITDA', 'DÍVIDA LÍQUIDA / EBITDA', 'Divida Liquida/EBITDA', 'Net Debt/EBITDA'],
    'Dív. Líquida/EBIT': ['Dív. Líquida/EBIT', 'DÍVIDA LÍQUIDA / EBIT', 'Divida Liquida/EBIT', 'Net Debt/EBIT'],
    'PL/Ativos': ['PL/Ativos', 'PATRIMÔNIO / ATIVOS', 'Patrimônio Líquido/Ativos', 'Equity/Assets'],
    'Passivos/Ativos': ['Passivos/Ativos', 'PASSIVOS / ATIVOS', 'Liabilities/Assets'],
    'Liq. Corrente': ['Liq. Corrente', 'LIQUIDEZ CORRENTE', 'Current Ratio', 'Liquidez'],
    'P/L': ['P/L', 'Preço/Lucro', 'P/E'],
    'PEG Ratio': ['PEG Ratio', 'PEG', 'Price/Earnings to Growth'],
    'P/VP': ['P/VP', 'Preço/Valor Patrimonial', 'Price/Book'],
    'EV/EBITDA': ['EV/EBITDA', 'Enterprise Value/EBITDA'],
    'EV/EBIT': ['EV/EBIT', 'Enterprise Value/EBIT'],
    'P/EBITDA': ['P/EBITDA', 'Preço/EBITDA', 'Price/EBITDA'],
    'P/EBIT': ['P/EBIT', 'Preço/EBIT', 'Price/EBIT'],
    'VPA': ['VPA', 'Valor Patrimonial por Ação', 'Book Value per Share'],
    'P/Ativo': ['P/Ativo', 'P/ATIVO', 'Preço/Ativos', 'Price/Assets'],
    'LPA': ['LPA', 'Lucro por Ação', 'Earnings per Share'],
    'P/SR': ['P/SR', 'P/RECEITA (PSR)', 'Preço/Receita', 'Price/Sales'],
    'P/Ativo Circ. Líq.': ['P/Ativo Circ. Líq.', 'P/ATIVO CIRC LIQ', 'Preço/Ativo Circulante Líquido', 'Price/Net Current Assets'],
    'Disponibilidade': ['Disponibilidade', 'Caixa e Equivalentes', 'Cash and Equivalents'],
    'Patrimônio Líquido': ['Patrimônio Líquido', 'Patrimonio Liquido', 'Equity'],
    'Dívida Bruta': ['Dívida Bruta', 'DÍVIDA BRUTA / PATRIMÔNIO', 'Gross Debt'],
    'Dívida Líquida': ['Dívida Líquida', 'Divida Liquida', 'Net Debt'],
    'Ativos': ['Ativos', 'Ativo Total', 'Total Assets'],
    'Ativo Circulante': ['Ativo Circulante', 'Current Assets'],
    'Liquidez Média Diária': ['Liquidez Média Diária', 'LIQUIDEZ MÉDIA DIÁRIA', 'Average Daily Liquidity'],
    'ROE': ['ROE', 'Retorno sobre o Patrimônio', 'Return on Equity'],
    'ROIC': ['ROIC', 'Retorno sobre Capital Investido', 'Return on Invested Capital'],
    'Margem Bruta': ['Margem Bruta', 'MARGEM BRUTA', 'Gross Margin'],
    'Margem Líquida': ['Margem Líquida', 'MARGEM LÍQUIDA', 'Net Margin'],
    'Margem Operacional': ['Margem Operacional', 'MARGEM EBIT', 'Operational Margin'],
    'Margem EBITDA': ['Margem EBITDA', 'MARGEM EBITDA', 'Ebitda Margin'],
    'P/Cap. Giro': ['P/Cap. Giro', 'P/CAP.GIRO', 'Preço/Capital de Giro', 'Price/Working Capital'],
    'DY': ['DY', 'DIVIDEND YIELD', 'Dividend Yield', 'Rendimento de Dividendos']
}

def limpar_valor(valor_str):
    if not valor_str or valor_str in ['N/A', '-', '']:
        return None
    # Remove caracteres indesejados e normaliza
    valor_str = valor_str.replace('%', '').replace(',', '.').replace('R$', '').replace('Bilhões', '').replace('Milhões', '').replace('\xa0', ' ').strip()
    try:
        valor = float(valor_str)
        # Ajustar para valores em bilhões ou milhões
        if 'Bilhões' in valor_str:
            valor *= 1_000_000_000
        elif 'Milhões' in valor_str:
            valor *= 1_000_000
        return valor
    except ValueError:
        return None

def buscar_indicador(driver, nome_indicador, verbose=True):
    aliases = INDICADOR_ALIASES.get(nome_indicador, [nome_indicador])

    try:
        # Aguardar até que a seção de indicadores ou elementos _card estejam presentes
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'INDICADORES FUNDAMENTALISTAS') or contains(@class, '_card')]"))
        )
        if verbose: print("[INFO] Página carregada (seção de indicadores ou _card detectada).")

        html = driver.page_source
        if verbose: print("[INFO] HTML extraído via page_source")
        soup = BeautifulSoup(html, 'html.parser')

        irrelevant_keywords = ['setor', 'segmento', 'recomenda', 'nível', 'papeis', 'aviso', 'disclaimer']

        # Busca por cada alias do indicador
        for alias in aliases:
            pattern = re.compile(rf'{re.escape(alias)}', re.IGNORECASE)
            if verbose: print(f"[INFO] Buscando alias: {alias}")

            # 1. Busca em divs da seção de indicadores fundamentalistas
            items = soup.find_all('div', string=pattern)
            if verbose: print(f"[INFO] Encontrados {len(items)} divs com texto correspondente a '{alias}'")
            for item in items:
                title_text = item.get_text().strip().lower()
                if any(keyword in title_text for keyword in irrelevant_keywords):
                    if verbose: print(f"[INFO] Título '{title_text}' ignorado (contém palavra-chave irrelevante)")
                    continue
                value_tag = item.find('span')
                if value_tag:
                    valor_str = value_tag.get_text().strip()
                    valor = limpar_valor(valor_str)
                    if valor is not None:
                        if verbose: print(f"[OK] '{alias}' encontrado em div: {valor}")
                        return valor
                    if verbose: print(f"[INFO] Valor inválido para '{alias}' em div: {valor_str}")

            # 2. Busca em divs com class="_card.*"
            items = soup.find_all('div', class_=re.compile(r'_card.*'))
            if verbose: print(f"[INFO] Encontrados {len(items)} divs com class='_card.*'")
            for item in items:
                header = item.find('div', class_='_card-header')
                if header:
                    title_tag = header.find('span', string=pattern) or header.find('span', attrs={'title': pattern})
                    if title_tag:
                        title_text = title_tag.get_text().strip().lower()
                        if any(keyword in title_text for keyword in irrelevant_keywords):
                            if verbose: print(f"[INFO] Título '{title_text}' ignorado (contém palavra-chave irrelevante)")
                            continue
                        body = item.find('div', class_='_card-body')
                        if body:
                            value_tag = body.find('span')
                            if value_tag:
                                valor_str = value_tag.get_text().strip()
                                valor = limpar_valor(valor_str)
                                if valor is not None:
                                    if verbose: print(f"[OK] '{alias}' encontrado em _card.*: {valor}")
                                    return valor
                                if verbose: print(f"[INFO] Valor inválido para '{alias}' em _card.*: {valor_str}")

            # 3. Busca em DADOS SOBRE A EMPRESA
            data_section = soup.find('div', string=re.compile(r'SOBRE A EMPRESA', re.IGNORECASE))
            if data_section:
                parent = data_section.find_parent('div')
                if parent:
                    items = parent.find_all('div', string=pattern)
                    if verbose: print(f"[INFO] Encontrados {len(items)} divs em DADOS SOBRE A EMPRESA para '{alias}'")
                    for item in items:
                        title_text = item.get_text().strip().lower()
                        if any(keyword in title_text for keyword in irrelevant_keywords):
                            if verbose: print(f"[INFO] Título '{title_text}' ignorado (contém palavra-chave irrelevante)")
                            continue
                        value_tag = item.find_next('div')
                        if value_tag:
                            valor_str = value_tag.get_text().strip()
                            valor = limpar_valor(valor_str)
                            if valor is not None:
                                if verbose: print(f"[OK] '{alias}' encontrado em DADOS SOBRE A EMPRESA: {valor}")
                                return valor
                            if verbose: print(f"[INFO] Valor inválido para '{alias}' em DADOS SOBRE A EMPRESA: {valor_str}")

            # 4. Busca genérica em todos os spans
            items = soup.find_all('span', string=pattern)
            if verbose: print(f"[INFO] Encontrados {len(items)} spans com texto correspondente a '{alias}'")
            for item in items:
                title_text = item.get_text().strip().lower()
                if any(keyword in title_text for keyword in irrelevant_keywords):
                    if verbose: print(f"[INFO] Título '{title_text}' ignorado (contém palavra-chave irrelevante)")
                    continue
                value_tag = item.find_next('span')
                if value_tag:
                    valor_str = value_tag.get_text().strip()
                    valor = limpar_valor(valor_str)
                    if valor is not None:
                        if verbose: print(f"[OK] '{alias}' encontrado em span genérico: {valor}")
                        return valor
                    if verbose: print(f"[INFO] Valor inválido para '{alias}' em span genérico: {valor_str}")

        if verbose: print(f"[NOT FOUND] Indicador '{nome_indicador}' não encontrado.")
        return None

    except Exception as e:
        if verbose: print(f"[ERROR] Erro ao buscar '{nome_indicador}': {str(e)}")
        return None

def extrair_todos_indicadores(driver, verbose=True):
    indicadores = {}

    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'INDICADORES FUNDAMENTALISTAS') or contains(@class, '_card')]"))
        )
        if verbose: print("[INFO] Página carregada (seção de indicadores ou _card detectada).")

        html = driver.page_source
        if verbose: print("[INFO] HTML extraído via page_source")
        soup = BeautifulSoup(html, 'html.parser')

        irrelevant_keywords = ['setor', 'segmento', 'recomenda', 'nível', 'papeis', 'aviso', 'disclaimer']

        # 1. Busca na seção de indicadores fundamentalistas
        section = soup.find('div', string=re.compile(r'INDICADORES FUNDAMENTALISTAS ITSA4', re.IGNORECASE))
        if section:
            parent = section.find_parent('div')
            if parent:
                items = parent.find_all('div', string=True)
                if verbose: print(f"[INFO] Encontrados {len(items)} divs na seção INDICADORES FUNDAMENTALISTAS")
                for item in items:
                    nome = item.get_text().strip()
                    title_text = nome.lower()
                    if any(keyword in title_text for keyword in irrelevant_keywords):
                        if verbose: print(f"[INFO] Título '{nome}' ignorado (contém palavra-chave irrelevante)")
                        continue
                    value_tag = item.find('span')
                    if value_tag:
                        valor_str = value_tag.get_text().strip()
                        valor = limpar_valor(valor_str)
                        if valor is not None and nome and nome not in indicadores:
                            indicadores[nome] = valor
                            if verbose: print(f"[OK] Indicador encontrado: {nome} = {valor}")

        # 2. Busca em divs com class="_card.*"
        items = soup.find_all('div', class_=re.compile(r'_card.*'))
        if verbose: print(f"[INFO] Encontrados {len(items)} divs com class='_card.*'")
        for item in items:
            header = item.find('div', class_='_card-header')
            if header:
                title_tag = header.find('span', string=True) or header.find('span', attrs={'title': True})
                if title_tag:
                    nome = title_tag.get_text().strip()
                    title_text = nome.lower()
                    if any(keyword in title_text for keyword in irrelevant_keywords):
                        if verbose: print(f"[INFO] Título '{nome}' ignorado (contém palavra-chave irrelevante)")
                        continue
                    body = item.find('div', class_='_card-body')
                    if body:
                        value_tag = body.find('span')
                        if value_tag:
                            valor_str = value_tag.get_text().strip()
                            valor = limpar_valor(valor_str)
                            if valor is not None and nome and nome not in indicadores:
                                indicadores[nome] = valor
                                if verbose: print(f"[OK] Indicador encontrado: {nome} = {valor}")

        # 3. Busca em DADOS SOBRE A EMPRESA
        data_section = soup.find('div', string=re.compile(r'SOBRE A EMPRESA', re.IGNORECASE))
        if data_section:
            parent = data_section.find_parent('div')
            if parent:
                items = parent.find_all('div', string=True)
                if verbose: print(f"[INFO] Encontrados {len(items)} divs em DADOS SOBRE A EMPRESA")
                for item in items:
                    nome = item.get_text().strip()
                    title_text = nome.lower()
                    if any(keyword in title_text for keyword in irrelevant_keywords):
                        if verbose: print(f"[INFO] Título '{nome}' ignorado (contém palavra-chave irrelevante)")
                        continue
                    value_tag = item.find_next('div')
                    if value_tag:
                        valor_str = value_tag.get_text().strip()
                        valor = limpar_valor(valor_str)
                        if valor is not None and nome and nome not in indicadores:
                            indicadores[nome] = valor
                            if verbose: print(f"[OK] Indicador encontrado em DADOS SOBRE A EMPRESA: {nome} = {valor}")

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
        indicadores = [
            'Giro Ativos', 'Dív. Líquida/PL', 'Dív. Líquida/EBITDA', 'Dív. Líquida/EBIT',
            'PL/Ativos', 'Passivos/Ativos', 'Liq. Corrente', 'P/L', 'PEG Ratio', 'P/VP',
            'EV/EBITDA', 'EV/EBIT', 'P/EBITDA', 'P/EBIT', 'VPA', 'P/Ativo', 'LPA',
            'P/SR', 'P/Ativo Circ. Líq.', 'Disponibilidade', 'Patrimônio Líquido',
            'Dívida Bruta', 'Dívida Líquida', 'Ativos', 'Ativo Circulante',
            'Liquidez Média Diária', 'ROE', 'ROIC', 'Margem Bruta', 'Margem Líquida',
            'Margem Operacional', 'Margem EBITDA', 'P/Cap. Giro', 'DY'
        ]
        resultados = {}
        for indicador in indicadores:
            valor = buscar_indicador(driver, indicador)
            resultados[indicador] = valor
            print(f"{indicador}: {valor}")
        print("\nTodos os indicadores encontrados:")
        todos = extrair_todos_indicadores(driver)
        for nome, valor in todos.items():
            print(f"{nome}: {valor}")
        print("\nResumo dos indicadores:")
        print(", ".join(f"{indicador} = {resultados[indicador]}" for indicador in indicadores))