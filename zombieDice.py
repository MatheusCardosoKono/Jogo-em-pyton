import random
import sys

def jogador_perde():
    print(listaJogadores[jogadorAtual]["nome: "] + " voltou ao mundo dos mortos! Boa sorte da próxima vez!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def vitoria_alcancada():
    global vitoria
    print(listaJogadores[jogadorAtual]["nome: "] + " venceu o jogo! Com " + str(listaJogadores[jogadorAtual]["cerebros: "]) + " cérebros!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    vitoria = True


def imprime_inicio():
    print("----------------------")
    print("Bem vindo a Zombiedice")
    print("----------------------")

def reseta_dados(jogadorAtual, listaDados, listaJogadores):
    global dadosSorteados
    global tiros
    global passos
    global cerebros
    global listaDadosRem

    dadosSorteados = []
    tiros = 0
    passos = 0
    cerebros = listaJogadores[jogadorAtual]["cerebros: "]
    listaDadosRem = listaDados.copy()
    return

#################################################################################################################################################################

imprime_inicio()

print("Defina o número de jogadores")
jogadores = int(input("Qual o número de jogadores?"))

while(jogadores < 2):
    print("Mínimo 2 jogadores")
    jogadores = int(input("Qual o número de jogadores?"))

listaJogadores = []
for i in range(jogadores) :
    nome = input("Qual o nome do jogador " + str(i + 1) + "?")
    listaJogadores.append({"nome: ":nome, "cerebros: ": 0})

print("bora jogar!")

dadoVerde = ("CPCTPC")
dadoAmarelo = ("TPCTPC")
dadoVermelho = ("TPTCPT")
listaDados = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho]
listaDadosRem = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho]

jogadorAtual = 0
dadosSorteados = []
tiros = 0
passos = 0
cerebros = str(listaJogadores[jogadorAtual]["cerebros: "])
vitoria = False



while not vitoria:
    print("___________________________________________________")
    print("Vez de " + listaJogadores[jogadorAtual]["nome: "])
    for i in range(3):
        numeroSorteado = random.randrange(0, len(listaDadosRem) - 1)
        dadoSorteado = listaDadosRem[numeroSorteado]

        if (dadoSorteado == dadoVerde):
            print((listaJogadores[jogadorAtual]["nome: "]) + " recebe Dado Verde")
        elif (dadoSorteado == dadoAmarelo):
            print((listaJogadores[jogadorAtual]["nome: "]) + " recebe Dado Amarelo")
        else:
            print((listaJogadores[jogadorAtual]["nome: "]) + " recebe Dado Vermelho")

        dadosSorteados.append(dadoSorteado)


    print("As faces sorteadas foram: ")

    for dadoSorteado in dadosSorteados:
        faceDado = random.choice(dadoSorteado)

        if faceDado == "C":
            print("C - Você comeu um Cérebro!")
            if dadoSorteado in listaDadosRem:
                listaDadosRem.remove(dadoSorteado)
            listaJogadores[jogadorAtual]["cerebros: "] += 1
        elif faceDado == "T":
            print("T - Você tomou um Tiro! :(")
            if dadoSorteado in listaDadosRem:
                listaDadosRem.remove(dadoSorteado)
            tiros += 1
        else:
            print("P - Sua vítima escapou!")
            passos += 1
    print("Pontuação: ")
    print("Cérebros: " + str(listaJogadores[jogadorAtual]["cerebros: "]))
    print("Tiros: " + str(tiros))
    verdeRestantes = listaDadosRem.count(dadoVerde)
    amareloRestantes = listaDadosRem.count(dadoAmarelo)
    vermelhoRestantes = listaDadosRem.count(dadoVermelho)
    print("Dados vermelhos restantes: " + str(vermelhoRestantes))
    print("Dados Amarelos restantes: " + str(amareloRestantes))
    print("Dados verdes restantes: " + str(verdeRestantes))

    if listaJogadores[jogadorAtual]["cerebros: "] >= 13:
        vitoria_alcancada()
        sys.exit("Fim de Jogo")


    if tiros >= 3:
        jogador_perde()
        del listaJogadores[jogadorAtual]
        if len(listaJogadores) == 1:
            jogadorAtual = 0
            vitoria_alcancada()
            sys.exit("Fim de Jogo")
        else:
            reseta_dados(jogadorAtual, listaDados, listaJogadores)



    elif len(listaDadosRem) < 3:
        jogadorAtual += 1
        reseta_dados(jogadorAtual, listaDados, listaJogadores)
        print("Não possue dados suficientes para rodar! Passando a rodada para jogador: " + str(listaJogadores[jogadorAtual]["nome: "]))

    else:

        continuarTurno = input("Deseja continuar rolando? [s/n]")

        if continuarTurno == "n":
            reseta_dados(jogadorAtual, listaDados, listaJogadores)
            if jogadorAtual == len(listaJogadores) - 1:
                jogadorAtual = 0
            else:
                jogadorAtual += 1



        else:
            print("Iniciando mais uma rodada! Boa sorte :)")
            dadosSorteados = []

