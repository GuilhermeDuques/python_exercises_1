def diagnosticar_gastos(Renda_mensal_total,Gastos_totais_com_moradia,Gastos_totais_com_educação,Gastos_totais_com_transporte):
    porcentagem_moradia = float(Gastos_totais_com_moradia * (100/Renda_mensal_total))
    porcentagem_educação = float(Gastos_totais_com_educação * (100/Renda_mensal_total))
    porcentagem_transporte = float(Gastos_totais_com_transporte * (100/Renda_mensal_total))
    valor_necessario_moradia = Renda_mensal_total * 0.3
    valor_necessario_educação = Renda_mensal_total * 0.2
    valor_necessario_transporte = Renda_mensal_total * 0.15

    print("Diagnostico:")
    
    if porcentagem_moradia < 30 :
        print("Seus gastos totais com moradia comprometem ",porcentagem_moradia,"% de sua renda total. O máximo recomendado é de 30%. Seus gastos com moradia estão dentro da margem recomendada.")
    else :
        print("Seus gastos totais com moradia comprometem ",porcentagem_moradia,"% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$",valor_necessario_moradia,".")

    if porcentagem_educação < 20 :
        print("Seus gastos totais com educação comprometem ",porcentagem_educação,"% de sua renda total. O máximo recomendado é de 20%. Seus gastos com educação estão dentro da margem recomendada.")
    else :
        print("Seus gastos totais com educação comprometem ",porcentagem_educação,"% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$",valor_necessario_educação,".")

    if porcentagem_transporte < 15 :
        print("Seus gastos totais com transporte comprometem ",porcentagem_transporte,"% de sua renda total. O máximo recomendado é de 15%. Seus gastos com transporte estão dentro da margem recomendada.")
    else :
        print("Seus gastos totais com transporte comprometem ",porcentagem_transporte,"% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$",valor_necessario_transporte,".")




Renda_mensal_total = float(input("Informe a renda total mensal : R$"))
    
Gastos_totais_com_moradia = float(input("Informe os gastos totais com moradia : R$"))

Gastos_totais_com_educação = float(input("Informe os gastos totais com educação : R$"))
    
Gastos_totais_com_transporte = float(input("Informe os gastos totais com transporte : R$"))





diagnosticar_gastos (Renda_mensal_total, Gastos_totais_com_moradia, Gastos_totais_com_educação, Gastos_totais_com_transporte)