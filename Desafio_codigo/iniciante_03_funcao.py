def obter_dados():
    entrada = input("Digite a capacidade atual e o aumento percentual (separados por um espaço): ")
    dados = entrada.split()

    if len(dados) != 2:
        print("Você esqueceu de dar um espaço entre os valores. Tente novamente.")
        return None, None
    else:
        capacidade_atual, aumento_percentual = map(int, dados)
        return capacidade_atual, aumento_percentual

def calcular_nova_capacidade(capacidade_atual, aumento_percentual):
    return int(capacidade_atual + capacidade_atual * (aumento_percentual / 100))

def main():
    capacidade_atual, aumento_percentual = obter_dados()
    if capacidade_atual is not None and aumento_percentual is not None:
        nova_capacidade = calcular_nova_capacidade(capacidade_atual, aumento_percentual)
        print("Nova capacidade:", nova_capacidade)

if __name__ == "__main__":
    main()
