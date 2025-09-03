from datetime import datetime
import time

def linhas(mensagem):
    print(f"""{'-' * 50}
{mensagem.center(50)}
{'Horário:'.rjust(25)} {data[0]}:{data[1]}
{'Restaurante fecha às 22:30'.center(50)}
{'-' * 50}""")

def mostrar_cardapio():
    global preco_comida
    preco_comida = 0

    while True: 
        print("""CARDÁPIO
    [1]: Batatas Fritas - R$10 (200 gramas)       [6]: X-Salada - R$30
    [2]: Coca-Cola - R$12 (2 litros)              [7]: Porção de Frango - R$70
    [3]: Onion Ring - R$20 (200 gramas)           [8]: Tilápia com acompanhamentos - R$90 (600 gramas)
    [4]: Sprite - R$12 (2 litros)                 [9]: H2O - R$8 (600 ml)
    [5]: Polenta Frita - R$40 (500 gramas)        [10]: Sair""")

        cardapio = int(input('Digite o cardápio:\n>>>'))

        while cardapio <= 0 or cardapio > 10:
            cardapio = int(input('Por favor, digite corretamente.\nDigite o cardápio:\n>>>'))

        if cardapio == 1:
            preco_comida += 10
        elif cardapio == 2:
            preco_comida += 12
        elif cardapio == 3:
            preco_comida += 20
        elif cardapio == 4:
            preco_comida += 12
        elif cardapio == 5:
            preco_comida += 40
        elif cardapio == 6:
            preco_comida += 30
        elif cardapio == 7:
            preco_comida += 70
        elif cardapio == 8:
            preco_comida += 90
        elif cardapio == 9:
            preco_comida += 8
        elif cardapio == 10:
            while preco_comida == 0:
                print('Deve-se escolher ao menos um alimento.')
                mostrar_cardapio()


            else:
                print('Seu pedido está sendo preparado...')

                segundos = 15

                while segundos > 0:
                    print(f'{segundos:02d}', end='\r', flush=True)
                    time.sleep(1)

                    if segundos == 0:
                        segundos = 59
                    else:
                        segundos -= 1

                print('00:00')
                break
        print('Adicionado com sucesso!')


data = datetime.now().strftime('%H'), datetime.now().strftime('%M')

if data[0] >= '22' and data[1] > '30':
    print(f'Agora são {data[0]}:{data[1]}')
    print('Restaurante Fechado')
    print('Volte sempre!')
else:
    idades = []
    desconto = 0
    preco_entrada = 0
    linhas('Bem vindo(a) ao Restaurante!')

    print('CADASTRO DE PESSOAS')
    pessoas = int(input('São quantas pessoas?\n>>> '))
    while pessoas <= 0:
        pessoas = int(input('Por favor, digite corretamente\n>>> '))

    for pessoa in range(pessoas):
        idade = int(input(f'Digite a idade da pessoa {pessoa+1}\n>>> '))
        while idade <= 0 or idade > 120:
            idade = int(input(f'Idade excedeu o limite.\nDigite a idade da pessoa {pessoa+1}\n>>> '))

    idades.append(idade)
    preco_entrada += 25

    if idade < 10:
        desconto += 0.05
    elif idade >= 10 and idade < 18:
        desconto += 0.03
    elif idade >= 18:
        desconto += 0.02

    preco_entrada -= (preco_entrada * desconto)
    print(f'O preço por todas as pessoas é de R${preco_entrada} reais.')


    mostrar_cardapio()

    total = preco_entrada + preco_comida

    print(f'O preço total é de R${total} reais')
