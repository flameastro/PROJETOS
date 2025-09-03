import random
print("""----------------------------------------------------------------------------------
Bem vindo ao par ou impar! (Você estará jogando contra uma máquina). As regras são:
1- escolha entre par ou impar
2- escolha um número entre 1 a 100
Se você escolher par, e o resultado da soma do seu número com a da máquina der
par, então você ganha, vice-versa.
----------------------------------------------------------------------------------""")

partidas = {
    "Máquina": 0,
    "Jogador": 0
}

rodada = 0
try:
    while True:
        rodada += 1
        print(f'\n----------\nrodada {rodada}\n----------')
        machineChoice = random.randint(1, 100)

        pergunta = input('par ou impar:\n>>>').lower()
        while pergunta not in ['par', 'impar', 'ímpar']:
            pergunta = input('POR FAVOR, DIGITE PAR OU IMPAR:\n>>>').lower()

        userChoice = int(input('Escolha um número:\n>>>'))
        while userChoice not in range(1, 101):
            userChoice = int(input('Por favor, escolha um número entre 1 a 100!:\n>>>'))

        soma = userChoice + machineChoice            

        if (pergunta == 'par' and soma % 2 == 0) or (pergunta == 'impar' and soma % 2 != 0) or (pergunta == 'ímpar' and soma % 2 != 0):
            print(f'VOCÊ GANHOU! A máquina escolheu {machineChoice} e você escolheu {userChoice}')
            partidas['Jogador'] += 1
        else:
            pontoMachine =+ 1
            print(f'A MÁQUINA GANHOU! A máquina escolheu {machineChoice} e você escolheu {userChoice}')
            partidas['Máquina'] += 1

        print(f'Soma = {machineChoice + userChoice}')

        continuar = input('Deseja continuar? [S/N]:\n>>>').strip().upper()
        while continuar not in ['S', 'N']:
            continuar = input('Por favor, digite corretamente.\nDeseja continuar? [S/N]\n>>>').strip().upper()
        if continuar == 'N':
            break
        elif continuar == 'S':
            continue
except:
    print('ERRO!')
else:
    for chave, valor in partidas.items():
        print(f'{chave} fez {valor} {"ponto" if valor == 1 else "pontos"}')
    empate = partidas['Máquina'] == partidas['Jogador']
    vitoria = partidas['Máquina'] < partidas['Jogador']
    derrota = partidas['Máquina'] > partidas['Jogador']

    if empate:
        print('Empate')
    elif vitoria:
        print('Você ganhou!')
    elif derrota:
        print('A máquina ganhou')
