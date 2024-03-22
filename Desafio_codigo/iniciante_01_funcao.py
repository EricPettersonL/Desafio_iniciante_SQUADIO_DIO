def explorar_floresta():
    quantidade_passos = int(input("Digite a quantidade de passos: "))
    
    """
    A function that explores a forest by taking a specified number of steps. 
    It prompts the user to input the quantity of steps and then prints out the exploration progress, 
    starting from 1 step and increasing by 1 until the specified quantity is reached. 
    If the input is 0, it prints 'Nenhum passo dado na floresta'. 
    If the input is negative, it prints 'Digite uma quantidade de passos positiva'.
    """

    if quantidade_passos == 0:
        print("Nenhum passo dado na floresta")
    elif quantidade_passos > 0:
        for i in range(1, quantidade_passos + 1):
            if i == 1:
                print("Explorador: 1 passo")
            else:
                print(f"Explorador: {i} passos")
    else:
        print("Digite uma quantidade de passos positiva")

if __name__ == "__main__":
    explorar_floresta()
