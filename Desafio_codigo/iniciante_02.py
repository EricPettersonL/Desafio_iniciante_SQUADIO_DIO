# Crie um programa que permita cadastrar uma lista de itens que o personagem possui. 
# A lista deve conter o valor fixo de 3 itens e deve ser exibida na tela.

# Lista para armazenar os itens
itens = []

#//TODO: Solicite os itens ao usuário
for i in range(3):
    item = input(f"Digite o {i+1}° item: ")
    itens.append(item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")