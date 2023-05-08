import matplotlib.pyplot as plt
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

def grafico_PIB(Pais):
    rotulos, conteudo = extrair_dados('kaka.csv')
    Indice = []
    Valores = []
    
    
    for linha in conteudo:
        print(linha)
        print(len(linha))
        
    
        if (linha[0] == Pais):
            
            i = 2013
          
            for indice in range (1, len(linha)):
                
                Indice.append(i)
                Valores.append(float(linha[indice]))
                i = i + 1
            
           
            
            plt.plot(Indice,Valores)
            plt.show()

Pais = input("Informe um pais:")

grafico_PIB(Pais)
