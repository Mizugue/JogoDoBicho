import time
from bs4 import BeautifulSoup
import requests
import pyautogui
from itertools import permutations
import datetime

def captura():
    global resposta
    re = requests.get("https://www.resultadofacil.com.br/resultado-banca-federal")
    resposta = re.content


def webscrap():
    try:
        global lista
        lista = []
        soup = BeautifulSoup(resposta, 'html.parser')
        h3 = soup.find("h3", class_="h4")
        data = h3.text
        data = data[:20] + " :" + data[20:]
        print(f"                                                {data}                   ")
        print("")
        divs = soup.find_all("td")
        soma = 0
        for i in divs:
            soma += 1
            if soma <= 20:
                lista.append(i.text)
            else:
                pass
    except:
        hora = datetime.datetime.now()
        print(f" Estamos atualizando o resultado! Tenha paciencia... {hora}")
        exit()


def organizacao():
    global premio1, premio2, premio3, premio4, premio5, resulmilharcercada, resulcentenacercada, resuldezenacercada, resulgrupocercado, animais
    resulcentenacercada = []
    resuldezenacercada = []
    resulgrupocercado = []
    animais = []

    dados = [lista[i:i + 4] for i in range(0, len(lista), 4)]
    for i in range(len(dados)):
        for j in range(len(dados[i])):
            try:
                dados[i][j] = int(dados[i][j])
            except ValueError:
                pass


    premio1 = dados[0]
    premio2 = dados[1]
    premio3 = dados[2]
    premio4 = dados[3]
    premio5 = dados[4]

    animais = [premio1[3], premio2[3], premio3[3], premio4[3], premio5[3]]
    resulgrupocercado = [premio1[2], premio2[2], premio3[2], premio4[2], premio5[2]]
    resulmilharcercada = [premio1[1], premio2[1], premio3[1], premio4[1], premio5[1]]

    for i in resulmilharcercada:
        cen = (list(str(i)))
        cen.pop(0)
        cen = (int("".join(cen)))
        resulcentenacercada.append(cen)

        dez = (list(str(i)))
        dez.pop(0)
        dez.pop(1)
        dez = (int("".join(dez)))
        resuldezenacercada.append(dez)



def menu():

    global jogos
    while True:
        try:
            resposta = input("Voce fez algum jogo? (sim/nao): ")
            if resposta == "sim":
                jogos = int(input("\n Quantos jogos voce fez?: "))
                print("\nShow de bola, vamos registrar os mesmos! ")
                break
            elif resposta == "nao":
                exit('Mesmo assim, espero ter ajudado em algo -_-')
            else:
                print("Não existe essa opcao!")
        except ValueError:
            print("Digite um valor válido!")


def registro():
    global log, milharseca, milharcercada, milharinvertida, centenaseca, centenacercada, centenainvertida, dezenaseca, dezenacercada, dezenainvertida, dezenaduque, dezenaterno, gruposeco, grupocercado, grupoduqueseco, grupoduquecercado, grupoternoseco, grupoternocercado
    sub = []
    log = []
    milharseca = []
    milharcercada = []
    milharinvertida = []
    centenaseca = []
    centenacercada = []
    centenainvertida = []
    dezenaseca = []
    dezenacercada = []
    dezenainvertida = []
    dezenaduque = []
    dezenaterno = []
    gruposeco = []
    grupocercado = []
    grupoduqueseco = []
    grupoduquecercado = []
    grupoternoseco = []
    grupoternocercado = []

    print("  Mostre-me seu jogo! ")

    try:

        for i in range(1, jogos + 1):

            casa = (int(input("\n                                                   [1]Milhar - [2]Centena - [3]Dezena - [4]Grupo = ")))
            print("")

            if casa == 1:
                opcaomilhar = (int(input("                       [1]Milhar Seca - [2]Milhar cercada 1 ao 5 - [3]Milhar invertida = ")))
                if opcaomilhar == 1:
                    milharseca.append(int(input("                                                Digite a milhar: ")))
                elif opcaomilhar == 2:
                    milharcercada.append(int(input("                                             Digite a milhar: ")))
                elif opcaomilhar == 3:
                    milharinvertida.append(int(input("                                           Digite a milhar: ")))
                else:
                    print("                                                   Nao existe essa opcao de jogo! Logo, refaça todo o mesmo!                                                   ")
                    registro()



            elif casa == 2:
                opcaocentena = (
                    int(input("        [1]Centena Seca - [2]Centena cercada 1 ao 5 - [3]Centena invertida = ")))
                if opcaocentena == 1:
                    centenaseca.append(int(input("                               Digite a centena:  ")))
                elif opcaocentena == 2:
                    centenacercada.append(int(input("                               Digite a centena: ")))
                elif opcaocentena == 3:
                    centenainvertida.append(int(input("                               Digite a centena:  ")))
                else:
                    print("                                                   Nao existe essa opcao de jogo! Logo, refaça todo o mesmo!                                                   ")
                    registro()



            elif casa == 3:
                opcaodezena = (int(input("        [1]Dezena Seca - [2]Dezena cercada 1 ao 5 - [3]Dezena invertida - [4]Duque de Dezena - [5]Terno de Dezena = ")))
                if opcaodezena == 1:
                    dezenaseca.append(
                        int(input("                                                   Digite a dezena: ")))
                elif opcaodezena == 2:
                    dezenacercada.append(
                        int(input("                                                   Digite a dezena:  ")))
                elif opcaodezena == 3:
                    dezenainvertida.append(
                        int(input("                                                   Digite a dezena:  ")))
                elif opcaodezena == 4:
                    print("Digite as duas dezenas:")
                    x = (int(input("")))
                    y = int(input(""))
                    sub = [x, y]
                    dezenaduque.append(sub)
                elif opcaodezena == 5:
                    print("Digite as tres dezenas:")
                    x = (int(input("")))
                    y = (int(input("")))
                    z = (int(input("")))
                    sub = [x, y, z]
                    dezenaterno.append(sub)
                else:
                    print("                                                   Nao existe essa opcao de jogo! Logo, refaça todo o mesmo!                                                   ")
                    registro()



            elif casa == 4:
                opcaogrupo = (int(input("        [1]Grupo Seco - [2]Grupo cercado 1 ao 5 - [3]Dupla de grupo seco 1/2 - [4]Dupla de grupo cercado 1 ao 5 - [5]Terno de grupo 1 ao 3 - [6]Terno de grupo 1 ao 5  = ")))
                if opcaogrupo == 1:
                    gruposeco.append(int(input("                                                   Digite o Grupo: ")))
                elif opcaogrupo == 2:
                    grupocercado.append(
                        int(input("                                                   Digite o Grupo: ")))
                elif opcaogrupo == 3:
                    print("Digite os dois grupos: ")
                    x = (int(input(" ")))
                    y = int(input(" "))
                    sub = [x, y]
                    grupoduqueseco.append(sub)
                elif opcaogrupo == 4:
                    print("Digite os dois grupos: ")
                    x = (int(input(" ")))
                    y = int(input(" "))
                    sub = [x, y]
                    grupoduquecercado.append(sub)
                elif opcaogrupo == 5:
                    print("Digite os tres grupos: ")
                    x = (int(input(" ")))
                    y = (int(input(" ")))
                    z = (int(input(" ")))
                    sub = [x, y, z]
                    grupoternoseco.append(sub)
                elif opcaogrupo == 6:
                    print("Digite os tres grupos: ")
                    x = (int(input(" ")))
                    y = (int(input(" ")))
                    z = (int(input(" ")))
                    sub = [x, y, z]
                    grupoternocercado.append(sub)
                else:
                    print("                                                   Nao existe essa opcao de jogo! Logo, refaça todo o mesmo!                                                   ")
                    registro()



            else:
                print("                                                   Nao existe essa opcao de jogo! Logo, refaça todo o mesmo!                                                   ")
                registro()

            if casa > 0 and casa <= 4:
                if casa == 1:
                    sub = [casa, opcaomilhar]

                elif casa == 2:
                    sub = [casa, opcaocentena]

                elif casa == 3:
                    sub = [casa, opcaodezena]

                elif casa == 4:
                    sub = [casa, opcaogrupo]
                log.append(sub)
            else:
                pass


    except ValueError:
        print("                                                   Voce digitou algo errado! Logo, refaça os jogos                                                   ")
        registro()


def correcao():
    invertidos = []
    soma = 0
    derrota = 0

    def permutar(lista):
        invertidos = []

        for numero in lista:
            numero_str = str(numero)
            if (len(numero_str)) == 1 and lista is milharinvertida:
                numero_str = numero_str + "000"
                permutacoes = permutations(numero_str)
                for permutacao in permutacoes:
                    numeroinvertido = int("".join(permutacao))
                    invertidos.append(numeroinvertido)

            elif (len(numero_str)) == 2 and lista is milharinvertida or (len(numero_str)) == 1 and lista is centenainvertida:
                numero_str = numero_str + "00"
                permutacoes = permutations(numero_str)
                for permutacao in permutacoes:
                    numeroinvertido = int("".join(permutacao))
                    invertidos.append(numeroinvertido)

            elif (len(numero_str)) == 3 and lista is milharinvertida or (len(numero_str)) == 2 and lista is centenainvertida or (len(numero_str)) == 1 and lista is dezenainvertida:
                numero_str = numero_str + "0"
                permutacoes = permutations(numero_str)
                for permutacao in permutacoes:
                    numeroinvertido = int("".join(permutacao))
                    invertidos.append(numeroinvertido)
            else:
                permutacoes = permutations(numero_str)
                for permutacao in permutacoes:
                    numeroinvertido = int("".join(permutacao))
                    invertidos.append(numeroinvertido)



        invertidos = set(invertidos)
        invertidos = list(invertidos)


        return invertidos


    print("\n Os jogos foram registrados com sucesso!! Aguarde agora a correcao🤞🍀", end="")
    for i in range(5):
        print(".", end="")
        time.sleep(0.5)
    print("")
    pyautogui.sleep(1)
    for i in log:
        if i[0] == 1:
            if i[1] == 1:
                for i in milharseca:
                    if i == premio1[1]:
                        print(f"-Parabens voce acertou a milhar {i} na cabeca!")
                        milharseca.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 2:
                for i in milharcercada:
                    if i in resulmilharcercada:
                        posicao = resulmilharcercada.index(i) + 1
                        print(f"-Parabens!! Voce acertou a milhar cercada {i} na posicao {posicao}!")
                        milharcercada.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 3:
                if soma == 0:
                    invertidos = permutar(milharinvertida)
                    for i in invertidos:
                        if i in resulmilharcercada:
                            posicao = resulmilharcercada.index(i) + 1
                            print(f"-Parabens!! Voce acertou a milhar {i} invertida na posicao {posicao}!")
                            invertidos.remove(i)
                            soma += 1
                            derrota += 1
                        else:
                            pass
                else:
                    for i in invertidos:
                        if i in resulmilharcercada:
                            posicao = resulmilharcercada.index(i) + 1
                            print(f"-Parabens!! Voce acertou a milhar {i} invertida na posicao {posicao}!")
                            invertidos.remove(i)
                            derrota += 1
                        else:
                            pass




        elif i[0] == 2:
            if i[1] == 1:
                for i in centenaseca:
                    if i == resulcentenacercada[0]:
                        print(f"-Parabens voce acertou a centena {i} na cabeca!")
                        centenaseca.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 2:
                for i in centenacercada:
                    if i in resulcentenacercada:
                        posicao = resulcentenacercada.index(i) + 1
                        print(f"-Parabens!! Voce acertou a centena cercada {i} na posicao {posicao}!")
                        centenacercada.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 3:
                if soma == 0:
                    invertidos = permutar(centenainvertida)
                    for i in invertidos:
                        if i in resulcentenacercada:
                            posicao = resulcentenacercada.index(i) + 1
                            print(f"-Parabens!! Voce acertou a centena {i} invertida na posicao {posicao}!")
                            invertidos.remove(i)
                            soma += 1
                            derrota += 1
                        else:
                            pass
                else:
                    for i in invertidos:
                        if i in resulcentenacercada:
                            posicao = resulcentenacercada.index(i) + 1
                            print(f"-Parabens!! Voce acertou a centena {i} invertida na posicao {posicao}!")
                            invertidos.remove(i)
                            derrota += 1
                        else:
                            pass


        elif i[0] == 3:
            if i[1] == 1:
                for i in dezenaseca:
                    if i == resuldezenacercada[0]:
                        print(f"-Parabens voce acertou a dezena {i} na cabeca!")
                        dezenaseca.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 2:
                for i in dezenacercada:
                    if i in resuldezenacercada:
                        posicao = resuldezenacercada.index(i) + 1
                        print(f"-Parabens!! Voce acertou a dezena cercada {i} na posicao {posicao}!")
                        dezenacercada.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 3:
                if soma == 0:
                    invertidos = permutar(dezenainvertida)
                    for i in invertidos:
                        if i in resuldezenacercada:
                            posicao = resuldezenacercada.index(i) + 1
                            print(f"-Parabens!! Voce acertou a dezena {i} invertida na posicao {posicao}!")
                            invertidos.remove(i)
                            soma += 1
                            derrota += 1
                        else:
                            pass
                else:
                    for i in invertidos:
                        if i in resuldezenacercada:
                            posicao = resuldezenacercada.index(i) + 1
                            print(f"-Parabens!! Voce acertou a dezena {i} invertida na posicao {posicao}!")
                            invertidos.remove(i)
                            derrota += 1
                        else:
                            pass
            elif i[1] == 4:
                for i in dezenaduque:
                    if i[0] and i[1] in resuldezenacercada:
                        posicao = resuldezenacercada.index(i[0]) + 1
                        posicao1 = resuldezenacercada.index(i[1]) + 1
                        print(f"-Parabens!! Voce acertou a Dupla de dezena {i[0]} na posicao {posicao} e {i[1]} na posicao {posicao1}!")
                        dezenaduque.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 5:
                for i in dezenaterno:
                    if i[0] and i[1] and i[2] in resuldezenacercada:
                        posicao = resuldezenacercada.index(i[0]) + 1
                        posicao1 = resuldezenacercada.index(i[1]) + 1
                        posicao2 = resuldezenacercada.index(i[2]) + 1
                        print(f"-Parabens!! Voce acertou o Terno de dezena {i[0]} na posicao {posicao}, {i[1]} na posicao {posicao1} e {i[2]} na {posicao2}!")
                        dezenaterno.remove(i)
                        derrota += 1
                    else:
                        pass
        elif i[0] == 4:
            if i[1] == 1:
                for i in gruposeco:
                    if i == resulgrupocercado[0]:
                        print(f"-Parabens!! Voce acertou o grupo {i} - {animais[0]}, na cabeca!")
                        gruposeco.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 2:
                for i in grupocercado:
                    if i in resulgrupocercado:
                        posicao = resulgrupocercado.index(i) + 1
                        coringa = resulgrupocercado.index(i)
                        coringa = animais[coringa]
                        print(f"-Parabens!! Voce acertou o grupo {i} - {coringa}, na posicao {posicao}!")
                        grupocercado.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 3:
                for i in grupoduqueseco:
                    if i[0] == resulgrupocercado[0] and i[1] == resulgrupocercado[1]:
                        print(f"-Parabens!!! Voce acertou o Duque de grupo {i[0]} - {animais[0]} e {i[1]} - {animais[1]}, na cabeca!")
                        grupoduqueseco.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 4:
                for i in grupoduquecercado:
                    if i[0] and i[1] in resulgrupocercado:
                        posicao = resulgrupocercado.index(i[0]) + 1
                        coringa = resulgrupocercado.index(i[0])
                        posicao1 = resulgrupocercado.index(i[1]) + 1
                        coringa1 = resulgrupocercado.index(i[1])
                        print(f"-Parabens!! Voce acertou o Duque de grupo {i[0]} - {animais[coringa]} na posicao {posicao} e {i[1]} - {animais[coringa1]} na posicao {posicao1} cercados!")
                        grupoduquecercado.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 5:
                for i in grupoternoseco:
                    if i[0] == resulgrupocercado[0] and i[1] == resulgrupocercado[1] and i[2] == resulgrupocercado[2]:
                        print(f"-Parabens!! Voce acertou o Terno de grupo {i[0]} - {animais[0]}, {i[1]} - {animais[1]} e {i[2]} - {animais[2]} na cabeca!")
                        grupoternoseco.remove(i)
                        derrota += 1
                    else:
                        pass
            elif i[1] == 6:
                for i in grupoternocercado:
                    if i[0] and i[1] and i[2] in resulgrupocercado:
                        posicao = resulgrupocercado.index(i[0]) + 1
                        coringa = resulgrupocercado.index(i[0])
                        posicao1 = resulgrupocercado.index(i[1]) + 1
                        coringa1 = resulgrupocercado.index(i[1])
                        posicao2 = resulgrupocercado.index(i[2])
                        coringa2 = resulgrupocercado.index(i[2])
                        print(f"-Parabens!! Voce acertou o Terno de grupo {i[0]} - {animais[coringa]} na posicao {posicao}, {i[1]} - {animais[coringa1]} na posicao {posicao1} e {i[2]} - {animais[coringa2]} na posicao {posicao2}!")
                        grupoternocercado.remove(i)
                        derrota += 1
                    else:
                        pass

    if derrota == 0:

        print(f"\n➡️ Infelizmente nao foi dessa vez! Dos {jogos} jogos, voce perdeu todos...")
    else:
        print(f"\n➡️ Dessa vez, em {jogos} jogos, voce obteve exito em {derrota}! ")



def resultado():
    print("\n------------------------------------------------------------------------------------------------------------------")
    print("                                                    RESULTADO OFICIAL!                                                \n")
    for i in range(0,5):
        print(f"                                             🍀 {i+1}º - {resulmilharcercada[i]} - Grupo {resulgrupocercado[i]} {animais[i]} 🍀                                               ")
    print("\n------------------------------------------------------------------------------------------------------------------")





if __name__ == "__main__":
    captura()
    webscrap()
    organizacao()
    menu()
    registro()
    correcao()
    resultado()






