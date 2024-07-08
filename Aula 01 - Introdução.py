#IMPRIMIR/EXIBIR UMA INFORMAÇÃO

#Variáveis
faturamento = 1000
custo = 700

#Cálculo
imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento


#Exibir o resultado
print("Fraturamento foi de", faturamento)
print("O custo foi de", custo)
print("O lucro foi de", lucro)
print("A margem de lucro foi de", margem_lucro)


teve_lucro = True #Variável tipo Boolean

# Mod -> % resto da divisão
tempo_contrato = 170
tempo_anos = 170 / 12
print("Tempo em anos", int(tempo_anos))
tempo_meses = 170 % 12
print("Tempo em meses", tempo_meses)
