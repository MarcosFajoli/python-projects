import jogos


def tabuleiro(marcacoes):  # construcao do tabuleiro
    tabuleiro_str: str = "\n     1     2     3  \n" \
                         "        |     |     \n" \
                         f"1    {marcacoes[0][0]}  |  {marcacoes[0][1]}  |  {marcacoes[0][2]}  \n" \
                         "   _____|_____|_____\n" \
                         "        |     |     \n" \
                         f"2    {marcacoes[1][0]}  |  {marcacoes[1][1]}  |  {marcacoes[1][2]}  \n" \
                         "   _____|_____|_____\n" \
                         "        |     |     \n" \
                         f"3    {marcacoes[2][0]}  |  {marcacoes[2][1]}  |  {marcacoes[2][2]}  \n" \
                         "        |     |     \n"

    return tabuleiro_str


def resetar_marcacoes():  # mapeia o array de marcacoes como " "
    marcacoes = []
    for x in range(0, 3):
        linha = []
        for y in range(0, 3):
            linha.append(" ")
        marcacoes.append(linha)

    return marcacoes


def validar_jogada(entrada_list):
    # variavel contendo as validações
    is_valid: bool = len(entrada_list) == 1 or \
                                len(entrada_list) > 2 or \
                                (not (entrada_list[0].isnumeric() and entrada_list[1].isnumeric())) or \
                                int(entrada_list[0]) < 1 or \
                                int(entrada_list[0]) > 3 or \
                                int(entrada_list[1]) < 1 or \
                                int(entrada_list[1]) > 3

    return is_valid


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

        marcacoes: list = resetar_marcacoes()

        for i in range(1, 10):
            print(tabuleiro(marcacoes))

            if i % 2 == 1:
                jogador_rodada: int = 1
                marcador: str = "X"
            else:
                jogador_rodada: int = 2
                marcador: str = "O"

            entrada_str: str = input(
                f"Jogador {jogador_rodada}, escolha a posição a ser jogada no formato: 1, 1 (linha e coluna)\n")
            entrada_list: list = entrada_str.split(", ")

            # verifica o input feito, e se está vazio no tabuleiro
            while validar_jogada(entrada_list) or marcacoes[int(entrada_list[0]) - 1][int(entrada_list[1]) - 1] != " ":
                entrada_str: str = input("Escolha um formato válido de posição vazio: EX 1, 1 (até 3)\n")
                entrada_list: list = entrada_str.split(", ")

            linha: int = int(entrada_list[0]) - 1
            coluna: int = int(entrada_list[1]) - 1

            marcacoes[linha][coluna]: str = marcador

        input_continuar: str = input("Deseja continuar a jogar? (Digite 1 para sim): ")
        if input_continuar != "1":
            continuar = False

    print("\nRetornando para a seleção de jogos...\n")
    jogos.escolher_jogo()


if __name__ == "__main__":
    jogar()
