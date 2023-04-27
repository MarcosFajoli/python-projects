import jogos


def tabuleiro(marcacoes):
    tabuleiro_str: str = "     |     |     \n" \
                         f"  {marcacoes[0][0]}  |  {marcacoes[0][1]}  |  {marcacoes[0][2]}  \n" \
                         "_____|_____|_____\n" \
                         "     |     |     \n" \
                         f"  {marcacoes[1][0]}  |  {marcacoes[1][1]}  |  {marcacoes[1][2]}  \n" \
                         "_____|_____|_____\n" \
                         "     |     |     \n" \
                         f"  {marcacoes[2][0]}  |  {marcacoes[2][1]}  |  {marcacoes[2][2]}  \n" \
                         "     |     |     \n"

    return tabuleiro_str


def resetar_marcacoes():
    marcacoes = []
    for x in range(0, 3):
        linha = []
        for y in range(0, 3):
            linha.append("X")
        marcacoes.append(linha)

    return marcacoes


def jogar():
    continuar: bool = True
    total_partidas: int = 3

    print("============================")
    print("=======Jogo da velha!=======")
    print("============================\n")

    print("Bem vindo ao jogo da velha. Chame seu amigo para jogar, pois ele é multiplayer! (LOCAL)")
    print("\nRegras do jogo:")
    print("1. Faça uma linha com seu sinal na vertical, diagonal ou horizontal para ganhar!")
    print("2. Não deixe com que seu oponente complete a linha!")
    print(f"3. Após {total_partidas} partidas, veremos quem é o verdadeiro vencedor...\n\nBoa sorte!\n")

    while continuar:
        print("Iniciando o jogo. \n")

        marcacoes = resetar_marcacoes()
        print(tabuleiro(marcacoes))

        entrada1_str: str = input("Jogador 1, escolha a posição a ser jogada no formato: 1, 1 (linha e coluna)\n")
        entrada1_list: list = entrada1_str.split(", ")

        # realiza a validação do número digitado
        while len(entrada1_list) == 1 or \
                len(entrada1_list) > 2 or \
                not (entrada1_list[0].isnumeric() and entrada1_list[1].isnumeric()) or \
                len(entrada1_list) == 1 or \
                len(entrada1_list) > 2 or \
                int(entrada1_list[0]) < 1 or \
                int(entrada1_list[0]) > 3 or \
                int(entrada1_list[1]) < 1 or \
                int(entrada1_list[1]) > 3:
            entrada1_str = input("Escolha um formato válido de posição: 1, 1 (até 3)\n")
            entrada1_list = entrada1_str.split(", ")

        input_continuar: str = input("Deseja continuar a jogar? (Digite 1 para sim): ")
        if input_continuar != "1":
            continuar = False

    print("\nRetornando para a seleção de jogos...\n")
    jogos.escolher_jogo()


if __name__ == "__main__":
    jogar()
