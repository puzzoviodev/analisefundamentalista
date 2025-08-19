import fundamentus

import openpyxl
import time
from openpyxl.styles import numbers

TITLES = [
    'Identificação', 'Resumo Financeiro', 'Cotações', 'Informações Básicas',
    'Oscilações', 'Indicadores de Valuation', 'Indicadores de Rentabilidade',
    'Indicadores de Endividamento', 'Balanço Patrimonial', 'Demonstrativo de Resultados'
]




wbsaida = openpyxl.Workbook()
Dicrentabilidade = {}
Dicstock_identification = {}
Dicfinancial_summary = {}
Dicprice_information = {}
Dicdetailed_information = {}
Dicoscillations = {}
Dicprofitability_indicators = {}
Dicindebtedness_indicators = {}
Dicbalance_sheet = {}
Dicincome_statement = {}
Dicvaluation_indicators = {}










def montadicionario(stock_identification, financial_summary, price_information, detailed_information, oscillations,
                    valuation_indicators, profitability_indicators, indebtedness_indicators, balance_sheet,
                    income_statement):
    try:

        for information in stock_identification:
            Dicstock_identification[stock_identification[information].title] = stock_identification[information].value
        for information in financial_summary:
            Dicfinancial_summary[financial_summary[information].title] = financial_summary[information].value
        for information in price_information:
            Dicprice_information[price_information[information].title] = price_information[information].value
        for information in detailed_information:
            if information != 'variation_52_weeks':
                Dicdetailed_information[detailed_information[information].title] = detailed_information[
                    information].value
            else:
                for sub_information in detailed_information[information]:
                    Dicdetailed_information[detailed_information[information][sub_information].title] = \
                        detailed_information[information][sub_information].value
        for information in oscillations:
            Dicoscillations[oscillations[information].title] = oscillations[information].value
        for information in valuation_indicators:
            Dicvaluation_indicators[valuation_indicators[information].title] = valuation_indicators[information].value
        for information in profitability_indicators:
            Dicprofitability_indicators[profitability_indicators[information].title] = profitability_indicators[
                information].value
        for information in indebtedness_indicators:
            Dicindebtedness_indicators[indebtedness_indicators[information].title] = indebtedness_indicators[
                information].value
        for information in balance_sheet:
            Dicbalance_sheet[balance_sheet[information].title] = balance_sheet[information].value
        # for information in income_statement['three_months']:
        #   Dicincome_statement[income_statement[information].title] = income_statement[information].value
        # for information in income_statement['twelve_months']:
        #   Dicincome_statement[income_statement[information].title] = income_statement[information].value

    except Exception as e:
        print(f"Erro inesperado: {e}")
        print("montadicionario - Erro")
    finally:
        print("montadicionario - OK")
    return




import time

def evaluate_teste(pfcl):
    try:
        # Start timer
        start = time.time()

        print('Valor passado: ' + str(pfcl))
        stock = pfcl

        # Obter informações da ação
        main_pipeline = fundamentus.Pipeline(stock)
        response = main_pipeline.get_all_information()

        # Verifica se a resposta contém os dados esperados
        if not hasattr(response, 'transformed_information'):
            raise ValueError("Resposta inválida: 'transformed_information' não encontrado.")

        info = response.transformed_information

        # Extrair informações
        stock_identification = info.get('stock_identification', {})
        financial_summary = info.get('financial_summary', {})
        price_information = info.get('price_information', {})
        detailed_information = info.get('detailed_information', {})
        oscillations = info.get('oscillations', {})
        valuation_indicators = info.get('valuation_indicators', {})
        profitability_indicators = info.get('profitability_indicators', {})
        indebtedness_indicators = info.get('indebtedness_indicators', {})
        balance_sheet = info.get('balance_sheet', {})
        income_statement = info.get('income_statement', {})

        # Monta dicionário com os dados
        montadicionario(
            stock_identification, financial_summary, price_information,
            detailed_information, oscillations, valuation_indicators,
            profitability_indicators, indebtedness_indicators,
            balance_sheet, income_statement
        )

        # Extrai LPA com segurança
        LPA = detailed_information.get('LPA')
        print('Teste saída: ' + str(LPA))

        end = time.time()
        print(f'Informações obtidas em {int(end - start)} segundos.')

        return LPA

    except Exception as e:
        print(f"Erro ao avaliar '{pfcl}': {str(e)}")
        return None


