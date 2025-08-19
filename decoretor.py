# Define a classe ResultadoPVP para armazenar resultados da avaliação P/VP
class ResultadoPVP:
    # Construtor que inicializa os atributos do resultado da avaliação P/VP
    def __init__(self, classificacao, faixa, descricao, definicao, agrupador, formula, riscos, referencia_cruzada):
        # Atribui a classificação (ex.: "Ótimo", "Crítico") à variável de instância
        self.classificacao = classificacao
        # Atribui a faixa de P/VP (ex.: "0 <= P/VP <= 1") à variável de instância
        self.faixa = faixa
        # Atribui a descrição, removendo espaços em branco no início/fim
        self.descricao = descricao.strip()
        # Atribui a definição do P/VP, removendo espaços em branco
        self.definicao = definicao.strip()
        # Atribui a categoria de agrupamento (ex.: "Valuation")
        self.agrupador = agrupador
        # Atribui a fórmula do P/VP
        self.formula = formula
        # Atribui os riscos, removendo espaços em branco
        self.riscos = riscos.strip()
        # Atribui as referências cruzadas, removendo espaços em branco
        self.referencia_cruzada = referencia_cruzada.strip()

    # Define a representação em string do objeto para depuração/impressão
    def __repr__(self):
        # Retorna string formatada com classificação e faixa
        return f"<ResultadoPVP: {self.classificacao} | Faixa: {self.faixa}>"

    # Converte o objeto em dicionário para serialização
    def to_dict(self):
        # Retorna dicionário com todos os atributos da instância
        return {
            'classificacao': self.classificacao,
            'faixa': self.faixa,
            'descricao': self.descricao,
            'definicao': self.definicao,
            'agrupador': self.agrupador,
            'formula': self.formula,
            'riscos': self.riscos,
            'referencia_cruzada': self.referencia_cruzada
        }

# Define a classe PVPEvaluator para avaliar índices P/VP
class PVPEvaluator:
    # Construtor que inicializa definição, agrupador e fórmula do P/VP
    def __init__(self):
        # Define string multilinha explicando o índice P/VP
        self.definicao = '''
        O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado
        como (Preço da Ação / Valor Patrimonial por Ação). É um indicador de valuation que avalia se a
        ação está cara ou barata em relação aos ativos líquidos da empresa. Um P/VP baixo sugere
        subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
        '''
        # Define a categoria de agrupamento como "Valuation"
        self.agrupador = 'Valuation'
        # Define a fórmula do P/VP
        self.formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    # Decorator para validar que os parâmetros são strings não vazias
    def validar_strings(funcao):
        def wrapper(self, classificacao, faixa, descricao, riscos, referencia):
            # Verifica se cada parâmetro é uma string não vazia
            for param, nome in [
                (classificacao, "classificacao"),
                (faixa, "faixa"),
                (descricao, "descricao"),
                (riscos, "riscos"),
                (referencia, "referencia")
            ]:
                if not isinstance(param, str) or not param.strip():
                    raise ValueError(f"O parâmetro '{nome}' deve ser uma string não vazia.")
            # Chama a função original com os parâmetros validados
            return funcao(self, classificacao, faixa, descricao, riscos, referencia)
        return wrapper

    # Cria objeto ResultadoPVP com os parâmetros fornecidos
    @validar_strings
    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia):
        # Instancia e retorna ResultadoPVP com atributos da instância
        return ResultadoPVP(
            classificacao=classificacao,
            faixa=faixa,
            descricao=descricao,
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos=riscos,
            referencia_cruzada=referencia
        )

    # Avalia o valor P/VP e retorna um objeto ResultadoPVP
    def avaliar(self, p_vp):
        # Tenta processar o valor P/VP
        try:
            # Converte o P/VP para float para garantir que é numérico
            p_vp = float(p_vp)
            # Verifica se P/VP é negativo, indicando problemas críticos
            if p_vp < 0:
                # Retorna ResultadoPVP para P/VP negativo
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/VP < 0',
                    descricao='Valor negativo pode indicar distorções contábeis ou prejuízos acumulados.',
                    riscos='Alta probabilidade de falência ou diluição acionária em reestruturações.',
                    referencia='Avalie evaluate_debt_to_equity para saúde financeira, evaluate_cash_flow para geração de caixa e evaluate_peg_ratio para perspectivas de crescimento.'
                )
            # Verifica se P/VP está entre 0 e 1, indicando subvalorização
            elif 0 <= p_vp <= 1:
                # Retorna ResultadoPVP para ação subvalorizada
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/VP <= 1',
                    descricao='A ação está sendo negociada abaixo do valor patrimonial.',
                    riscos='Patrimônio pode incluir ativos obsoletos.',
                    referencia='Analise evaluate_vpa para valor patrimonial e evaluate_roe para rentabilidade.'
                )
            # Verifica se P/VP está entre 1 e 1.5, indicando valuation moderada
            elif 1 < p_vp <= 1.5:
                # Retorna ResultadoPVP para valuation moderada
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='1 < P/VP <= 1.5',
                    descricao='Preço próximo ao valor patrimonial, com leve prêmio.',
                    riscos='Estagnação em setores maduros.',
                    referencia='Compare com evaluate_p_l para lucros e evaluate_pl_ativos para estrutura.'
                )
            # Verifica se P/VP está entre 1.5 e 2, indicando sobrevalorização
            elif 1.5 < p_vp <= 2:
                # Retorna ResultadoPVP para ação sobrevalorizada
                return self.gerar_resultado(
                    classificacao='Ruim',
                    faixa='1.5 < P/VP <= 2',
                    descricao='Preço elevado em relação ao patrimônio.',
                    riscos='Expectativas não realizadas podem levar a correções.',
                    referencia='Verifique evaluate_peg_ratio para crescimento e evaluate_evebitda para valuation.'
                )
            # Verifica se P/VP está entre 2 e 3, indicando alta sobrevalorização
            elif 2 < p_vp <= 3:
                # Retorna ResultadoPVP para ação muito sobrevalorizada
                return self.gerar_resultado(
                    classificacao='Péssimo',
                    faixa='2 < P/VP <= 3',
                    descricao='Preço muito acima do valor patrimonial.',
                    riscos='Sensibilidade a mudanças econômicas.',
                    referencia='Combine com evaluate_psr para receita e evaluate_margem_liquida para eficiência.'
                )
            # Verifica se P/VP excede 3, indicando sobrevalorização extrema
            elif p_vp > 3:
                # Retorna ResultadoPVP para ação extremamente sobrevalorizada
                return self.gerar_resultado(
                    classificacao='Fora da faixa',
                    faixa='P/VP > 3',
                    descricao='Preço extremamente elevado em relação ao patrimônio.',
                    riscos='Bolhas especulativas.',
                    referencia='Avalie evaluate_p_ativo para ativos e evaluate_crescimento_receita para tendências.'
                )
        # Captura exceções para entradas inválidas (ex.: não numéricas)
        except Exception as e:
            # Retorna ResultadoPVP com mensagem de erro
            return self._erro(mensagem=str(e))

    # Trata erros criando um ResultadoPVP de erro
    def _erro(self, mensagem):
        # Retorna ResultadoPVP com detalhes de erro
        return ResultadoPVP(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar o P/VP: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A'
        )

# Exibe os atributos de um ResultadoPVP formatados
def exibir_resultado(resultado):
    # Imprime cabeçalho do resultado da avaliação
    print("📊 Resultado da Avaliação P/VP")
    # Imprime a classificação
    print(f"Classificação: {resultado.classificacao}")
    # Imprime a faixa de P/VP
    print(f"Faixa: {resultado.faixa}")
    # Imprime a descrição
    print(f"Descrição: {resultado.descricao}")
    # Imprime a definição do P/VP
    print(f"Definição: {resultado.definicao}")
    # Imprime a categoria de agrupamento
    print(f"Agrupador: {resultado.agrupador}")
    # Imprime a fórmula
    print(f"Fórmula: {resultado.formula}")
    # Imprime os riscos
    print(f"Riscos: {resultado.riscos}")
    # Imprime as referências cruzadas
    print(f"Referência Cruzada: {resultado.referencia_cruzada}")
    # Imprime linha separadora
    print("-" * 60)

# Bloco principal para testes
if __name__ == "__main__":
    # Cria instância de PVPEvaluator
    avaliador = PVPEvaluator()

    # Teste 1: Avaliação automática com P/VP = 1.2
    # Avalia o valor P/VP 1.2
    resultado_avaliacao = avaliador.avaliar(1.2)
    # Imprime cabeçalho do teste
    print("🔍 Teste de avaliação automática:")
    # Imprime o objeto ResultadoPVP
    print(resultado_avaliacao)
    # Imprime a representação em dicionário
    print(resultado_avaliacao.to_dict())
    # Imprime linha em branco
    print()

    # Teste 2: Geração manual de resultado
    # Gera ResultadoPVP com entradas manuais
    resultado_manual = avaliador.gerar_resultado(
        classificacao='Teste',
        faixa='1.0 - 2.0',
        descricao='Exemplo de uso externo',
        riscos='Risco moderado',
        referencia='Referência fictícia'
    )
    # Imprime cabeçalho do teste
    print("🧪 Teste de geração manual de resultado:")
    # Imprime o objeto ResultadoPVP
    print(resultado_manual)
    # Imprime a representação em dicionário
    print(resultado_manual.to_dict())
    # Imprime linha em branco
    print()

    # Teste 3: Simulação de erro
    # Avalia entrada inválida para disparar erro
    resultado_erro = avaliador.avaliar("valor_invalido")
    # Imprime cabeçalho do teste
    print("⚠️ Teste de erro:")
    # Imprime o ResultadoPVP de erro
    print(resultado_erro)
    # Imprime a representação em dicionário
    print(resultado_erro.to_dict())
    # Imprime linha em branco
    print()

    # Teste adicional: Exibição formatada
    # Define valor de teste P/VP
    valor_pvp = 1.2
    # Avalia o valor P/VP
    resultado = avaliador.avaliar(valor_pvp)
    # Exibe resultado formatado
    exibir_resultado(resultado)
    # Imprime cabeçalho do dicionário
    print("📦 Resultado como dicionário:")
    # Converte resultado em dicionário e imprime
    print(resultado.to_dict())