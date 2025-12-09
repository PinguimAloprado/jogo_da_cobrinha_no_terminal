from time import sleep
import pynput
import os
from random import randint
from funcoes_da_cobra import pontuação1, menu_cria, pontuação2, controles

# se for se da o trabalho de le isso, meus pesames que eu mato o portugues a cada 3 palavras e tem muita piadas, leia por sua conta e risco

# status obrigatorios a serem pre_definidos alto explicativos, mas caso vc tenha preguiça de pensa la vamos nos

corpo1 = [[22,3],[22,2],[22,1]] # o corpo1 base da cobra, cada lista dentro da lista é uma parte do corpo1

corpo2 = [[22,60],[22,61],[22,62]] # o corpo2 base da cobra, cada lista dentro da lista é uma parte do corpo1

direção1 = [0,1] # literalmente a direção1 que a cobra1 vai

direção2 = [0,-1] # literalmente a direção2 que a cobra2 vai

direção_t1 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

direção_t2 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

lista_de_moviemntos1 = [[0,1],[0,1],[0,1]] # lista de movimentos individuais de cada parte do corpo1.

lista_de_moviemntos2 = [[0,-1],[0,-1],[0,-1]] # lista de movimentos individuais de cada parte do corpo2.

local_frut = [22, 22] # local onde a fruta objeto fonte de interesse da cobra aparece

frut_comido = confir_frut = confir_corpo = pausa_tela = False # sistema de confirmação para sabe onde o corpo1 ta na matriz ea fruta tb, e se ele comeu a fruta.

leitura_tecla = rodando_menu = True # mantem o loop do jogo rodando

local_novo_corpo1 = [] # aqui eu guardo as coodernas do corpo1 ate ele se colocado em jogo

local_novo_corpo2 = [] # aqui eu guardo as coodernas do corpo2 ate ele se colocado em jogo

pontos1 = pontos2 = seta_local1 = 0 # so tenta advinha aposto que vc consegue

local_interface = 'menu'

opçao_escolhida = -1

# advinha tela do jogo o meu deus
texto_tela_kkk = pontuação1(pontos1)

# funções para muda a direção1 da cobra temporariamente

def up(): # não so não, eu confio que voce é inteligente o suficiente para descobrir sozinho oq essa parte faz
    global direção_t1,direção1, seta_local1

    if 'jogo' in local_interface:
        if direção_t1[0] == 1:
            pass
        else:
            direção1 = [-1,0]

    elif 'menu' in local_interface:
        seta_local1 -= 1

        if seta_local1 < 0:
            seta_local1 = 3

def down():
    global direção_t1,direção1, seta_local1, local_interface

    if 'jogo' in local_interface:
        if direção_t1[0] == -1:
            pass
        else:
            direção1 = [1,0]

    elif 'menu' in local_interface:
        seta_local1 += 1

        if seta_local1 > 3:
            seta_local1 = 0

def left():
    global direção_t1,direção1
    if direção_t1[1] == 1:
        pass
    else:
        direção1 = [0,-1]

def right():
    global direção_t1,direção1
    if direção_t1[1] == -1:
        pass
    else:
        direção1 = [0,1]

def Ww(): # não so não, eu confio que voce é inteligente o suficiente para descobrir sozinho oq essa parte faz
    global direção_t2,direção2, ceta_local2

    if 'jogo' in local_interface:
        if direção_t2[0] == 1:
            pass
        else:
            direção2 = [-1,0]

    elif 'menu' in local_interface:
        ceta_local2 -= 1

        if ceta_local2 < 0:
            ceta_local2 = 3

def Ss():
    global direção_t2,direção2, ceta_local2, local_interface

    if 'jogo' in local_interface:
        if direção_t2[0] == -1:
            pass
        else:
            direção2 = [1,0]

    elif 'menu' in local_interface:
        ceta_local2 += 1

        if ceta_local2 > 3:
            ceta_local2 = 0

def Dd():
    global direção_t2,direção2
    if direção_t2[1] == -1:
        pass
    else:
        direção2 = [0, 1]

def Aa():
    global direção_t2,direção2
    if direção_t2[1] == 1:
        pass
    else:
        direção2 = [0, -1]




# ativa as setas para o jogo

def on_press(key):
    global rodando_jogo, leitura_tecla, opçao_escolhida, pausa_tela, rodando_menu

    if not leitura_tecla:
        return 

    try:
        if key == pynput.keyboard.Key.up:
            up()
        elif key == pynput.keyboard.Key.down:
            down()
        elif key == pynput.keyboard.Key.left:
            left()
        elif key == pynput.keyboard.Key.right:
            right()
        elif key == pynput.keyboard.KeyCode.from_char('w'):
            Ww()
        elif key == pynput.keyboard.KeyCode.from_char('s'):
            Ss()
        elif key == pynput.keyboard.KeyCode.from_char('d'):
            Dd()
        elif key == pynput.keyboard.KeyCode.from_char('a'):
            Aa()
        elif key == pynput.keyboard.Key.enter:

            if 'menu' in local_interface:
                opçao_escolhida = seta_local1

            elif 'end game' in local_interface:
                pausa_tela = False
        elif key == pynput.keyboard.Key.esc:
            rodando_jogo = rodando_menu = pausa_tela = False
            """print(corpo1)
            print(lista_de_moviemntos1)"""
            return False  # para o listener
    except AttributeError:
        pass

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

rodando_jogo = True

while rodando_menu:

    os.system("clear")

    local_interface = 'menu'

    menu_tela = menu_cria(seta_local1)
    print(menu_tela)
    sleep(0.2)
    
    if opçao_escolhida == 0:

        rodando_jogo = True

        opçao_escolhida = -1

        leitura_tecla = True

        local_interface = 'jogo'

        while rodando_jogo: #gera a tela onde estamos jogando e atualizar posição e pontuções

            direção_t1 = direção1.copy() # sietema para empedir a cobra de entra dentro de se mesma

            lista_de_moviemntos1.insert(0, direção1) # atualizar a direção1 da cobra definitivamente


            for c in range(len(corpo1)): # atualizar a posição da cobra
                corpo1[c][0] += lista_de_moviemntos1[c][0]

                if corpo1[c][0] > 39: # faz a cobra ir para o outro lado da tela
                    corpo1[c][0] = 0

                elif corpo1[c][0] < 0: # faz a cobra ir para o outro lado da tela
                    corpo1[c][0] = 39

                corpo1[c][1] += lista_de_moviemntos1[c][1]

                if corpo1[c][1] > 63: # faz a cobra ir para o outro lado da tela
                    corpo1[c][1] = 0

                elif corpo1[c][1] < 0: # faz a cobra ir para o outro lado da tela
                    corpo1[c][1] = 63


            if local_frut[0] == corpo1[0][0] and local_frut[1] == corpo1[0][1]: # confirma se comeu a fruta para muda ela de lugar e aumentar a cobra

                local_novo_corpo1.append(local_frut) # marcando o local para quando tive espaço colocar o corpo1

                pontos1 += 1

                # advinha tela do jogo sendo atualizada o meu deus
                #texto_tela_kkk = pontuação1(pontos1)

                while True: # loop para acha um lugar para fruta 
                    Xx = randint(0,39)
                    Yy = randint(0,63)
                    frut_aprov = True
                    for c in corpo1: #loop de fato que acha
                        if (Xx == c[0] and Yy == c[1]) or (Xx == local_novo_corpo1[0][0] and Yy == local_novo_corpo1[0][1]):
                            frut_aprov = False # achou um lugar que n pode e tenta de novo
                            break
                    if frut_aprov: # achou um lugar que pode e libera
                        local_frut = [Xx, Yy] # muda o lugar da fruta
                        break

            if len(local_novo_corpo1) > 0: #olhando para ve se ja pode add a nova parte do corpo1

                ta_safe = True
                for c in corpo1:    
                    
                    if c[0] == local_novo_corpo1[0][0] and c[1] == local_novo_corpo1[0][1]:
                        ta_safe = False             
                        break   

                if ta_safe:
                    corpo1.append([local_novo_corpo1[0][0],local_novo_corpo1[0][1]])
                    local_novo_corpo1.pop(0)
                    


            for c in corpo1[1:]: #olhnado para ve se a cabeça bateu em algo

                if c[0] == corpo1[0][0] and c[1] == corpo1[0][1]:
                    pausa_tela = True
                    rodando_jogo = False

            
            # advinha tela do jogo o meu deus
            texto_tela_kkk = pontuação1(pontos1)
            for c in range(40): # isso foi massa porem tem um problema duvido acha, ele cria a tela basicamente, esse primeiro for gera o tamanho da coluna eixo y basicamente

                for cc in range(64): # gera o tamanho da linha eixo x

                    for ccc in corpo1: # ve se tenho que pinta aqui

                        if c == ccc[0] and cc == ccc[1]:
                            confir_corpo = True
                            break

                        elif c == local_frut[0] and cc == local_frut[1]:
                            confir_frut = True
                            break

                    if confir_corpo: # pinta de fato o corpo1
                        texto_tela_kkk += f'\033[41m   \033[m'
                        confir_corpo = False

                    elif confir_frut: # pinta de fato a fruta
                        texto_tela_kkk += f'\033[44m   \033[m'
                        confir_frut = False
                        
                    else: #deixa em branco
                        texto_tela_kkk += f'\033[40m   \033[m'

                texto_tela_kkk += '\n' # separa em linhas


            os.system("clear") # impedir de poluir o terminal
            print(texto_tela_kkk) # mostra a tela montada

            if len(corpo1) < len(lista_de_moviemntos1) - 1:
                lista_de_moviemntos1.pop()

            sleep(0.1) # impedir a tela de causa um ataca epiletico em vc



        corpo1 = [[22,3],[22,2],[22,1]] # o corpo1 base da cobra, cada lista dentro da lista é uma parte do corpo1

        direção1 = [0,1] # literalmente a direção1 que a cobra vai

        direção_t1 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

        lista_de_moviemntos1 = [[0,1],[0,1],[0,1]] # lista de movimentos individuais de cada parte do corpo1.

        local_frut = [22, 22] # local onde a fruta objeto fonte de interesse da cobra aparece

        pontos1 = 0

        local_novo_corpo1 = [] # aqui eu guardo as coodernas do corpo1 ate ele se colocado em jogo



        while pausa_tela:
            local_interface = 'end game'
                   
    elif opçao_escolhida == 1: #aqui vai ser o de 2

        rodando_jogo = True

        opçao_escolhida = -1

        leitura_tecla = True

        local_interface = 'jogo'

        while rodando_jogo: #gera a tela onde estamos jogando e atualizar posição e pontuções

            direção_t1 = direção1.copy() # sietema para empedir a cobra de entra dentro de se mesma

            lista_de_moviemntos1.insert(0, direção1) # atualizar a direção1 da cobra definitivamente

            direção_t2= direção2.copy() # sietema para empedir a cobra de entra dentro de se mesma

            lista_de_moviemntos2.insert(0, direção2) # atualizar a direção1 da cobra definitivamente


            for c in range(len(corpo1)): # atualizar a posição da cobra1
                corpo1[c][0] += lista_de_moviemntos1[c][0]

                if corpo1[c][0] > 39: # faz a cobra ir para o outro lado da tela
                    corpo1[c][0] = 0

                elif corpo1[c][0] < 0: # faz a cobra ir para o outro lado da tela
                    corpo1[c][0] = 39

                corpo1[c][1] += lista_de_moviemntos1[c][1]

                if corpo1[c][1] > 63: # faz a cobra ir para o outro lado da tela
                    corpo1[c][1] = 0

                elif corpo1[c][1] < 0: # faz a cobra ir para o outro lado da tela
                    corpo1[c][1] = 63

            for c in range(len(corpo2)): # atualizar a posição da cobra2
                corpo2[c][0] += lista_de_moviemntos2[c][0]

                if corpo2[c][0] > 39: # faz a cobra ir para o outro lado da tela
                    corpo2[c][0] = 0

                elif corpo2[c][0] < 0: # faz a cobra ir para o outro lado da tela
                    corpo2[c][0] = 39

                corpo2[c][1] += lista_de_moviemntos2[c][1]

                if corpo2[c][1] > 63: # faz a cobra ir para o outro lado da tela
                    corpo2[c][1] = 0

                elif corpo2[c][1] < 0: # faz a cobra ir para o outro lado da tela
                    corpo2[c][1] = 63





            if corpo2[0] == corpo1[0] and corpo2[0] == local_frut: # confirma se comeu a fruta para muda ela de lugar e aumentar a cobra
                pontos1 += 1
                pontos2 += 1

                corpo1 = [[22,3],[22,2],[22,1]] # o corpo1 base da cobra, cada lista dentro da lista é uma parte do corpo1

                corpo2 = [[22,60],[22,61],[22,62]] # o corpo2 base da cobra, cada lista dentro da lista é uma parte do corpo1

                direção1 = [0,1] # literalmente a direção1 que a cobra1 vai

                direção2 = [0,-1] # literalmente a direção2 que a cobra2 vai

                direção_t1 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

                direção_t2 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

                lista_de_moviemntos1 = [[0,1],[0,1],[0,1]] # lista de movimentos individuais de cada parte do corpo1.

                lista_de_moviemntos2 = [[0,-1],[0,-1],[0,-1]] # lista de movimentos individuais de cada parte do corpo2.

                pontos1 = 0

                pontos2 = 0

                local_novo_corpo1 = []

                local_novo_corpo2 = []

                while True: # loop para acha um lugar para fruta 
                    Xx = randint(0,39)
                    Yy = randint(0,63)
                    
                    if [Xx, Yy] in corpo1 and [Xx, Yy] in local_novo_corpo1[0]:
                        pass

                    elif [Xx, Yy] in corpo2 and [Xx, Yy] in local_novo_corpo2[0]:
                        pass

                    else: # achou um lugar que pode e libera
                        local_frut = [Xx, Yy] # muda o lugar da fruta
                        break

            elif local_frut == corpo1[0]: # confirma se comeu a fruta para muda ela de lugar e aumentar a cobra

                local_novo_corpo1.append(local_frut) # marcando o local para quando tive espaço colocar o corpo1

                pontos1 += 1

                # advinha tela do jogo sendo atualizada o meu deus
                #texto_tela_kkk = pontuação1(pontos1)

                while True: # loop para acha um lugar para fruta 
                    Xx = randint(0,39)
                    Yy = randint(0,63)
                    
                    if [Xx, Yy] in corpo1 and [Xx, Yy] in local_novo_corpo1[0]:
                        pass

                    elif [Xx, Yy] in corpo2 and [Xx, Yy] in local_novo_corpo2[0]:
                        pass

                    else: # achou um lugar que pode e libera
                        local_frut = [Xx, Yy] # muda o lugar da fruta
                        break

            elif local_frut == corpo2[0]: # confirma se comeu a fruta para muda ela de lugar e aumentar a cobra

                local_novo_corpo2.append(local_frut) # marcando o local para quando tive espaço colocar o corpo1

                pontos2 += 1

                # advinha tela do jogo sendo atualizada o meu deus
                #texto_tela_kkk = pontuação1(pontos1)

                while True: # loop para acha um lugar para fruta 
                    Xx = randint(0,39)
                    Yy = randint(0,63)
                    
                    if [Xx, Yy] in corpo1 and [Xx, Yy] in local_novo_corpo1[0]:
                        pass

                    elif [Xx, Yy] in corpo2 and [Xx, Yy] in local_novo_corpo2[0]:
                        pass

                    else: # achou um lugar que pode e libera
                        local_frut = [Xx, Yy] # muda o lugar da fruta
                        break           

            if len(local_novo_corpo1) > 0: #olhando para ve se ja pode add a nova parte do corpo1

                if [local_novo_corpo1[0][0],local_novo_corpo1[0][1]] in corpo1:
                    pass

                else:
                    corpo1.append([local_novo_corpo1[0][0],local_novo_corpo1[0][1]])
                    local_novo_corpo1.pop(0)

            if len(local_novo_corpo2) > 0: #olhando para ve se ja pode add a nova parte do corpo1

                if [local_novo_corpo2[0][0],local_novo_corpo2[0][1]] in corpo2:
                    pass

                else:
                    corpo2.append([local_novo_corpo2[0][0],local_novo_corpo2[0][1]])
                    local_novo_corpo2.pop(0)
            
                    
            if corpo1[0] in corpo2 and corpo2[0] in corpo1:

                corpo1 = [[22,3],[22,2],[22,1]] # o corpo1 base da cobra, cada lista dentro da lista é uma parte do corpo1

                corpo2 = [[22,60],[22,61],[22,62]] # o corpo2 base da cobra, cada lista dentro da lista é uma parte do corpo1

                direção1 = [0,1] # literalmente a direção1 que a cobra1 vai

                direção2 = [0,-1] # literalmente a direção2 que a cobra2 vai

                direção_t1 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

                direção_t2 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

                lista_de_moviemntos1 = [[0,1],[0,1],[0,1]] # lista de movimentos individuais de cada parte do corpo1.

                lista_de_moviemntos2 = [[0,-1],[0,-1],[0,-1]] # lista de movimentos individuais de cada parte do corpo2.

                local_novo_corpo1 = []

                local_novo_corpo2 = []

            elif corpo1[0]in corpo1[1:] or corpo1[0] in corpo2 : #vendo se a cabeça 1 bateu em algo

                corpo1 = [[22,3],[22,2],[22,1]] # o corpo1 base da cobra, cada lista dentro da lista é uma parte do corpo1

                direção1 = [0,1] # literalmente a direção1 que a cobra1 vai

                direção_t1 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

                lista_de_moviemntos1 = [[0,1],[0,1],[0,1]] # lista de movimentos individuais de cada parte do corpo1.

                pontos2 += pontos1

                pontos1 = 0

                local_novo_corpo1 = []

            elif corpo2[0] in corpo2[1:] or corpo2[0] in corpo1 : #vendo se a cabeça 2 bateu em algo

                corpo2 = [[22,60],[22,61],[22,62]] # o corpo2 base da cobra, cada lista dentro da lista é uma parte do corpo1

                direção2 = [0,-1] # literalmente a direção2 que a cobra2 vai

                direção_t2 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

                lista_de_moviemntos2 = [[0,-1],[0,-1],[0,-1]] # lista de movimentos individuais de cada parte do corpo2.

                pontos1 += pontos2

                pontos2 = 0

                local_novo_corpo2 = []

            if pontos2 == 50 or pontos1 == 50:
                pausa_tela = True
                rodando_jogo = False

            
            # advinha tela do jogo o meu deus
            texto_tela_kkk = pontuação2(pontos1, pontos2)
            for c in range(40): # isso foi massa porem tem um problema duvido acha, ele cria a tela basicamente, esse primeiro for gera o tamanho da coluna eixo y basicamente

                for cc in range(64): # gera o tamanho da linha eixo x


                    if local_frut == [c,cc]:
                        texto_tela_kkk += f'\033[44m   \033[m'

                    elif [c,cc] in corpo1:
                        texto_tela_kkk += f'\033[41m   \033[m'

                    elif [c,cc] in corpo2:
                        texto_tela_kkk += f'\033[42m   \033[m'

                    else:
                        texto_tela_kkk += f'\033[40m   \033[m'


                texto_tela_kkk += '\n' # separa em linhas


            os.system("clear") # impedir de poluir o terminal
            print(texto_tela_kkk) # mostra a tela montada

            if len(corpo1) < len(lista_de_moviemntos1) - 1:
                lista_de_moviemntos1.pop()

            if len(corpo2) < len(lista_de_moviemntos2) - 1:
                lista_de_moviemntos2.pop()

            sleep(0.1) # impedir a tela de causa um ataca epiletico em vc


            
        corpo1 = [[22,3],[22,2],[22,1]] # o corpo1 base da cobra, cada lista dentro da lista é uma parte do corpo1

        corpo2 = [[22,60],[22,61],[22,62]] # o corpo2 base da cobra, cada lista dentro da lista é uma parte do corpo1

        direção1 = [0,1] # literalmente a direção1 que a cobra1 vai

        direção2 = [0,-1] # literalmente a direção2 que a cobra2 vai

        direção_t1 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

        direção_t2 = [0,0] # sistema de priguiçoso para empedir a cobra de anda dentro de si mesma

        lista_de_moviemntos1 = [[0,1],[0,1],[0,1]] # lista de movimentos individuais de cada parte do corpo1.

        lista_de_moviemntos2 = [[0,-1],[0,-1],[0,-1]] # lista de movimentos individuais de cada parte do corpo2.

        local_frut = [22, 22] # local onde a fruta objeto fonte de interesse da cobra aparece

        pontos1 = 0

        pontos2 = 0

        local_novo_corpo1 = []

        local_novo_corpo2 = []



        while pausa_tela:
            local_interface = 'end game'
                   
    elif opçao_escolhida == 2:

        os.system("clear") # impedir de poluir o terminal
        pausa_tela = True
        opçao_escolhida = -1

        print(controles())

        while pausa_tela:
            local_interface = 'end game'        

    elif opçao_escolhida == 3: # sai do jogo
        rodando_menu = False


listener.stop()