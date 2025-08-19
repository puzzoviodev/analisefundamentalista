# Funções extraídas

def evaluate_divida_liquida_ebitda(divida_liquida_ebitda):
    """
    Avalia a Dívida Líquida/EBITDA com base em faixas definidas para o mercado brasileiro:
    - Dívida Líquida/EBITDA < 0: Fora da faixa (sem dívida líquida ou EBITDA negativo)
    - 0 ≤ Dívida Líquida/EBITDA ≤ 1: Ótimo (endividamento muito baixo)
    - 1 < Dívida Líquida/EBITDA ≤ 2: Moderado (endividamento aceitável)
    - 2 < Dívida Líquida/EBITDA ≤ 3: Ruim (endividamento elevado)
    - 3 < Dívida Líquida/EBITDA ≤ 4: Péssimo (endividamento muito alto)
    - Dívida Líquida/EBITDA > 4: Crítico (endividamento excessivo, risco elevado)
    """
    definicao = """
    A Dívida Líquida/EBITDA mede a capacidade da empresa de pagar sua dívida líquida com base no EBITDA,
    calculada como (Dívida Total - Caixa e Equivalentes) / EBITDA. É um indicador chave de alavancagem
    financeira, mostrando quantos anos a empresa levaria para quitar sua dívida líquida com sua geração
    de caixa operacional. Um valor baixo indica saúde financeira, enquanto um valor alto sugere risco
    financeiro elevado. É amplamente utilizado em setores intensivos em capital, como mineração e energia.
    """
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida/EBITDA = (Dívida Total - Caixa e Equivalentes) / EBITDA'

    try:
        if divida_liquida_ebitda < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Líquida/EBITDA < 0',
                'descricao': """
                Um valor negativo indica que a empresa não possui dívida líquida (caixa excede a dívida)
                ou que o EBITDA é negativo. Empresas como a Totvs (TOTS3), com forte geração de caixa, podem
                apresentar valores negativos em períodos de alta liquidez. Para investidores, isso pode ser
                positivo, sugerindo solidez financeira, mas também pode indicar ineficiência na alocação de
                capital, como excesso de caixa ocioso. Análises complementares, como ROIC e fluxo de caixa livre,
                são recomendadas para avaliar a eficiência do uso do caixa.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_liquida_ebitda <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Líquida/EBITDA <= 1',
                'descricao': """
                Um valor entre 0 e 1 reflete endividamento muito baixo, indicando que a empresa pode quitar
                sua dívida líquida rapidamente com sua geração de caixa. Empresas como a Vale (VALE3) em períodos
                de alta nos preços de minério de ferro frequentemente operam nessa faixa. Para investidores,
                essa faixa é atrativa, pois sugere baixo risco financeiro e flexibilidade para investimentos ou
                dividendos. É importante verificar a consistência do EBITDA e a composição da dívida.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_liquida_ebitda <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Dívida Líquida/EBITDA <= 2',
                'descricao': """
                Um valor entre 1 e 2 indica endividamento aceitável, com a empresa mantendo um equilíbrio entre
                dívida e geração de caixa. No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa
                faixa devido à sua gestão financeira eficiente. Para investidores, essa faixa sugere risco moderado,
                com a empresa capaz de suportar oscilações econômicas sem grandes pressões. É importante avaliar
                a estrutura da dívida (curto vs. longo prazo) e a geração de fluxo de caixa livre.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_liquida_ebitda <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida Líquida/EBITDA <= 3',
                'descricao': """
                Um valor entre 2 e 3 sugere endividamento elevado, indicando que a empresa levaria um tempo
                considerável para quitar sua dívida líquida com o EBITDA. Isso é comum em setores intensivos em
                capital, como a Petrobras (PETR4) em períodos de investimentos pesados. Para investidores, essa
                faixa exige cautela, pois a empresa pode ser vulnerável a aumentos de juros ou quedas na receita.
                Análise de fluxo de caixa e covenants de dívida é recomendada.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < divida_liquida_ebitda <= 4:
            return {
                'classificacao': 'Péssimo',
                'faixa': '3 < Dívida Líquida/EBITDA <= 4',
                'descricao': """
                Um valor entre 3 e 4 reflete endividamento muito alto, indicando risco significativo de pressão
                financeira. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises, enfrentando dificuldades
                para gerenciar dívidas elevadas. Para investidores, essa faixa é preocupante, exigindo análise detalhada
                da estrutura de capital, planos de desalavancagem e fluxo de caixa operacional.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_liquida_ebitda > 4:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Líquida/EBITDA > 4',
                'descricao': """
                Um valor acima de 4 indica endividamento excessivo, sugerindo que a empresa depende fortemente de
                dívidas em relação à sua geração de caixa. Isso é alarmante e típico de empresas em dificuldades
                financeiras, como a Gol (GOLL4) em períodos de crise no setor aéreo. Para investidores, essa faixa é
                de altíssimo risco, com possibilidade de reestruturação ou insolvência. A análise deve focar na
                capacidade de geração de caixa, estratégias de redução de dívida e covenants financeiros.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f"""
            Ocorreu um erro ao processar a Dívida Líquida/EBITDA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o EBITDA for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que a dívida líquida e o EBITDA estejam corretos e sejam valores numéricos válidos.
            """,
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_p_l(p_l):
    '''
    Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro:
    - P/L < 0: Crítico (lucro negativo, risco elevado)
    - 0 ≤ P/L ≤ 10: Ótimo (subvalorizado, oportunidade de compra)
    - 10 < P/L ≤ 15: Moderado (valuation justo)
    - 15 < P/L ≤ 20: Ruim (sobrevalorizado, cautela necessária)
    - 20 < P/L ≤ 25: Péssimo (muito caro, alto risco)
    - P/L > 25: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Preço/Lucro (P/L) compara o preço da ação ao lucro por ação, calculado como (Preço da Ação / Lucro por Ação).
    É um indicador de valuation que avalia se a ação está cara ou barata em relação aos lucros. Um P/L baixo
    sugere subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
    '''
    agrupador = 'Valuation'
    formula = 'P/L = Preço da Ação / Lucro por Ação'

    try:
        if p_l < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/L < 0',
                'descricao': '''
                Um P/L negativo indica que a empresa está gerando prejuízo, sugerindo risco elevado. Isso é comum
                em empresas em crise, como a Oi (OIBR3). Para investidores, essa faixa exige análise detalhada da
                saúde financeira e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_l <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/L <= 10',
                'descricao': '''
                Um P/L entre 0 e 10 sugere que a ação está subvalorizada, indicando uma potencial oportunidade de
                compra. Isso é comum em setores cíclicos, como a Vale (VALE3) em períodos de baixa. Para investidores,
                essa faixa é atrativa, mas é importante verificar a sustentabilidade dos lucros.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < p_l <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '10 < P/L <= 15',
                'descricao': '''
                Um P/L entre 10 e 15 reflete um valuation justo, típico de empresas com lucros estáveis. Empresas
                como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio
                entre preço e fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < p_l <= 20:
            return {
                'classificacao': 'Ruim',
                'faixa': '15 < P/L <= 20',
                'descricao': '''
                Um P/L entre 15 e 20 sugere que a ação está sobrevalorizada, indicando que o mercado espera
                crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa. Para
                investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar sem crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < p_l <= 25:
            return {
                'classificacao': 'Péssimo',
                'faixa': '20 < P/L <= 25',
                'descricao': '''
                Um P/L entre 20 e 25 indica que a ação é muito cara, sugerindo que o mercado está pagando um
                prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar P/L nessa faixa em momentos de
                otimismo. Para investidores, essa faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif p_l > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/L > 25',
                'descricao': '''
                Um P/L acima de 25 é extremamente elevado, geralmente associado a empresas com altíssimas
                expectativas de crescimento, como o Nubank (NUBR33). Para investidores, essa faixa é de altíssimo
                risco, refletindo mais especulação do que fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o P/L: {str(e)}. Isso pode ter acontecido se o valor fornecido não for
            numérico ou se o lucro por ação for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o preço da ação e o lucro por ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_liquidez_corrente(liquidez_corrente):
    '''
    Avalia a Liquidez Corrente com base em faixas definidas para o mercado brasileiro:
    - Liquidez Corrente < 0.5: Crítico (dificuldade extrema em pagar obrigações de curto prazo)
    - 0.5 ≤ Liquidez Corrente ≤ 1: Ruim (capacidade limitada de pagar obrigações de curto prazo)
    - 1 < Liquidez Corrente ≤ 1.5: Moderado (capacidade aceitável de pagar obrigações de curto prazo)
    - 1.5 < Liquidez Corrente ≤ 2: Ótimo (boa capacidade de pagar obrigações de curto prazo)
    - Liquidez Corrente > 2: Fora da faixa (excesso de liquidez, possível ineficiência)
    '''
    definicao = '''
    A Liquidez Corrente mede a capacidade da empresa de pagar suas obrigações de curto prazo com seus
    ativos circulantes, calculada como (Ativo Circulante / Passivo Circulante). É um indicador de liquidez
    que reflete a saúde financeira de curto prazo. Um valor alto sugere solidez, enquanto um valor baixo
    indica risco de inadimplência.
    '''
    agrupador = 'Liquidez'
    formula = 'Liquidez Corrente = Ativo Circulante / Passivo Circulante'

    try:
        if liquidez_corrente < 0.5:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Liquidez Corrente < 0.5',
                'descricao': '''
                Uma Liquidez Corrente abaixo de 0.5 indica dificuldade extrema em pagar obrigações de curto prazo,
                sugerindo risco elevado de inadimplência. Isso é comum em empresas em crise, como a Oi (OIBR3).
                Para investidores, essa faixa é um alerta grave, exigindo análise da gestão de caixa e recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 <= liquidez_corrente <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 <= Liquidez Corrente <= 1',
                'descricao': '''
                Uma Liquidez Corrente entre 0.5 e 1 reflete capacidade limitada de pagar obrigações de curto prazo,
                indicando dependência de conversão de ativos em caixa. Isso é comum em setores com margens apertadas,
                como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < liquidez_corrente <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Liquidez Corrente <= 1.5',
                'descricao': '''
                Uma Liquidez Corrente entre 1 e 1.5 indica capacidade aceitável de pagar obrigações de curto prazo.
                Empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere
                equilíbrio entre liquidez e eficiência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < liquidez_corrente <= 2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1.5 < Liquidez Corrente <= 2',
                'descricao': '''
                Uma Liquidez Corrente entre 1.5 e 2 reflete boa capacidade de pagar obrigações de curto prazo,
                indicando solidez financeira. Empresas como a Ambev (ABEV3) frequentemente apresentam liquidez nessa
                faixa. Para investidores, essa faixa é atrativa, sugerindo resiliência financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif liquidez_corrente > 2:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Liquidez Corrente > 2',
                'descricao': '''
                Uma Liquidez Corrente acima de 2 indica excesso de liquidez, com ativos circulantes muito superiores
                às obrigações de curto prazo. Isso pode ocorrer em empresas como a Vale (VALE3) em períodos de alta
                geração de caixa. Para investidores, essa faixa pode ser positiva, mas também pode indicar ineficiência
                na alocação de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Liquidez Corrente: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o passivo circulante for zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que o ativo circulante e o passivo circulante estejam corretos e sejam
            valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_giro_ativos(giro_ativos):
    '''
    Avalia o Giro de Ativos com base em faixas definidas para o mercado brasileiro:
    - Giro de Ativos < 0.2: Crítico (baixa eficiência no uso de ativos)
    - 0.2 ≤ Giro de Ativos ≤ 0.5: Ruim (eficiência limitada no uso de ativos)
    - 0.5 < Giro de Ativos ≤ 1: Moderado (eficiência aceitável no uso de ativos)
    - 1 < Giro de Ativos ≤ 1.5: Ótimo (alta eficiência no uso de ativos)
    - Giro de Ativos > 1.5: Fora da faixa (eficiência excepcional no uso de ativos)
    '''
    definicao = '''
    O Giro de Ativos mede a eficiência da empresa em gerar receita com seus ativos totais, calculado
    como (Receita Bruta / Ativos Totais). É um indicador que reflete como a empresa utiliza seus ativos
    para gerar vendas. Um valor alto sugere eficiência, enquanto um valor baixo indica subutilização de
    ativos.
    '''
    agrupador = 'Eficiência'
    formula = 'Giro de Ativos = Receita Bruta / Ativos Totais'

    try:
        if giro_ativos < 0.2:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Giro de Ativos < 0.2',
                'descricao': '''
                Um Giro de Ativos abaixo de 0.2 indica baixa eficiência no uso de ativos, sugerindo subutilização
                ou ativos ociosos. Isso é comum em empresas com grandes investimentos fixos, como a CSN (CSNA3) em
                períodos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 <= giro_ativos <= 0.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 <= Giro de Ativos <= 0.5',
                'descricao': '''
                Um Giro de Ativos entre 0.2 e 0.5 reflete eficiência limitada no uso de ativos, indicando que a
                empresa gera receita moderada em relação aos ativos. Isso é comum em setores intensivos em capital,
                como a Petrobras (PETR4). Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < giro_ativos <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Giro de Ativos <= 1',
                'descricao': '''
                Um Giro de Ativos entre 0.5 e 1 indica eficiência aceitável no uso de ativos. Empresas como a
                Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio
                entre eficiência e estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < giro_ativos <= 1.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Giro de Ativos <= 1.5',
                'descricao': '''
                Um Giro de Ativos entre 1 e 1.5 reflete alta eficiência no uso de ativos, indicando que a empresa
                gera receita significativa com seus ativos. Empresas como a Ambev (ABEV3) frequentemente apresentam
                giro nessa faixa. Para investidores, essa faixa é atrativa, sugerindo eficiência operacional.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif giro_ativos > 1.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Giro de Ativos > 1.5',
                'descricao': '''
                Um Giro de Ativos acima de 1.5 é excepcional, indicando eficiência extremamente alta no uso de
                ativos. Isso pode ocorrer em empresas como a Magazine Luiza (MGLU3) em períodos de forte crescimento.
                Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois pode não ser sustentável.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Giro de Ativos: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se os ativos totais forem zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que a receita bruta e os ativos totais estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_p_vp(p_vp):
    '''
    Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas definidas para o mercado brasileiro:
    - P/VP < 0: Fora da faixa (patrimônio líquido negativo)
    - 0 ≤ P/VP ≤ 1: Ótimo (subvalorizado, oportunidade de compra)
    - 1 < P/VP ≤ 1.5: Moderado (valuation justo)
    - 1.5 < P/VP ≤ 2: Ruim (sobrevalorizado, cautela necessária)
    - 2 < P/VP ≤ 3: Péssimo (muito caro, alto risco)
    - P/VP > 3: Crítico (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado
    como (Preço da Ação / Valor Patrimonial por Ação). É um indicador de valuation que avalia se a
    ação está cara ou barata em relação aos ativos líquidos da empresa. Um P/VP baixo sugere
    subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
    '''
    agrupador = 'Valuation'
    formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    try:
        if p_vp < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/VP < 0',
                'descricao': '''
                Um P/VP negativo indica que o patrimônio líquido da empresa é negativo, sugerindo sérias
                dificuldades financeiras. Isso é comum em empresas em crise, como a Oi (OIBR3). Para
                investidores, essa faixa é um alerta grave, exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_vp <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/VP <= 1',
                'descricao': '''
                Um P/VP entre 0 e 1 sugere que a ação está subvalorizada, sendo negociada abaixo do seu
                valor patrimonial. Isso é comum em setores cíclicos, como a Vale (VALE3) em períodos de baixa.
                Para investidores, essa faixa é atrativa, mas é importante verificar a qualidade dos ativos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < p_vp <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < P/VP <= 1.5',
                'descricao': '''
                Um P/VP entre 1 e 1.5 reflete um valuation justo, típico de empresas com estabilidade financeira.
                Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores, essa faixa
                sugere equilíbrio entre preço e fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < p_vp <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '1.5 < P/VP <= 2',
                'descricao': '''
                Um P/VP entre 1.5 e 2 sugere que a ação está sobrevalorizada, indicando que o mercado espera
                crescimento. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa. Para investidores,
                essa faixa exige cautela, pois o preço elevado pode não se sustentar sem crescimento robusto.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < p_vp <= 3:
            return {
                'classificacao': 'Péssimo',
                'faixa': '2 < P/VP <= 3',
                'descricao': '''
                Um P/VP entre 2 e 3 indica que a ação é muito cara, sugerindo que o mercado está pagando um
                prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar P/VP nessa faixa em momentos
                de otimismo. Para investidores, essa faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif p_vp > 3:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/VP > 3',
                'descricao': '''
                Um P/VP acima de 3 é extremamente elevado, geralmente associado a empresas com altíssimas
                expectativas de crescimento, como o Nubank (NUBR33). Para investidores, essa faixa reflete
                especulação e alto risco, exigindo análise detalhada dos fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o P/VP: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se o valor patrimonial por ação for zero, o que impede o cálculo.
            Verifique os dados de entrada, assegurando que o preço da ação e o valor patrimonial por ação
            estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_divida_liquida_patrimonio(divida_liquida_patrimonio):
    '''
    Avalia a Dívida Líquida/Patrimônio com base em faixas definidas para o mercado brasileiro:
    - Dívida Líquida/Patrimônio < 0: Fora da faixa (sem dívida líquida ou patrimônio negativo)
    - 0 ≤ Dívida Líquida/Patrimônio ≤ 0.3: Ótimo (endividamento muito baixo)
    - 0.3 < Dívida Líquida/Patrimônio ≤ 0.6: Moderado (endividamento aceitável)
    - 0.6 < Dívida Líquida/Patrimônio ≤ 1: Ruim (endividamento elevado)
    - 1 < Dívida Líquida/Patrimônio ≤ 1.5: Péssimo (endividamento muito alto)
    - Dívida Líquida/Patrimônio > 1.5: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida Líquida/Patrimônio mede a proporção da dívida líquida (dívida total menos caixa e equivalentes)
    em relação ao patrimônio líquido, calculada como (Dívida Líquida / Patrimônio Líquido). É um indicador
    de alavancagem financeira que avalia o nível de endividamento líquido. Um valor baixo sugere solidez,
    enquanto um valor alto indica maior risco financeiro.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida/Patrimônio = Dívida Líquida / Patrimônio Líquido'

    try:
        if divida_liquida_patrimonio < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Líquida/Patrimônio < 0',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio negativa indica que a empresa tem mais caixa do que dívida ou
                que o patrimônio líquido é negativo. Empresas como a Totvs (TOTS3) podem apresentar valores
                negativos em períodos de alta liquidez, enquanto um patrimônio negativo (ex.: Oi - OIBR3) é
                alarmante. Para investidores, essa faixa exige análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_liquida_patrimonio <= 0.3:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Líquida/Patrimônio <= 0.3',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 0 e 0.3 reflete endividamento muito baixo, indicando
                solidez financeira. Empresas como a Vale (VALE3) em períodos de alta geração de caixa
                frequentemente operam nessa faixa. Para investidores, essa faixa é atrativa, sugerindo
                baixo risco financeiro.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < divida_liquida_patrimonio <= 0.6:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < Dívida Líquida/Patrimônio <= 0.6',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 0.3 e 0.6 indica endividamento aceitável, com equilíbrio
                entre dívida líquida e capital próprio. Empresas como a Ambev (ABEV3) frequentemente operam
                nessa faixa. Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.6 < divida_liquida_patrimonio <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.6 < Dívida Líquida/Patrimônio <= 1',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 0.6 e 1 sugere endividamento elevado, indicando
                dependência significativa de dívidas líquidas. Isso é comum em setores intensivos em capital,
                como a Petrobras (PETR4). Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_liquida_patrimonio <= 1.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1 < Dívida Líquida/Patrimônio <= 1.5',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 1 e 1.5 reflete endividamento muito alto, indicando
                risco significativo. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises.
                Para investidores, essa faixa é preocupante, exigindo análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_liquida_patrimonio > 1.5:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Líquida/Patrimônio > 1.5',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio acima de 1.5 indica endividamento excessivo, sugerindo
                dependência extrema de dívidas líquidas. Isso é típico de empresas em dificuldades, como
                a Gol (GOLL4) em crises. Para investidores, essa faixa é de altíssimo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida Líquida/Patrimônio: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se o patrimônio líquido for zero,
            o que impede o cálculo. Verifique os dados de entrada, assegurando que a dívida líquida
            e o patrimônio líquido estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_p_ebitda(p_ebitda):
    '''
    Avalia o Preço/EBITDA com base em faixas definidas para o mercado brasileiro:
    - P/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
    - 0 ≤ P/EBITDA ≤ 4: Ótimo (subvalorizado, oportunidade de compra)
    - 4 < P/EBITDA ≤ 8: Moderado (valuation justo)
    - 8 < P/EBITDA ≤ 12: Ruim (sobrevalorizado, cautela necessária)
    - 12 < P/EBITDA ≤ 16: Péssimo (muito caro, alto risco)
    - P/EBITDA > 16: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Preço/EBITDA compara o valor da empresa (valor de mercado + dívida líquida) ao EBITDA,
    calculado como (Enterprise Value / EBITDA). É um indicador de valuation que avalia se a
    empresa está cara ou barata em relação à sua lucratividade operacional. Um P/EBITDA baixo
    sugere subvalorização, enquanto um valor alto indica sobrevalorização.
    '''
    agrupador = 'Valuation'
    formula = 'P/EBITDA = Enterprise Value / EBITDA'

    try:
        if p_ebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/EBITDA < 0',
                'descricao': '''
                Um P/EBITDA negativo indica que a empresa tem EBITDA negativo, sugerindo prejuízo
                operacional. Isso é comum em empresas em crise, como a Oi (OIBR3). Para investidores,
                essa faixa é um alerta grave, exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_ebitda <= 4:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/EBITDA <= 4',
                'descricao': '''
                Um P/EBITDA entre 0 e 4 sugere que a empresa está subvalorizada, sendo uma potencial
                oportunidade de compra. Isso é comum em setores cíclicos, como a Vale (VALE3) em
                períodos de baixa. Para investidores, essa faixa é atrativa, mas exige verificação
                da sustentabilidade do EBITDA.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < p_ebitda <= 8:
            return {
                'classificacao': 'Moderado',
                'faixa': '4 < P/EBITDA <= 8',
                'descricao': '''
                Um P/EBITDA entre 4 e 8 reflete um valuation justo, típico de empresas com lucratividade
                estável. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para
                investidores, essa faixa sugere equilíbrio entre preço e fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 8 < p_ebitda <= 12:
            return {
                'classificacao': 'Ruim',
                'faixa': '8 < P/EBITDA <= 12',
                'descricao': '''
                Um P/EBITDA entre 8 e 12 sugere que a empresa está sobrevalorizada, indicando que o
                mercado espera crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem
                atingir essa faixa. Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 12 < p_ebitda <= 16:
            return {
                'classificacao': 'Péssimo',
                'faixa': '12 < P/EBITDA <= 16',
                'descricao': '''
                Um P/EBITDA entre 12 e 16 indica que a empresa é muito cara, sugerindo que o mercado
                está pagando um prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar
                P/EBITDA nessa faixa em momentos de otimismo. Para investidores, essa faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif p_ebitda > 16:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/EBITDA > 16',
                'descricao': '''
                Um P/EBITDA acima de 16 é extremamente elevado, geralmente associado a empresas com
                altíssimas expectativas de crescimento, como o Nubank (NUBR33). Para investidores,
                essa faixa reflete especulação e alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o P/EBITDA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o EBITDA for zero, o que impede o cálculo. Verifique
            os dados de entrada, assegurando que o enterprise value e o EBITDA estejam corretos
            e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_ev_ebit(ev_ebit):
    '''
    Avalia o Enterprise Value/EBIT com base em faixas definidas para o mercado brasileiro:
    - EV/EBIT < 0: Crítico (EBIT negativo, risco elevado)
    - 0 ≤ EV/EBIT ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
    - 5 < EV/EBIT ≤ 10: Moderado (valuation justo)
    - 10 < EV/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
    - 15 < EV/EBIT ≤ 20: Péssimo (muito caro, alto risco)
    - EV/EBIT > 20: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Enterprise Value/EBIT compara o valor da empresa (valor de mercado + dívida líquida)
    ao lucro operacional antes de juros e impostos, calculado como (Enterprise Value / EBIT).
    É um indicador de valuation que avalia se a empresa está cara ou barata em relação à sua
    lucratividade operacional. Um EV/EBIT baixo sugere subvalorização, enquanto um valor alto
    indica sobrevalorização.
    '''
    agrupador = 'Valuation'
    formula = 'EV/EBIT = Enterprise Value / EBIT'

    try:
        if ev_ebit < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'EV/EBIT < 0',
                'descricao': '''
                Um EV/EBIT negativo indica que a empresa tem EBIT negativo, sugerindo prejuízo
                operacional. Isso é comum em empresas em crise, como a Oi (OIBR3). Para investidores,
                essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= ev_ebit <= 5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= EV/EBIT <= 5',
                'descricao': '''
                Um EV/EBIT entre 0 e 5 sugere que a empresa está subvalorizada, sendo uma potencial
                oportunidade de compra. Isso é comum em setores cíclicos, como a Vale (VALE3) em
                períodos de baixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < ev_ebit <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < EV/EBIT <= 10',
                'descricao': '''
                Um EV/EBIT entre 5 e 10 reflete um valuation justo, típico de empresas com
                lucratividade estável. Empresas como a Ambev (ABEV3) frequentemente operam nessa
                faixa. Para investidores, essa faixa sugere equilíbrio entre preço e fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < ev_ebit <= 15:
            return {
                'classificacao': 'Ruim',
                'faixa': '10 < EV/EBIT <= 15',
                'descricao': '''
                Um EV/EBIT entre 10 e 15 sugere que a empresa está sobrevalorizada, indicando
                que o mercado espera crescimento significativo. Empresas como a Raia Drogasil
                (RADL3) podem atingir essa faixa. Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < ev_ebit <= 20:
            return {
                'classificacao': 'Péssimo',
                'faixa': '15 < EV/EBIT <= 20',
                'descricao': '''
                Um EV/EBIT entre 15 e 20 indica que a empresa é muito cara, sugerindo que o
                mercado está pagando um prêmio elevado. Empresas como a Localiza (RENT3) podem
                apresentar EV/EBIT nessa faixa em momentos de otimismo. Para investidores, essa
                faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif ev_ebit > 20:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'EV/EBIT > 20',
                'descricao': '''
                Um EV/EBIT acima de 20 é extremamente elevado, geralmente associado a empresas com
                altíssimas expectativas de crescimento, como o Nubank (NUBR33). Para investidores,
                essa faixa reflete especulação e alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o EV/EBIT: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o EBIT for zero, o que impede o cálculo. Verifique
            os dados de entrada, assegurando que o enterprise value e o EBIT estejam corretos
            e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_giro_ativos(giro_ativos):
    '''
    Avalia o Giro de Ativos com base em faixas definidas para o mercado brasileiro:
    - Giro de Ativos < 0.3: Crítico (baixa eficiência no uso de ativos)
    - 0.3 ≤ Giro de Ativos ≤ 0.6: Ruim (eficiência baixa)
    - 0.6 < Giro de Ativos ≤ 1: Moderado (eficiência aceitável)
    - 1 < Giro de Ativos ≤ 1.5: Ótimo (eficiência robusta)
    - Giro de Ativos > 1.5: Fora da faixa (eficiência excepcional)
    '''
    definicao = '''
    O Giro de Ativos mede a eficiência com que a empresa utiliza seus ativos para gerar receita,
    calculado como (Receita Bruta / Ativos Totais). É um indicador de eficiência operacional
    que reflete a capacidade da empresa de maximizar o uso de seus ativos. Um giro alto sugere
    eficiência, enquanto um giro baixo indica subutilização.
    '''
    agrupador = 'Eficiência'
    formula = 'Giro de Ativos = Receita Bruta / Ativos Totais'

    try:
        if giro_ativos < 0.3:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Giro de Ativos < 0.3',
                'descricao': '''
                Um Giro de Ativos abaixo de 0.3 indica baixa eficiência no uso dos ativos, sugerindo
                subutilização ou ativos ociosos. Isso é comum em empresas em crise, como a Oi (OIBR3).
                Para investidores, essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 <= giro_ativos <= 0.6:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.3 <= Giro de Ativos <= 0.6',
                'descricao': '''
                Um Giro de Ativos entre 0.3 e 0.6 reflete eficiência baixa, indicando que a empresa
                tem dificuldade em gerar receita com seus ativos. Isso é comum em setores intensivos
                em capital, como a Petrobras (PETR4). Para investidores, essa faixa sugere risco
                moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.6 < giro_ativos <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.6 < Giro de Ativos <= 1',
                'descricao': '''
                Um Giro de Ativos entre 0.6 e 1 indica eficiência aceitável, típico de empresas com
                utilização moderada de ativos. Empresas como a Suzano (SUZB3) frequentemente operam
                nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < giro_ativos <= 1.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Giro de Ativos <= 1.5',
                'descricao': '''
                Um Giro de Ativos entre 1 e 1.5 reflete eficiência robusta, indicando que a empresa
                utiliza seus ativos de forma eficaz. Empresas como a Ambev (ABEV3) frequentemente
                apresentam giro nessa faixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif giro_ativos > 1.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Giro de Ativos > 1.5',
                'descricao': '''
                Um Giro de Ativos acima de 1.5 é excepcional, indicando eficiência extremamente alta
                no uso dos ativos. Isso pode ocorrer em empresas como a Magazine Luiza (MGLU3) em
                períodos de alta rotatividade. Para investidores, essa faixa é altamente atrativa,
                mas exige análise da sustentabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Giro de Ativos: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se os ativos totais forem zero, o que
            impede o cálculo. Verifique os dados de entrada, assegurando que a receita bruta
            e os ativos totais estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_pebit(pebit):
        '''
        Avalia o Preço/EBIT com base em faixas definidas para o mercado brasileiro:
        - P/EBIT < 0: Crítico (EBIT negativo, risco elevado)
        - 0 ≤ P/EBIT ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
        - 5 < P/EBIT ≤ 10: Moderado (valuation justo, crescimento moderado)
        - 10 < P/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
        - 15 < P/EBIT ≤ 20: Péssimo (muito caro, alto risco)
        - P/EBIT > 20: Fora da faixa (extremamente sobrevalorizado, risco elevado)
        '''
        definicao = '''
        Indicador que relaciona o preço da ação ao EBIT, medindo a capacidade da empresa de gerar
        lucro operacional em relação ao seu valor de mercado. É útil para avaliar a lucratividade
        antes de impostos e juros.
        '''
        agrupador = 'Valuation'
        formula = 'P/EBIT = Preço da Ação / EBIT por Ação'

        try:
            if pebit < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'P/EBIT < 0',
                    'descricao': '''
                    P/EBIT negativo indica EBIT negativo, sugerindo ineficiência operacional ou prejuízo.
                    Comum em setores com alta depreciação (ex.: siderurgia, como CSNA3). Exige análise
                    de fluxo de caixa.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= pebit <= 5:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '0 <= P/EBIT <= 5',
                    'descricao': '''
                    P/EBIT baixo sugere subvalorização, indicando oportunidade de compra. Comum em setores
                    cíclicos (ex.: mineração como VALE3) ou empresas com desafios temporários.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < pebit <= 10:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5 < P/EBIT <= 10',
                    'descricao': '''
                    P/EBIT indica valuation justo, típico de empresas com geração de lucro operacional
                    estável (ex.: energia como ELET3). Equilíbrio entre risco e retorno.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 10 < pebit <= 15:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '10 < P/EBIT <= 15',
                    'descricao': '''
                    P/EBIT elevado sugere sobrevalorização moderada, comum em setores de crescimento
                    (ex.: varejo como MGLU3). Exige análise de margens e crescimento futuro.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 15 < pebit <= 20:
                return {
                    'classificacao': 'Péssimo',
                    'faixa': '15 < P/EBIT <= 20',
                    'descricao': '''
                    P/EBIT muito alto indica ação cara, com expectativas de crescimento elevadas. Risco
                    de correção em setores como tecnologia (ex.: TOTS3).
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            else:  # pebit > 20
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'P/EBIT > 20',
                    'descricao': '''
                    P/EBIT extremamente elevado sugere sobrevalorização severa, típica de empresas
                    especulativas (ex.: startups listadas como NUBR33). Análise detalhada do crescimento
                    é essencial.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Erro ao processar P/EBIT: {str(e)}. Verifique se o valor fornecido é um número válido
                e se o EBIT por ação não é zero.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

def evaluate_evebitda(evebitda):
    '''
    Avalia o EV/EBITDA com base em faixas definidas para o mercado brasileiro:
    - EV/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
    - 0 ≤ EV/EBITDA ≤ 4: Ótimo (subvalorizado, oportunidade de compra)
    - 4 < EV/EBITDA ≤ 7: Moderado (valuation justo, crescimento moderado)
    - 7 < EV/EBITDA ≤ 10: Ruim (sobrevalorizado, cautela necessária)
    - 10 < EV/EBITDA ≤ 15: Péssimo (muito caro, alto risco)
    - EV/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado, risco elevado)
    '''
    definicao = '''
    Indicador que relaciona o valor da empresa (valor de mercado + dívida líquida) ao EBITDA,
    avaliando a capacidade de geração de caixa em relação ao valor total da companhia. É útil
    para comparar empresas com diferentes estruturas de capital.
    '''
    agrupador = 'Valuation'
    formula = 'EV/EBITDA = (Valor de Mercado + Dívida Líquida) / EBITDA'

    try:
        if evebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'EV/EBITDA < 0',
                'descricao': '''
                EV/EBITDA negativo indica EBITDA negativo, sugerindo problemas operacionais graves.
                Comum em empresas em crise ou setores cíclicos (ex.: mineração como CSNA3). Exige
                análise de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= evebitda <= 4:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= EV/EBITDA <= 4',
                'descricao': '''
                EV/EBITDA baixo sugere subvalorização, indicando oportunidade de compra. Comum em
                setores com ativos pesados (ex.: mineração como VALE3). Confirme com análise de
                endividamento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < evebitda <= 7:
            return {
                'classificacao': 'Moderado',
                'faixa': '4 < EV/EBITDA <= 7',
                'descricao': '''
                EV/EBITDA indica valuation justo, típico de empresas com geração de caixa estável
                (ex.: utilities como ELET3). Equilíbrio entre risco e retorno.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 7 < evebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '7 < EV/EBITDA <= 10',
                'descricao': '''
                EV/EBITDA elevado sugere sobrevalorização moderada, comum em setores de crescimento
                (ex.: consumo como ABEV3). Exige análise de crescimento futuro.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < evebitda <= 15:
            return {
                'classificacao': 'Péssimo',
                'faixa': '10 < EV/EBITDA <= 15',
                'descricao': '''
                EV/EBITDA muito alto indica empresa cara, com expectativas de crescimento elevadas.
                Risco de correção em setores como tecnologia (ex.: TOTS3).
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # evebitda > 15
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'EV/EBITDA > 15',
                'descricao': '''
                EV/EBITDA extremamente elevado sugere sobrevalorização severa, típica de empresas
                especulativas (ex.: startups como NUBR33). Análise detalhada é essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar EV/EBITDA: {str(e)}. Verifique se o valor fornecido é um número
            válido e se o EBITDA não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_pl_ativos(pl_ativos):
    '''
    Avalia o Patrimônio Líquido/Ativos com base em faixas definidas:
    - PL/Ativos < 0: Crítico (patrimônio negativo, risco elevado)
    - 0 ≤ PL/Ativos ≤ 0.1: Péssimo (alta alavancagem)
    - 0.1 < PL/Ativos ≤ 0.3: Ruim (alavancagem moderada)
    - 0.3 < PL/Ativos ≤ 0.5: Moderado (estrutura equilibrada)
    - 0.5 < PL/Ativos ≤ 0.7: Ótimo (patrimônio sólido)
    - PL/Ativos > 0.7: Fora da faixa (pouco endividamento)
    '''
    definicao = '''
    Indicador que mede a proporção do patrimônio líquido em relação aos ativos totais, avaliando
    o grau de alavancagem financeira da empresa. Um valor alto indica baixa dependência de dívidas,
    enquanto um valor baixo sugere maior alavancagem.
    '''
    agrupador = 'Estrutura de Capital'
    formula = 'PL/Ativos = Patrimônio Líquido / Ativos Totais'

    try:
        if pl_ativos < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'PL/Ativos < 0',
                'descricao': '''
                PL/Ativos negativo indica patrimônio líquido negativo, sugerindo insolvência. Comum
                em empresas em crise (ex.: Oi - OIBR3). Para investidores, é um alerta grave,
                exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pl_ativos <= 0.1:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= PL/Ativos <= 0.1',
                'descricao': '''
                PL/Ativos muito baixo sugere alta alavancagem, comum em bancos (ex.: Itaú - ITUB4).
                Risco financeiro elevado, requerendo atenção ao fluxo de caixa e endividamento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.1 < pl_ativos <= 0.3:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.1 < PL/Ativos <= 0.3',
                'descricao': '''
                PL/Ativos baixo indica alavancagem moderada, comum em utilities (ex.: Engie Brasil - EGIE3).
                Exige monitoramento da capacidade de pagamento de dívidas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < pl_ativos <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < PL/Ativos <= 0.5',
                'descricao': '''
                PL/Ativos equilibrado sugere estrutura financeira saudável, comum em indústrias
                (ex.: Suzano - SUZB3). Para investidores, indica equilíbrio entre risco e estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < pl_ativos <= 0.7:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0.5 < PL/Ativos <= 0.7',
                'descricao': '''
                PL/Ativos alto indica patrimônio sólido, comum em consumo (ex.: Ambev - ABEV3).
                Sinal de baixa alavancagem, atrativo para investidores conservadores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # pl_ativos > 0.7
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PL/Ativos > 0.7',
                'descricao': '''
                PL/Ativos extremamente alto sugere pouco endividamento, comum em tecnologia
                (ex.: Totvs - TOTS3). Pode indicar subvalorização, mas exige análise de eficiência
                no uso de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar PL/Ativos: {str(e)}. Verifique se o valor fornecido é um número
            válido e se os ativos totais não são zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_peg_ratio(peg):
    '''
    Avalia o PEG Ratio com base em faixas definidas:
    - PEG < 0: Crítico (crescimento negativo, risco elevado)
    - 0 ≤ PEG ≤ 0.5: Ótimo (subvalorizado com alto crescimento)
    - 0.5 < PEG ≤ 1: Moderado (valuation justo)
    - 1 < PEG ≤ 1.5: Ruim (sobrevalorizado, cautela necessária)
    - 1.5 < PEG ≤ 2: Péssimo (muito caro, alto risco)
    - PEG > 2: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    Indicador que relaciona o P/L com a taxa de crescimento esperada dos lucros, avaliando se
    o preço da ação é justificado pelo seu potencial de crescimento. Um PEG baixo sugere
    subvalorização em relação ao crescimento esperado.
    '''
    agrupador = 'Valuation'
    formula = 'PEG = (Preço/Lucro) / Crescimento Anual Esperado do Lucro (%)'

    try:
        if peg < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'PEG < 0',
                'descricao': '''
                PEG negativo indica crescimento esperado negativo ou P/L negativo, sugerindo
                problemas financeiros ou de mercado. Comum em empresas em crise (ex.: Oi - OIBR3).
                Para investidores, é um alerta grave, exigindo análise detalhada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= peg <= 0.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= PEG <= 0.5',
                'descricao': '''
                PEG baixo sugere subvalorização com alto potencial de crescimento, comum em
                tecnologia (ex.: Totvs - TOTS3). Oportunidade de compra para investidores focados
                em crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < peg <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < PEG <= 1',
                'descricao': '''
                PEG indica valuation justo, equilibrando preço e crescimento, comum em varejo
                (ex.: Magazine Luiza - MGLU3). Para investidores, sugere equilíbrio entre risco
                e retorno.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < peg <= 1.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < PEG <= 1.5',
                'descricao': '''
                PEG elevado sugere sobrevalorização moderada, indicando expectativas de crescimento
                moderadas. Comum em setores competitivos (ex.: consumo como LREN3). Exige análise
                de perspectivas futuras.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < peg <= 2:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1.5 < PEG <= 2',
                'descricao': '''
                PEG muito alto indica ação cara em relação ao crescimento, comum em setores
                especulativos (ex.: tecnologia como NUBR33). Risco de correção elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # peg > 2
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PEG > 2',
                'descricao': '''
                PEG extremamente elevado sugere sobrevalorização severa, típica de empresas
                especulativas (ex.: startups como NUBR33). Análise detalhada do crescimento é
                essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar PEG Ratio: {str(e)}. Verifique se o valor fornecido é um número
            válido e se o crescimento anual esperado do lucro não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_p_ativo(p_ativo):
    '''
    Avalia o Preço/Ativo Total com base em faixas definidas:
    - P/Ativo < 0: Crítico (impossível)
    - 0 ≤ P/Ativo ≤ 0.2: Ótimo (subvalorizado)
    - 0.2 < P/Ativo ≤ 0.5: Moderado (valuation justo)
    - 0.5 < P/Ativo ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/Ativo ≤ 1.5: Péssimo (muito caro)
    - P/Ativo > 1.5: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    Indicador que compara o preço da ação com os ativos totais por ação, avaliando se a empresa
    está sendo negociada acima ou abaixo do valor de seus ativos. É útil para identificar
    subvalorização em empresas com muitos ativos.
    '''
    agrupador = 'Valuation'
    formula = 'P/Ativo = Preço da Ação / Ativos Totais por Ação'

    try:
        if p_ativo < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/Ativo < 0',
                'descricao': '''
                P/Ativo negativo é impossível, indicando erro nos dados financeiros ou cálculo
                incorreto. Verifique os dados de preço da ação e ativos totais.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_ativo <= 0.2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/Ativo <= 0.2',
                'descricao': '''
                P/Ativo baixo sugere subvalorização, comum em mineração (ex.: Vale - VALE3).
                Oportunidade de compra para investidores focados em valor.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < p_ativo <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < P/Ativo <= 0.5',
                'descricao': '''
                P/Ativo indica valuation justo, típico de energia (ex.: Eletrobras - ELET3).
                Equilíbrio entre risco e retorno para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < p_ativo <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < P/Ativo <= 1',
                'descricao': '''
                P/Ativo elevado sugere sobrevalorização, comum em consumo (ex.: Ambev - ABEV3).
                Exige análise detalhada do valor dos ativos e perspectivas de crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < p_ativo <= 1.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1 < P/Ativo <= 1.5',
                'descricao': '''
                P/Ativo muito alto indica ação cara, comum em tecnologia (ex.: Totvs - TOTS3).
                Risco de correção elevado, exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # p_ativo > 1.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/Ativo > 1.5',
                'descricao': '''
                P/Ativo extremamente elevado sugere sobrevalorização severa, indicando alto risco.
                Típico de empresas especulativas (ex.: Nubank - NUBR33). Análise detalhada é
                essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar P/Ativo: {str(e)}. Verifique se o valor fornecido é um número
            válido e se os ativos totais por ação não são zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_vpa(vpa_preco):
    '''
    Avalia o VPA/Preço com base em faixas definidas:
    - VPA/Preço < 0: Crítico (patrimônio negativo)
    - 0 ≤ VPA/Preço ≤ 0.5: Fora da faixa (sobrevalorizado)
    - 0.5 < VPA/Preço ≤ 0.8: Péssimo (muito caro)
    - 0.8 < VPA/Preço ≤ 1: Ruim (sobrevalorizado)
    - 1 < VPA/Preço ≤ 1.5: Moderado (valuation justo)
    - VPA/Preço > 1.5: Ótimo (subvalorizado)
    '''
    definicao = '''
    Indicador que compara o valor patrimonial por ação com o preço da ação, avaliando se a
    empresa está subvalorizada ou sobrevalorizada em relação ao seu patrimônio líquido. Um valor
    alto sugere subvalorização.
    '''
    agrupador = 'Valuation'
    formula = 'VPA/Preço = Valor Patrimonial por Ação / Preço da Ação'

    try:
        if vpa_preco < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'VPA/Preço < 0',
                'descricao': '''
                VPA/Preço negativo indica patrimônio líquido negativo, sugerindo insolvência.
                Comum em empresas em crise (ex.: Oi - OIBR3). Para investidores, é um alerta grave,
                exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= vpa_preco <= 0.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': '0 <= VPA/Preço <= 0.5',
                'descricao': '''
                VPA/Preço muito baixo indica sobrevalorização severa, comum em tecnologia
                (ex.: Totvs - TOTS3). Para investidores, sugere risco elevado de correção.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < vpa_preco <= 0.8:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0.5 < VPA/Preço <= 0.8',
                'descricao': '''
                VPA/Preço baixo sugere ação cara, comum em varejo (ex.: Magazine Luiza - MGLU3).
                Exige cautela e análise de outros indicadores de valuation.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.8 < vpa_preco <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.8 < VPA/Preço <= 1',
                'descricao': '''
                VPA/Preço indica sobrevalorização moderada, comum em consumo (ex.: Ambev - ABEV3).
                Para investidores, sugere necessidade de análise de crescimento e rentabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < vpa_preco <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < VPA/Preço <= 1.5',
                'descricao': '''
                VPA/Preço indica valuation justo, típico de indústrias (ex.: Suzano - SUZB3).
                Equilíbrio entre risco e retorno para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # vpa_preco > 1.5
            return {
                'classificacao': 'Ótimo',
                'faixa': 'VPA/Preço > 1.5',
                'descricao': '''
                VPA/Preço alto sugere subvalorização, comum em setores maduros (ex.: bancos como
                Bradesco - BBDC4). Oportunidade de compra para investidores focados em valor.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar VPA/Preço: {str(e)}. Verifique se o valor fornecido é um número
            válido e se o preço da ação não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula

        }

def evaluate_lpa(lpa):
    '''
    Avalia o Lucro por Ação (LPA) com base em faixas definidas:
    - LPA < 0: Crítico (prejuízo)
    - 0 ≤ LPA ≤ 0.2: Péssimo (lucro muito baixo)
    - 0.2 < LPA ≤ 0.5: Ruim (lucro limitado)
    - 0.5 < LPA ≤ 1: Moderado (lucro adequado)
    - 1 < LPA ≤ 2: Ótimo (lucro alto)
    - LPA > 2: Fora da faixa (lucro excepcional)
    '''
    definicao = '''
    Indicador que mede o lucro líquido por ação, refletindo a lucratividade da empresa por ação
    emitida. É útil para avaliar a capacidade da empresa de gerar retorno aos acionistas.
    '''
    agrupador = 'Lucratividade'
    formula = 'LPA = Lucro Líquido / Número de Ações'

    try:
        if lpa < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'LPA < 0',
                'descricao': '''
                LPA negativo indica prejuízo por ação, sugerindo problemas financeiros. Comum em
                empresas em crise (ex.: Oi - OIBR3). Para investidores, é um alerta grave, exigindo
                análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= lpa <= 0.2:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= LPA <= 0.2',
                'descricao': '''
                LPA muito baixo sugere lucratividade insuficiente, comum em empresas em crise ou com
                margens apertadas (ex.: varejo como PCAR3). Para investidores, indica alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < lpa <= 0.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 < LPA <= 0.5',
                'descricao': '''
                LPA limitado indica lucratividade moderada, comum em setores cíclicos (ex.: Gerdau - GGBR4).
                Para investidores, sugere necessidade de monitoramento de tendências de lucro.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < lpa <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < LPA <= 1',
                'descricao': '''
                LPA adequado sugere lucratividade equilibrada, comum em consumo (ex.: Ambev - ABEV3).
                Para investidores, indica equilíbrio entre risco e retorno.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < lpa <= 2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < LPA <= 2',
                'descricao': '''
                LPA alto indica forte lucratividade, comum em tecnologia (ex.: Totvs - TOTS3).
                Oportunidade atrativa para investidores focados em crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # lpa > 2
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'LPA > 2',
                'descricao': '''
                LPA extremamente alto sugere lucratividade excepcional, comum em empresas líderes
                (ex.: Vale - VALE3). Para investidores, é atrativo, mas exige análise de
                sustentabilidade dos lucros.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar LPA: {str(e)}. Verifique se o valor fornecido é um número válido
            e se o número de ações não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_passivos_ativos(passivos_ativos):
    '''
    Avalia o Passivos/Ativos com base em faixas definidas:
    - Passivos/Ativos < 0: Crítico (impossível)
    - 0 ≤ Passivos/Ativos ≤ 0.3: Ótimo (baixo endividamento)
    - 0.3 < Passivos/Ativos ≤ 0.5: Moderado (endividamento controlado)
    - 0.5 < Passivos/Ativos ≤ 0.7: Ruim (endividamento moderado)
    - 0.7 < Passivos/Ativos ≤ 0.9: Péssimo (endividamento alto)
    - Passivos/Ativos > 0.9: Fora da faixa (endividamento excessivo)
    '''
    definicao = '''
    Indicador que mede a proporção dos passivos totais em relação aos ativos totais, avaliando
    o nível de endividamento da empresa. Um valor alto indica maior dependência de dívidas,
    enquanto um valor baixo sugere maior solidez financeira.
    '''
    agrupador = 'Endividamento'
    formula = 'Passivos/Ativos = Passivos Totais / Ativos Totais'

    try:
        if passivos_ativos < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Passivos/Ativos < 0',
                'descricao': '''
                Passivos/Ativos negativo é impossível, indicando erro nos dados financeiros ou
                cálculo incorreto. Verifique os dados de passivos e ativos totais.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= passivos_ativos <= 0.3:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Passivos/Ativos <= 0.3',
                'descricao': '''
                Passivos/Ativos baixo indica baixo endividamento, comum em tecnologia
                (ex.: Totvs - TOTS3). Sinal de saúde financeira, atrativo para investidores
                conservadores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < passivos_ativos <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < Passivos/Ativos <= 0.5',
                'descricao': '''
                Passivos/Ativos moderado sugere endividamento controlado, comum em consumo
                (ex.: Ambev - ABEV3). Para investidores, indica equilíbrio entre risco e estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < passivos_ativos <= 0.7:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < Passivos/Ativos <= 0.7',
                'descricao': '''
                Passivos/Ativos elevado indica endividamento moderado, comum em indústrias
                (ex.: Suzano - SUZB3). Exige monitoramento da capacidade de pagamento de dívidas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.7 < passivos_ativos <= 0.9:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0.7 < Passivos/Ativos <= 0.9',
                'descricao': '''
                Passivos/Ativos alto sugere endividamento elevado, comum em utilities
                (ex.: Engie Brasil - EGIE3). Risco financeiro elevado, requer atenção ao fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # passivos_ativos > 0.9
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Passivos/Ativos > 0.9',
                'descricao': '''
                Passivos/Ativos extremamente alto indica endividamento excessivo, comum em bancos
                (ex.: Itaú - ITUB4). Alto risco para investidores, exige análise detalhada de solvência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Passivos/Ativos: {str(e)}. Verifique se o valor fornecido é um número
            válido e se os ativos totais não são zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_psr(psr):
    '''
    Avalia o Preço/Receita (P/SR) com base em faixas definidas:
    - P/SR < 0: Crítico (receita negativa)
    - 0 ≤ P/SR ≤ 0.3: Ótimo (subvalorizado)
    - 0.3 < P/SR ≤ 0.8: Moderado (valuation justo)
    - 0.8 < P/SR ≤ 1.5: Ruim (sobrevalorizado)
    - 1.5 < P/SR ≤ 2.5: Péssimo (muito caro)
    - P/SR > 2.5: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    Indicador que relaciona o preço da ação à receita líquida por ação, avaliando o valor de
    mercado em relação às vendas. É útil para empresas com lucros baixos ou negativos.
    '''
    agrupador = 'Valuation'
    formula = 'P/SR = Preço da Ação / Receita Líquida por Ação'

    try:
        if psr < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/SR < 0',
                'descricao': '''
                P/SR negativo indica receita negativa, sugerindo graves problemas operacionais.
                Comum em empresas em crise (ex.: Oi - OIBR3). Para investidores, é um alerta grave,
                exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= psr <= 0.3:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/SR <= 0.3',
                'descricao': '''
                P/SR baixo sugere subvalorização, comum em mineração (ex.: Vale - VALE3).
                Oportunidade de compra para investidores focados em valor.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < psr <= 0.8:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < P/SR <= 0.8',
                'descricao': '''
                P/SR indica valuation justo, típico de energia (ex.: Eletrobras - ELET3).
                Equilíbrio entre risco e retorno para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.8 < psr <= 1.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.8 < P/SR <= 1.5',
                'descricao': '''
                P/SR elevado sugere sobrevalorização, comum em consumo (ex.: Ambev - ABEV3).
                Exige análise detalhada de margens e crescimento de receita.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < psr <= 2.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1.5 < P/SR <= 2.5',
                'descricao': '''
                P/SR muito alto indica ação cara, comum em tecnologia (ex.: Totvs - TOTS3).
                Risco de correção elevado, exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # psr > 2.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/SR > 2.5',
                'descricao': '''
                P/SR extremamente elevado sugere sobrevalorização severa, indicando alto risco.
                Típico de empresas especulativas (ex.: Nubank - NUBR33). Análise detalhada é
                essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar P/SR: {str(e)}. Verifique se o valor fornecido é um número válido
            e se a receita líquida por ação não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_p_ativo_circ_liq(p_acl):
    '''
    Avalia o Preço/Ativo Circulante Líquido com base em faixas definidas:
    - P/ACL < 0: Crítico (ativo circulante líquido negativo)
    - 0 ≤ P/ACL ≤ 0.2: Ótimo (subvalorizado)
    - 0.2 < P/ACL ≤ 0.5: Moderado (valuation justo)
    - 0.5 < P/ACL ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/ACL ≤ 1.5: Péssimo (muito caro)
    - P/ACL > 1.5: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    Indicador que compara o preço da ação com o ativo circulante líquido por ação (ativo circulante
    menos passivo circulante), avaliando a liquidez imediata da empresa em relação ao seu valor
    de mercado.
    '''
    agrupador = 'Valuation'
    formula = 'P/ACL = Preço da Ação / (Ativo Circulante - Passivo Circulante) por Ação'

    try:
        if p_acl < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/ACL < 0',
                'descricao': '''
                P/ACL negativo indica ativo circulante líquido negativo, sugerindo problemas de
                liquidez ou passivo circulante maior que ativo circulante (ex.: Oi - OIBR3). Para
                investidores, é um alerta grave, exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_acl <= 0.2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/ACL <= 0.2',
                'descricao': '''
                P/ACL baixo sugere subvalorização em relação à liquidez, comum em mineração
                (ex.: Vale - VALE3). Oportunidade de compra, especialmente em setores com ativos
                circulantes robustos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < p_acl <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < P/ACL <= 0.5',
                'descricao': '''
                P/ACL indica valuation justo, comum em energia (ex.: Eletrobras - ELET3).
                Oferece equilíbrio entre risco e retorno para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < p_acl <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < P/ACL <= 1',
                'descricao': '''
                P/ACL elevado sugere sobrevalorização, comum em consumo (ex.: Ambev - ABEV3).
                Exige análise detalhada de liquidez e endividamento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < p_acl <= 1.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1 < P/ACL <= 1.5',
                'descricao': '''
                P/ACL muito alto indica ação cara, comum em tecnologia (ex.: Totvs - TOTS3).
                Risco de correção elevado devido a expectativas de mercado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # p_acl > 1.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/ACL > 1.5',
                'descricao': '''
                P/ACL extremamente elevado sugere sobrevalorização severa, típica de empresas
                especulativas ou com baixa liquidez relativa (ex.: Weg - WEGE3). Análise detalhada
                é essencial.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar P/ACL: {str(e)}. Verifique se o valor fornecido é um número válido
            e se o ativo circulante líquido por ação não é zero.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_disponibilidade(disponibilidade):
    '''
    Avalia a Disponibilidade (caixa e equivalentes, em R$ bilhões):
    - Disponibilidade < 0: Crítico
    - 0 ≤ Disponibilidade ≤ 0.05: Péssimo
    - 0.05 < Disponibilidade ≤ 0.2: Ruim
    - 0.2 < Disponibilidade ≤ 1: Moderado
    - 1 < Disponibilidade ≤ 10: Ótimo
    - Disponibilidade > 10: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa o caixa e equivalentes de caixa da empresa, refletindo a liquidez
    imediata disponível para cobrir obrigações ou investir.
    '''
    agrupador = 'Liquidez'
    formula = 'Disponibilidade = Caixa + Equivalentes de Caixa'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(disponibilidade, str):
            # Remove "R$" e espaços
            disponibilidade = disponibilidade.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            disponibilidade = disponibilidade.replace('.', '').replace(',', '.')
            disponibilidade = float(disponibilidade) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            disponibilidade = float(disponibilidade) / 1_000_000_000 if disponibilidade >= 1_000_000 else float(
                disponibilidade)

        if disponibilidade < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Disponibilidade < 0',
                'descricao': '''
                Disponibilidade negativa é impossível, indicando erro nos dados financeiros ou
                cálculo incorreto. Verifique os dados de caixa e equivalentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= disponibilidade <= 0.05:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= Disponibilidade <= 0.05',
                'descricao': '''
                Caixa muito baixo indica alto risco de liquidez, comum em empresas em crise
                (ex.: Oi - OIBR3). Para investidores, sugere dificuldades em cumprir obrigações
                de curto prazo.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.05 < disponibilidade <= 0.2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.05 < Disponibilidade <= 0.2',
                'descricao': '''
                Caixa limitado indica liquidez restrita, comum em small caps (ex.: Enauta - ENAT3).
                Exige monitoramento da gestão de caixa para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < disponibilidade <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < Disponibilidade <= 1',
                'descricao': '''
                Caixa adequado sugere liquidez equilibrada, típico de mid caps (ex.: Ambev - ABEV3).
                Oferece segurança moderada para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < disponibilidade <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Disponibilidade <= 10',
                'descricao': '''
                Caixa robusto indica forte liquidez, comum em large caps (ex.: Itaú - ITUB4).
                Atraente para investidores que priorizam segurança financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # disponibilidade > 10
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Disponibilidade > 10',
                'descricao': '''
                Caixa excepcional sugere liquidez extremamente alta, típico de blue chips
                (ex.: Vale - VALE3). Para investidores, indica forte capacidade de investimento ou
                distribuição de dividendos, mas exige análise de eficiência no uso do caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Disponibilidade: {str(e)}. Verifique se o valor é um número válido
            ou está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_patrimonio_liquido(pl):
    '''
    Avalia o Patrimônio Líquido (em R$ bilhões):
    - PL < 0: Crítico
    - 0 ≤ PL ≤ 0.5: Péssimo
    - 0.5 < PL ≤ 2: Ruim
    - 2 < PL ≤ 10: Moderado
    - 10 < PL ≤ 50: Ótimo
    - PL > 50: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa o valor contábil da empresa pertencente aos acionistas, calculado
    como ativos totais menos passivos totais. Valores altos indicam maior solidez financeira.
    '''
    agrupador = 'Estrutura de Capital'
    formula = 'PL = Ativos Totais - Passivos Totais'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(pl, str):
            # Remove "R$" e espaços
            pl = pl.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            pl = pl.replace('.', '').replace(',', '.')
            pl = float(pl) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            pl = float(pl) / 1_000_000_000 if pl >= 1_000_000 else float(pl)

        if pl < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'PL < 0',
                'descricao': '''
                Patrimônio líquido negativo indica que os passivos superam os ativos, sugerindo
                alto risco financeiro. Comum em empresas em crise (ex.: Oi - OIBR3). Para
                investidores, é um alerta grave, exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pl <= 0.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= PL <= 0.5',
                'descricao': '''
                Patrimônio muito baixo indica fragilidade financeira, típico de small caps
                (ex.: Enauta - ENAT3). Para investidores, sugere alto risco e necessidade de
                monitoramento de endividamento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < pl <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < PL <= 2',
                'descricao': '''
                Patrimônio limitado sugere estrutura financeira modesta, comum em empresas menores
                (ex.: Cyrela - CYRE3). Para investidores, indica necessidade de avaliar crescimento
                e solvência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < pl <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '2 < PL <= 10',
                'descricao': '''
                Patrimônio sólido indica estrutura financeira equilibrada, típico de mid caps
                (ex.: Ambev - ABEV3). Oferece segurança moderada para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < pl <= 50:
            return {
                'classificacao': 'Ótimo',
                'faixa': '10 < PL <= 50',
                'descricao': '''
                Patrimônio robusto sugere forte solidez financeira, comum em large caps
                (ex.: Itaú - ITUB4). Atraente para investidores que priorizam estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # pl > 50
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PL > 50',
                'descricao': '''
                Patrimônio excepcional indica altíssima solidez financeira, típico de blue chips
                (ex.: Vale - VALE3). Para investidores, sugere forte capacidade de resistência a
                crises, mas exige análise de eficiência no uso do capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Patrimônio Líquido: {str(e)}. Verifique se o valor é um número
            válido ou está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_divida_bruta(divida_bruta):
    '''
    Avalia a Dívida Bruta (em R$ bilhões):
    - Dívida Bruta < 0: Crítico
    - 0 ≤ Dívida Bruta ≤ 0.5: Ótimo
    - 0.5 < Dívida Bruta ≤ 2: Moderado
    - 2 < Dívida Bruta ≤ 10: Ruim
    - 10 < Dívida Bruta ≤ 20: Péssimo
    - Dívida Bruta > 20: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa o total de obrigações financeiras da empresa, incluindo empréstimos
    e financiamentos de curto e longo prazo.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Bruta = Total de Empréstimos e Financiamentos'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(divida_bruta, str):
            # Remove "R$" e espaços
            divida_bruta = divida_bruta.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            divida_bruta = divida_bruta.replace('.', '').replace(',', '.')
            divida_bruta = float(divida_bruta) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            divida_bruta = float(divida_bruta) / 1_000_000_000 if divida_bruta >= 1_000_000 else float(divida_bruta)

        if divida_bruta < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Bruta < 0',
                'descricao': '''
                Dívida bruta negativa é impossível, indicando erro nos dados financeiros ou cálculo
                incorreto. Verifique os dados de empréstimos e financiamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_bruta <= 0.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Bruta <= 0.5',
                'descricao': '''
                Dívida bruta muito baixa indica baixo risco financeiro, comum em empresas com pouca
                alavancagem (ex.: Totvs - TOTS3). Atraente para investidores que priorizam segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < divida_bruta <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Dívida Bruta <= 2',
                'descricao': '''
                Dívida bruta controlada sugere equilíbrio financeiro, típico de mid caps
                (ex.: Ambev - ABEV3). Oferece risco moderado para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_bruta <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida Bruta <= 10',
                'descricao': '''
                Dívida bruta moderada indica maior dependência de financiamentos, comum em indústrias
                (ex.: Suzano - SUZB3). Exige atenção à capacidade de pagamento para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < divida_bruta <= 20:
            return {
                'classificacao': 'Péssimo',
                'faixa': '10 < Dívida Bruta <= 20',
                'descricao': '''
                Dívida bruta alta sugere risco financeiro elevado, comum em utilities
                (ex.: Engie Brasil - EGIE3). Para investidores, requer análise detalhada de fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # divida_bruta > 20
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Bruta > 20',
                'descricao': '''
                Dívida bruta excessiva indica alta alavancagem, típico de empresas intensivas em
                capital (ex.: Vale - VALE3). Para investidores, é de alto risco, exigindo análise
                da sustentabilidade da dívida.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Dívida Bruta: {str(e)}. Verifique se o valor é um número válido ou
            está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_divida_liquida(divida_liquida):
    '''
    Avalia a Dívida Líquida (em R$ bilhões):
    - Dívida Líquida ≤ -0.5: Ótimo
    - -0.5 < Dívida Líquida ≤ 0: Moderado
    - 0 < Dívida Líquida ≤ 2: Ruim
    - 2 < Dívida Líquida ≤ 10: Péssimo
    - Dívida Líquida > 10: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa a dívida bruta da empresa menos seu caixa e equivalentes, refletindo
    o endividamento real. Valores negativos indicam mais caixa que dívidas.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida = Dívida Bruta - Caixa e Equivalentes'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(divida_liquida, str):
            # Remove "R$" e espaços
            divida_liquida = divida_liquida.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            divida_liquida = divida_liquida.replace('.', '').replace(',', '.')
            divida_liquida = float(divida_liquida) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            divida_liquida = float(divida_liquida) / 1_000_000_000 if abs(divida_liquida) >= 1_000_000 else float(
                divida_liquida)

        if divida_liquida <= -0.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': 'Dívida Líquida <= -0.5',
                'descricao': '''
                Dívida líquida negativa (caixa líquido) indica excelente saúde financeira, com mais
                caixa que dívidas. Comum em empresas com baixa alavancagem (ex.: Totvs - TOTS3).
                Atraente para investidores que priorizam segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif -0.5 < divida_liquida <= 0:
            return {
                'classificacao': 'Moderado',
                'faixa': '-0.5 < Dívida Líquida <= 0',
                'descricao': '''
                Dívida líquida próxima de zero sugere situação financeira equilibrada, com dívidas
                compensadas pelo caixa. Comum em empresas estáveis (ex.: Ambev - ABEV3). Oferece
                risco moderado para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 < divida_liquida <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0 < Dívida Líquida <= 2',
                'descricao': '''
                Dívida líquida moderada indica dependência de financiamentos, exigindo atenção.
                Comum em empresas de porte médio (ex.: Cyrela - CYRE3). Para investidores, sugere
                análise da capacidade de geração de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_liquida <= 10:
            return {
                'classificacao': 'Péssimo',
                'faixa': '2 < Dívida Líquida <= 10',
                'descricao': '''
                Dívida líquida alta reflete risco financeiro elevado, comum em indústrias intensivas
                em capital (ex.: Suzano - SUZB3). Para investidores, exige cautela e análise detalhada
                de fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # divida_liquida > 10
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Líquida > 10',
                'descricao': '''
                Dívida líquida excessiva indica alto risco financeiro, típico de empresas altamente
                alavancadas (ex.: Vale - VALE3). Para investidores, é essencial avaliar a
                sustentabilidade da dívida e a geração de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Dívida Líquida: {str(e)}. Verifique se o valor é um número válido
            ou está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_ativos(ativos):
    '''
    Avalia os Ativos Totais (em R$ bilhões):
    - Ativos < 0: Crítico
    - 0 ≤ Ativos ≤ 1: Péssimo
    - 1 < Ativos ≤ 5: Ruim
    - 5 < Ativos ≤ 20: Moderado
    - 20 < Ativos ≤ 100: Ótimo
    - Ativos > 100: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).
    '''
    definicao = '''
    Indicador que representa o total de ativos da empresa, incluindo circulantes e não circulantes.
    Valores altos indicam maior porte e capacidade de investimento.
    '''
    agrupador = 'Estrutura de Capital'
    formula = 'Ativos = Ativo Circulante + Ativo Não Circulante'

    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(ativos, str):
            # Remove "R$" e espaços
            ativos = ativos.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            ativos = ativos.replace('.', '').replace(',', '.')
            ativos = float(ativos) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            ativos = float(ativos) / 1_000_000_000 if ativos >= 1_000_000 else float(ativos)

        if ativos < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Ativos < 0',
                'descricao': '''
                Ativos negativos são impossíveis, indicando erro nos dados financeiros ou cálculo
                incorreto. Verifique os dados de ativos circulantes e não circulantes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= ativos <= 1:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0 <= Ativos <= 1',
                'descricao': '''
                Ativos muito baixos indicam porte financeiro limitado, típico de small caps
                (ex.: Enauta - ENAT3). Para investidores, sugere alto risco e baixa capacidade de
                investimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < ativos <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < Ativos <= 5',
                'descricao': '''
                Ativos limitados sugerem estrutura financeira modesta, comum em empresas menores
                (ex.: Cyrela - CYRE3). Para investidores, indica necessidade de avaliar crescimento
                e solvência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < ativos <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < Ativos <= 20',
                'descricao': '''
                Ativos sólidos indicam estrutura financeira equilibrada, típico de mid caps
                (ex.: Ambev - ABEV3). Oferece segurança moderada para investidores.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < ativos <= 100:
            return {
                'classificacao': 'Ótimo',
                'faixa': '20 < Ativos <= 100',
                'descricao': '''
                Ativos robustos sugerem forte solidez financeira, comum em large caps
                (ex.: Itaú - ITUB4). Atraente para investidores que priorizam estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # ativos > 100
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Ativos > 100',
                'descricao': '''
                Ativos excepcionais indicam altíssimo porte financeiro, típico de blue chips
                (ex.: Vale - VALE3). Para investidores, sugere forte capacidade de investimento,
                mas exige análise de eficiência no uso do capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Erro ao processar Ativos: {str(e)}. Verifique se o valor é um número válido ou
            está no formato correto (ex.: R$ 112.714.000).
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }
    """
    analisefundamentalista_10.py
    Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
    e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
    Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
    Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
    Indicador incluído: Ativo Circulante.
    """

    def evaluate_ativo_circulante(ativo_circulante):
        '''
        Avalia o Ativo Circulante (em R$ bilhões):
        - Ativo Circulante < 0: Crítico
        - 0 ≤ Ativo Circulante ≤ 0.2: Péssimo
        - 0.2 < Ativo Circulante ≤ 1: Ruim
        - 1 < Ativo Circulante ≤ 5: Moderado
        - 5 < Ativo Circulante ≤ 20: Ótimo
        - Ativo Circulante > 20: Fora da faixa
        Aceita valores no formato R$ 112.714.000 (converte para bilhões).
        '''
        definicao = '''
        Indicador que representa os ativos de curto prazo da empresa, como caixa, contas a receber
        e estoques, disponíveis para cobrir obrigações de curto prazo.
        '''
        agrupador = 'Liquidez'
        formula = 'Ativo Circulante = Caixa + Contas a Receber + Estoques + Outros Ativos de Curto Prazo'

        try:
            # Se for string, processar formato monetário brasileiro
            if isinstance(ativo_circulante, str):
                # Remove "R$" e espaços
                ativo_circulante = ativo_circulante.replace('R$', '').replace(' ', '')
                # Substitui ponto (milhares) e vírgula (decimal)
                ativo_circulante = ativo_circulante.replace('.', '').replace(',', '.')
                ativo_circulante = float(ativo_circulante) / 1_000_000_000  # Converte para bilhões
            else:
                # Garante que é float
                ativo_circulante = float(ativo_circulante) / 1_000_000_000 if ativo_circulante >= 1_000_000 else float(
                    ativo_circulante)

            if ativo_circulante < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Ativo Circulante < 0',
                    'descricao': '''
                    Ativo circulante negativo é impossível, indicando erro nos dados financeiros ou
                    cálculo incorreto. Verifique os dados de caixa, contas a receber e estoques.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= ativo_circulante <= 0.2:
                return {
                    'classificacao': 'Péssimo',
                    'faixa': '0 <= Ativo Circulante <= 0.2',
                    'descricao': '''
                    Ativo circulante muito baixo indica alto risco de liquidez, comum em empresas em
                    crise (ex.: Oi - OIBR3). Para investidores, sugere dificuldades em cumprir obrigações
                    de curto prazo.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0.2 < ativo_circulante <= 1:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0.2 < Ativo Circulante <= 1',
                    'descricao': '''
                    Ativo circulante limitado sugere liquidez restrita, comum em small caps
                    (ex.: Enauta - ENAT3). Exige monitoramento da gestão de caixa para investidores.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 1 < ativo_circulante <= 5:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '1 < Ativo Circulante <= 5',
                    'descricao': '''
                    Ativo circulante adequado sugere liquidez equilibrada, típico de mid caps
                    (ex.: Ambev - ABEV3). Oferece segurança moderada para investidores.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < ativo_circulante <= 20:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '5 < Ativo Circulante <= 20',
                    'descricao': '''
                    Ativo circulante robusto indica forte liquidez, comum em large caps
                    (ex.: Itaú - ITUB4). Atraente para investidores que priorizam segurança financeira.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            else:  # ativo_circulante > 20
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Ativo Circulante > 20',
                    'descricao': '''
                    Ativo circulante excepcional sugere liquidez extremamente alta, típico de blue chips
                    (ex.: Vale - VALE3). Para investidores, indica forte capacidade de cumprir obrigações
                    de curto prazo, mas exige análise de eficiência no uso do capital.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Erro ao processar Ativo Circulante: {str(e)}. Verifique se o valor é um número válido
                ou está no formato correto (ex.: R$ 112.714.000).
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

def evaluate_liquidez_media_diaria(liquidez):
    '''Avalia a Liquidez Média Diária (em R$ milhões):
    - Liquidez < 0: Crítico
    - 0 ≤ Liquidez ≤ 0.5: Péssimo
    - 0.5 < Liquidez ≤ 5: Ruim
    - 5 < Liquidez ≤ 20: Moderado
    - 20 < Liquidez ≤ 100: Ótimo
    - Liquidez > 100: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para milhões).'''
    definicao = '''Indicador que mede o volume médio diário de negociação da ação, refletindo a facilidade de compra e venda no mercado. Valores altos indicam maior liquidez e menor risco de negociação.'''
    agrupador = 'Liquidez'
    formula = 'Liquidez Média Diária = Volume Médio Diário de Negociação (em R$)'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(liquidez, str):
            # Remove "R$" e espaços
            liquidez = liquidez.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            liquidez = liquidez.replace('.', '').replace(',', '.')
            liquidez = float(liquidez) / 1_000_000  # Converte para milhões
        else:
            # Garante que é float
            liquidez = float(liquidez) / 1_000_000 if liquidez >= 1_000_000 else float(liquidez)

        if liquidez < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Liquidez < 0',
                'descricao': 'Liquidez média diária negativa, erro nos dados.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= liquidez <= 0.5:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= Liquidez <= 0.5',
                'descricao': 'Liquidez muito baixa, ação ilíquida, risco elevado (ex.: small caps pouco negociadas).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < liquidez <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < Liquidez <= 5',
                'descricao': 'Liquidez limitada, comum em small caps (ex.: ENAT3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < liquidez <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < Liquidez <= 20',
                'descricao': 'Liquidez adequada, típica de mid caps (ex.: ABEV3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < liquidez <= 100:
            return {
                'classificacao': 'Otimo',
                'faixa': '20 < Liquidez <= 100',
                'descricao': 'Liquidez robusta, comum em large caps (ex.: ITUB4).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Liquidez > 100',
                'descricao': 'Liquidez excepcional, típica de blue chips (ex.: VALE3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Liquidez Média Diária: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_ativo_circulante(ativo_circulante):
    '''Avalia o Ativo Circulante (em R$ bilhões):
    - Ativo Circulante < 0: Crítico
    - 0 ≤ Ativo Circulante ≤ 0.2: Péssimo
    - 0.2 < Ativo Circulante ≤ 1: Ruim
    - 1 < Ativo Circulante ≤ 5: Moderado
    - 5 < Ativo Circulante ≤ 20: Ótimo
    - Ativo Circulante > 20: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).'''
    definicao = '''Indicador que representa os ativos de curto prazo da empresa, como caixa, contas a receber e estoques, disponíveis para cobrir obrigações de curto prazo.'''
    agrupador = 'Liquidez'
    formula = 'Ativo Circulante = Caixa + Contas a Receber + Estoques + Outros Ativos de Curto Prazo'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(ativo_circulante, str):
            # Remove "R$" e espaços
            ativo_circulante = ativo_circulante.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            ativo_circulante = ativo_circulante.replace('.', '').replace(',', '.')
            ativo_circulante = float(ativo_circulante) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            ativo_circulante = float(ativo_circulante) / 1_000_000_000 if ativo_circulante >= 1_000_000 else float(ativo_circulante)

        if ativo_circulante < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Ativo Circulante < 0',
                'descricao': 'Ativo circulante negativo, erro nos dados.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= ativo_circulante <= 0.2:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= Ativo Circulante <= 0.2',
                'descricao': 'Ativo circulante muito baixo, risco de liquidez (ex.: OI).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < ativo_circulante <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 < Ativo Circulante <= 1',
                'descricao': 'Ativo circulante limitado, comum em small caps (ex.: ENAT3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < ativo_circulante <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Ativo Circulante <= 5',
                'descricao': 'Ativo circulante adequado, típico de mid caps (ex.: ABEV3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < ativo_circulante <= 20:
            return {
                'classificacao': 'Otimo',
                'faixa': '5 < Ativo Circulante <= 20',
                'descricao': 'Ativo circulante robusto, comum em large caps (ex.: ITUB4).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Ativo Circulante > 20',
                'descricao': 'Ativo circulante excepcional, típico de blue chips (ex.: VALE3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Ativo Circulante: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }