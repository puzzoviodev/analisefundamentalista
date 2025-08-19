import pandas as pd

# Função para converter JSON em Excel
def json_to_excel(json_file_path, excel_file_path):
    try:
        # Ler o arquivo JSON
        df = pd.read_json(json_file_path)
        
        # Verificar se as colunas esperadas estão presentes
        expected_columns = ['Indicador', 'Classificação', 'Faixa de Referência', 'Interpretação', 'Classificação2']
        if not all(col in df.columns for col in expected_columns):
            raise ValueError("O JSON não contém todas as colunas esperadas: " + ", ".join(expected_columns))
        
        # Salvar o DataFrame como Excel
        df.to_excel(excel_file_path, sheet_name='Indicadores', index=False, engine='openpyxl')
        print(f"Arquivo Excel '{excel_file_path}' gerado com sucesso!")
        
    except FileNotFoundError:
        print(f"Erro: O arquivo JSON '{json_file_path}' não foi encontrado.")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Caminhos dos arquivos
json_file_path = 'Indicadores_Atualizado_Critico.json'
excel_file_path = 'Indicadores_Atualizado_Critico.xlsx'

# Executar a conversão
if __name__ == "__main__":
    #json_to_excel('D:\indicadores_completo.json', 'D:\saida.xlsx')
    # Forma correta usando barras duplas
    json_to_excel(r'D:\indicadores_completo.json', r'D:\saida.xlsx')