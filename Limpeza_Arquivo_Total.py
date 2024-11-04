import os

def limpar_arquivo(caminho_arquivo):
    """
    Limpa o conteúdo do arquivo especificado.
    """
    try:
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write('')
    except Exception as e:
        print(f"Erro ao limpar o arquivo: {e}")


# Passo 1: Limpar arquivo de destino
limpar_arquivo(r"caminho_arquivo")
