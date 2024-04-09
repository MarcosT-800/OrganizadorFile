import pandas as pd

def organizar_arquivo(arquivo_entrada, arquivo_saida):
    try:
        # Ler dados do arquivo de entrada (assumindo que o separador é vírgula)
        df = pd.read_csv(arquivo_entrada)
        
        # Salvar os dados organizados em um arquivo Excel
        df.to_excel(arquivo_saida, index=False)
        
        return "Arquivo organizado foi salvo em " + arquivo_saida
    except Exception as e:
        return "Erro ao organizar arquivo: " + str(e)

# Arquivo de entrada (desorganizado)
arquivo_entrada = input("Insira o caminho do arquivo desorganizado: ")

# Arquivo de saída (organizado)
arquivo_saida = input("Insira o nome do arquivo de saída (com extensão .xlsx): ")

# Organizar o arquivo
resultado = organizar_arquivo(arquivo_entrada, arquivo_saida)
print(resultado)
