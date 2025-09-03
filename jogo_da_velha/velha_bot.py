import random, colorama as cor

def cores():
    cor.init(autoreset=True)
    global azul, vermelho, verde, ciano
    azul = cor.Fore.BLUE
    vermelho = cor.Fore.RED
    verde = cor.Fore.GREEN
    ciano = cor.Fore.CYAN
cores()

jogo = [['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']]

def view():
    for visualizacao in jogo:
        print(visualizacao)

def visu(indice1, indice2, letra):
    jogo[indice1][indice2] = letra
    for visualizacao in jogo:
        print(visualizacao)

def alerta_posicao():
    print(vermelho + "Não é possível ir nesta posição! Já está ocupada!")

contador = 10
while contador > 1:
    if contador % 2 == 0:
        for i in range(1, 2):
            view()
        numero = int(input('Digite um número: '))
        while numero < 0 or numero > 10:
            print(vermelho + 'O número deve ser entre 1 e 9!')
            numero = int(input('Digite um número: '))
            continue
        if numero == 1:
            if jogo[0][0] == 'O' or jogo[0][0] == 'X':
                alerta_posicao()
                continue
            visu(0, 0, 'X')
        elif numero == 2:
            
            if jogo[0][1] == 'O' or jogo[0][1] == 'X':
                alerta_posicao()
                continue
            visu(0, 1, 'X')
        elif numero == 3:
            
            if jogo[0][2] == 'O' or jogo[0][2] == 'X':
                alerta_posicao()
                continue
            visu(0, 2, 'X')
        elif numero == 4:

            if jogo[1][0] == 'O' or jogo[1][0] == 'X':
                alerta_posicao()
                continue
            visu(1, 0, 'X')
        elif numero == 5:
            
            if jogo[1][1] == 'O' or jogo[1][1] == 'X':
                alerta_posicao()
                continue
            visu(1, 1, 'X')
        elif numero == 6:
            
            if jogo[1][2] == 'O' or jogo[1][2] == 'X':
                alerta_posicao()
                continue
            visu(1, 2, 'X')
        elif numero == 7:
            
            if jogo[2][0] == 'O' or jogo[2][0] == 'X':
                alerta_posicao()
                continue
            visu(2, 0, 'X')
        elif numero == 8:
            
            if jogo[2][1] == 'O' or jogo[2][1] == 'X':
                alerta_posicao()
                continue
            visu(2, 1, 'X')
        elif numero == 9:
            if jogo[2][2] == 'O' or jogo[2][2] == 'X':
                alerta_posicao()
                continue
            visu(2, 2, 'X')
    elif contador % 2 == 1:
        linha = random.choice(jogo) 
        elemento = random.choice(linha)
        if elemento == 'X' or elemento == 'O':
            elemento = random.choice(linha)
            continue
        print(verde + f'O robô escolheu {elemento}'.center(50, '-'))
        if elemento == '1':
            if jogo[0][0] == 'X' or jogo[0][0] == 'O':
                alerta_posicao()
                view()
                continue
            jogo[0][0] = 'O'
        elif elemento == '2':
            if jogo[0][1] == 'X' or jogo[0][1] == 'O':
                alerta_posicao()
                view()
                continue
            jogo[0][1] = 'O'
        elif elemento == '3':
            if jogo[0][2] == 'X' or jogo[0][2] == 'O':
                alerta_posicao()
                view()
                continue
            jogo[0][2] = 'O'
        elif elemento == '4':
            if jogo[1][0] == 'X' or jogo[1][0] == 'O':
                alerta_posicao()
                view()
                continue
            jogo[1][0] = 'O'
        elif elemento == '5':
            if jogo[1][1] == 'X' or jogo[1][1] == 'O':
                alerta_posicao()
                view()
                continue
            jogo[1][1] = 'O'
        elif elemento == '6':
            if jogo[1][2] == 'X' or jogo[1][2] == 'O':
                alerta_posicao()
                view()
                continue
            jogo[1][2] = 'O'
        elif elemento == '7':
            if jogo[2][0] == 'X' or jogo[2][0] == 'O':
                alerta_posicao()
                view()
                continue
            jogo[2][0] = 'O'
        elif elemento == '8':
            if jogo[2][1] == 'X' or jogo[2][1] == 'O':
                alerta_posicao()
                view()
                continue
            jogo[2][1] = 'O'
        elif elemento == '9':
            if jogo[2][2] == 'X' or jogo[2][2] == 'O':
                alerta_posicao()
                view()
                continue
            jogo[2][2] = 'O'
          
    contador -= 1
    if (jogo[0][0] == 'X' and jogo[0][1] == 'X' and jogo[0][2] == 'X') or (jogo[1][0] == 'X' and jogo[1][1] == 'X' and jogo[1][2] == 'X') or (jogo[2][0] == 'X' and jogo[2][1] == 'X' and jogo[2][2] == 'X') or (jogo[0][0] == 'X' and jogo[1][0] == 'X' and jogo[2][0] == 'X') or (jogo[0][1] == 'X' and jogo[1][1] == 'X' and jogo[2][1] == 'X') or (jogo[0][2] == 'X' and jogo[1][2] == 'X' and jogo[2][2] == 'X') or (jogo[0][0] == 'X' and jogo[1][1] == 'X' and jogo[2][2] == 'X') or (jogo[2][0] == 'X' and jogo[1][1] == 'X' and jogo[0][2] == 'X'):
        print(azul + 'Você Ganhou!')
        view()
        break

    if (jogo[0][0] == 'O' and jogo[0][1] == 'O' and jogo[0][2] == 'O') or (jogo[1][0] == 'O' and jogo[1][1] == 'O' and jogo[1][2] == 'O') or (jogo[2][0] == 'O' and jogo[2][1] == 'O' and jogo[2][2] == 'O') or (jogo[0][0] == 'O' and jogo[1][0] == 'O' and jogo[2][0] == 'O') or (jogo[0][1] == 'O' and jogo[1][1] == 'O' and jogo[2][1] == 'O') or (jogo[0][2] == 'O' and jogo[1][2] == 'O' and jogo[2][2] == 'O') or (jogo[0][0] == 'O' and jogo[1][1] == 'O' and jogo[2][2] == 'O') or (jogo[2][0] == 'O' and jogo[1][1] == 'O' and jogo[0][2] == 'O'):
        print(ciano + 'Robô ganhou!')
        view()
        break
else:
    print(verde + 'Empate')