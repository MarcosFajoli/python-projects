import jogos


def jogar():
    continuar: bool = True
    total_tentativas: int = 3

    while continuar:
        print("============================")
        print("=======Jogo da velha!=======")
        print("============================\n")

        input_continuar: str = input("Deseja continuar a jogar? (Digite 1 para sim): ")
        if input_continuar != "1":
            continuar = False

    print("\nRetornando para a seleção de jogos...\n")
    jogos.escolher_jogo()


if __name__ == "__main__":
    jogar()
