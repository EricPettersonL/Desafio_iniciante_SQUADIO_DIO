def solicitar_itens():
    itens = []

    for i in range(3):
        item = input(f"Digite o {i+1}° item: ")
        itens.append(item)

    return itens

def exibir_itens(itens):
    print("Lista de itens:")
    for item in itens:
        print(f"- {item}")

def main():
    itens = solicitar_itens()
    exibir_itens(itens)

if __name__ == "__main__":
    main()