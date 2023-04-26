import adivinhacao
import velha


def escolher_jogo():
    print("============================")
    print("=====MINIGAMES LEMARQUE=====")
    print("============================\n")

    print("Escolha o minigame que deseja jogar:")
    print("(1) Adivinhação; (2) Jogo da Velha")

    escolha_str: str = input()
    while not escolha_str.isnumeric():
        escolha_str = input("Digite um número válido!!!\n")

    escolha: int = int(escolha_str)

    match escolha:
        case 1:
            print("Você escolheu o jogo da adivinhação! Iniciando...\n")
            adivinhacao.jogar()
        case 2:
            print("Você escolheu o jogo da velha! Iniciando...\n")
            velha.jogar()
        case _:
            print("Nenhuma opção válida inserida. Reiniciando...\n")
            escolher_jogo()


if __name__ == "__main__":
    escolher_jogo()
