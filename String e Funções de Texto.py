# STRINGS & FUNÇÕES DE TEXTO

faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print(f"Faturamento da empresa: {faturamento}, Custo {custo}, Lucro {lucro}")

email_cliente = "testesil@gmail.com"

# TRANSFORMANDO AS LETRAS DO E-MAIL EM MAIÚSCULO:
email_cliente = email_cliente.upper()
print(email_cliente)

# TRANSFORMANDO AS LETRAS DO E-MAIL EM MINÚSCULO:
email_cliente = email_cliente.lower()
print(email_cliente)

# DESCOBRINDO EM QUAL POSIÇÃO DETERMINADO(A) PALAVRA OU SÍMBOLO SE ENCONTRA NO E-MAIL:
print(email_cliente.find("@")-1)

# TAMANHO DO TEXTO:
print(len(email_cliente))

# EXTRAIR UM CARACTER:
print(email_cliente[0])

# TROCAR UM PEDAÇO DO TEXTO:
novo_email = email_cliente.replace("gmail.com", "outlook.com")
print(novo_email)

# AJUSTES NOS NOMES
nome = "gabriel silva"
print(nome.capitalize()) # Primeira letra maiúscula e o resto minúsculo.
print(nome.title()) # Letra de cada palavra em maiúsculo.


# Pegar o servidor do email
posicao_arroba = email_cliente.find("@")
servidor = email_cliente[posicao_arroba]
print(servidor)

# Pegar o 1° nome
posicao_especo = nome.find(" ")
primeiro_nome = nome[:posicao_especo]


# Pegar o sobrenome
sobrenome = nome[posicao_especo:]
print(primeiro_nome)
print(sobrenome)

# Casos especiais ------> Formatações numéricas 
# Inserindo 0%, ele atribuirá 0 casas decimais após a vírgula.
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: {faturamento}, Custo {custo}, Lucro {lucro}, Margem: {margem_lucro:0%}")
