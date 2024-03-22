# O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta.

# Entrada
quantidade_passos = int(input("Digite a quantidade de passos:"))

if quantidade_passos == 0:
    print("Nenhum passo dado na floresta")
elif quantidade_passos >= 1:
    for i in range(quantidade_passos):
        print("Explorador", i+1, "passos")
else:
    print("Digite uma quantidade de passos positiva")    