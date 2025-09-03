from random import choice


try:
    partidas = {
        "Jogador": 0,
        "Máquina": 0
    }

    possibilidades = ['pedra', 'papel', 'tesoura']

    while True:
        computador = choice(possibilidades)

        escolha = input('Pedra, Papel ou Tesoura?\n>>>').strip().lower()
        while escolha not in possibilidades:
            escolha = input('Por favor, digite corretamente.\nPedra, Papel ou Tesoura?\n>>>').strip().lower()

        vitoria = (computador == "pedra" and escolha == "papel") or (computador == "papel" and escolha == "tesoura") or (computador == "tesoura" and escolha == "pedra")

        empate = computador == escolha

        derrota = (computador == "pedra" and escolha == "tesoura") or (computador == "papel" and escolha == "pedra") or (computador == "tesoura" and escolha == "papel")


        print(f'Jogador: {escolha.upper()}\nMáquina: {computador.upper()}')
        if vitoria:
            print('Você venceu!')
            partidas["Jogador"] += 1
        elif empate:
            print('Empate!')
            partidas["Jogador"] += 1
            partidas["Máquina"] += 1
        elif derrota:
            print('A máquina venceu')
            partidas["Máquina"] += 1
        
        continuar = input('Deseja continuar? [S/N]:\n>>>').strip().upper()
        while continuar not in ['S', 'N']:
            continuar = input('Por favor, digite corretamente.\nDeseja continuar? [S/N]\n>>>').strip().upper()
        if continuar == 'N':
            break
        elif continuar == 'S':
            continue
except Exception as erro:
    print(f'Erro: {erro}')
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
