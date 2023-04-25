import random

continuar: bool = True

while continuar:
    print("============================")
    print("Adivinhe o número de 0 a 10!")
    print("============================\n")

    numero_aleatorio: int = random.randint(0, 10)
    numero_escolhido_str: str = input("Digite um número: ")

    while not numero_escolhido_str.isnumeric():
        numero_escolhido_str = input("Digite um NÚMERO: ")

    numero_escolhido: int = int(numero_escolhido_str)

    if numero_aleatorio == numero_escolhido:
        print(f"Vocé acertou!\nO número escolhido foi {numero_escolhido} e o gerado foi {numero_aleatorio}.")
    else:
        print(f"Vocé errou...\nO número escolhido foi {numero_escolhido} e o gerado foi {numero_aleatorio}.")

    input_continuar: str = input("Deseja continuar a jogar? (Digite 1 para sim): ")
    if input_continuar != "1":
        continuar = False