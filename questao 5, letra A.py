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

def extrair_PIB(Pais,Ano):

    rotulos, conteudo = extrair_dados('kaka.csv')
    try:
        Indice_ano = rotulos.index(Ano)
        print(Indice_ano)
        
    except ValueError:
        print("Ano inválido")
        raise
    PIB = 0
    Indice_pais = -1
    Indice_linha = 0
    for linha in conteudo:
        if linha[0] == Pais:
            PIB = linha[Indice_ano]
            Indice_pais = Indice_linha
            break
        Indice_linha = Indice_linha+1
    if Indice_pais == -1:
        raise ValueError('País inválido')
    print(Indice_pais)
    print("O PIB no país ",Pais,"no ano de ",Ano," é:US$",PIB,"trilhões")
    
Qual_pais = input("Informe um país:")
Qual_ano = input("Informe o ano:")
            
              
extrair_PIB(Qual_pais,Qual_ano)

