import random

continuar: bool = True

while continuar:
    print("============================")
    print("Adivinhe o número de 0 a 10!")
    print("============================\n")

    print("Você tem 3 chances para descobrir o número. Daremos dicas para facilitar.\nBoa sorte!\n")

    numero_aleatorio: int = random.randint(0, 10)
    acertou: bool = False

    for i in range(1, 4):
        numero_escolhido_str: str = input("Digite um número: ")

        while not numero_escolhido_str.isnumeric():
            numero_escolhido_str = input("Digite um NÚMERO: ")

        numero_escolhido: int = int(numero_escolhido_str)

        if numero_aleatorio == numero_escolhido:
            print(f"\nVocé acertou!\nO número escolhido foi {numero_escolhido} e o gerado foi {numero_aleatorio}.")
            print("Parabéns! Você é um vidente...\n")
            acertou = True
            break
        else:
            if numero_escolhido > numero_aleatorio:
                print(f"Vocé errou...\nO número escolhido foi {numero_escolhido} e ele é MAIOR que o número gerado!")
            else:
                print(f"Vocé errou...\nO número escolhido foi {numero_escolhido} e ele é MENOR que o número gerado!")
            print(f"Já foram {i} tentativas.")

    if not acertou:
        print(f"\nVemos que você é péssimo em adivinhação. O número gerado era {numero_aleatorio}.")
        print("Tente uma outra vez se quiser!\n")

    input_continuar: str = input("Deseja continuar a jogar? (Digite 1 para sim): ")
    if input_continuar != "1":
        continuar = False