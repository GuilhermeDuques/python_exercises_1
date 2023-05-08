def extrair_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo: 
        conteudo = arquivo.read() 

    conteudo = conteudo.splitlines() 
    rotulos = conteudo[0]
    rotulos = rotulos.split(',')
    conteudo = conteudo[1:] 
    dados = []
    for elemento in conteudo:
        elemento = elemento.split(',') 
        dados.append(elemento)
      
    return rotulos, dados

def variacao_PIB():
    rotulos, conteudo = extrair_dados('kaka.csv')
    
    for linha in conteudo:
        print(linha)
        print(len(linha))
    
 
        valor_inicial = float(linha[1])
        valor_final = float(linha[len(linha)-1])
    
    
    
        Variacao = (valor_final/valor_inicial - 1) * 100
        print(linha[0]," Variacao do PIB:",Variacao,"%")



variacao_PIB()