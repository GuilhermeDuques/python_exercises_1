import matplotlib.pyplot as plt
def calcule_os_gastos (Valor_inicial,Rendimento_por_período,Aporte_a_cada_período,Total_de_períodos):
      Indice = []
      Valores = []
  
      for i in range(Total_de_períodos):
          Valor_inicial = (Valor_inicial * (1 + (Rendimento_por_período/100))) + Aporte_a_cada_período
          Indice.append(i + 1)
          Valores.append(Valor_inicial)

          print("Após o ",(i + 1)," períodos o montante será de: R$ ",(Valor_inicial),".")
          
      plt.plot(Indice,Valores)
      plt.show()


     
    
Valor_inicial = float(input("Informe o valor inicial:R$"))

Rendimento_por_período = float(input("Informe o valor do rendimento por período:%"))

Aporte_a_cada_período = float(input("Informe o valor do aporte:R$"))

Total_de_períodos = int(input("Informe o total de períodos em meses:"))


    
calcule_os_gastos (Valor_inicial,Rendimento_por_período,Aporte_a_cada_período,Total_de_períodos)

