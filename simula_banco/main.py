import json
import random
import datetime

data = datetime.datetime.now().strftime('%d/%m/%Y -> %H:%M:%S')

try:
    with open('arquivo.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
except:
    with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
        arquivo.write('{}')

with open('arquivo.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)


def cadastrar():
    identificador = len(dados)

    nome = input('Digite o nome completo:\n>>>').strip().title()
    while ' ' not in nome:
        nome = input('Por favor, digite o nome completo:\n>>>').strip().title()
    for i in dados:
        if dados[i]['Nome'] == nome:
            print('Este usuário já está cadastrado, Tente entrar.')
            return False
        
    senha = input('Crie uma senha:\n>>>').strip()
    while len(senha) < 8:
        senha = input('A senha deve ter a menos 8 caracteres. Crie uma senha:\n>>>').strip()

    idade = int(input('Digite a sua idade:\n>>>'))
    while idade not in range(10, 121):
        idade = int(input('Digite corretamente.\nDigite a sua idade:\n>>>'))

    saldo = random.randrange(50, 101, 5)

    dados.update({identificador: {'Nome': nome, 'Idade': idade, 'Saldo': saldo, 'Senha': senha}})
    print('Cadastro realizado com sucesso')

    with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def visualizar():
    print(f'{"ID":<4} {"NOME":<45} {"SALDO"}')
    for i in dados:
        print(f'{i:<4} {dados[i]['Nome']:<45} R${dados[i]['Saldo']}')

def entrar():
    nome = input('Digite o seu nome completo:\n>>>').strip().title()
    senha = input('Digite sua senha:\n>>>').strip()
    for id_origem in dados:
        if dados[id_origem]['Nome'] == nome:
            if dados[id_origem]['Senha'] == senha:
                print(f'\nBem-vindo(a), {nome}!\n')

                print('O que deseja fazer?')
                print('1: Depositar')
                print('2: Sacar')
                print('3: Transferir')
                print('4: Sair')

                menu = int(input('Digite o menu:\n>>>'))
                while menu not in range(1, 5):
                    menu = int(input('Digite corretamente:\n>>>'))

                if menu == 1:
                    valor = int(input('Deseja depositar quanto?\n>>>'))
                    while valor <= 0:
                        valor = int(input('Valor inválido. Deseja depositar quanto?:\n>>>'))

                    dados[id_origem]['Saldo'] += valor
                    print(f'{nome} realizou um depósito no valor de R${valor}')
                    with open('historico.txt', 'a', encoding='utf-8') as historico:
                        historico.write(f'➥{data}\n{nome} realizou um depósito no valor de R${valor}\n\n')


                elif menu == 2:
                    valor = int(input('Deseja sacar quanto?\n>>>'))
                    while valor <= 0 or valor > dados[id_origem]['Saldo']:
                        valor = int(input('Valor inválido ou saldo insuficiente. Digite novamente:\n>>>'))

                    dados[id_origem]['Saldo'] -= valor
                    print(f'{nome} realizou um saque no valor de R${valor}')
                    with open('historico.txt', 'a', encoding='utf-8') as historico:
                        historico.write(f'➥{data}\n{nome} realizou um saque no valor de R${valor}\n\n')


                elif menu == 3:
                    valor = int(input('Deseja transferir quanto?\n>>>'))
                    while valor <= 0 or valor > dados[id_origem]['Saldo']:
                        valor = int(input('Valor inválido ou saldo insuficiente. Digite novamente:\n>>>'))

                    modo = input('Quer fazer a transferência por ID ou por nome? [ID/NOME]\n>>>').strip().lower()
                    while modo not in ['id', 'nome']:
                        modo = input('Digite ID ou NOME corretamente:\n>>>').strip().lower()

                    id_destino = None

                    if modo == 'id':
                        entrada = input('Digite o ID do destinatário:\n>>>')
                        if entrada in dados and entrada != id_origem:
                            id_destino = entrada
                        else:
                            print('ID inválido ou é o seu próprio ID.')

                    elif modo == 'nome':
                        nome_destino = input('Digite o nome completo do destinatário:\n>>>').strip().title()
                        for id_busca in dados:
                            if dados[id_busca]['Nome'] == nome_destino and id_busca != id_origem:
                                id_destino = id_busca
                                break
                        if not id_destino:
                            print('Nome não encontrado ou é o seu próprio nome.')

                    if id_destino:
                        dados[id_origem]['Saldo'] -= valor
                        dados[id_destino]['Saldo'] += valor
                        print(f'{nome} fez uma transferência de R${valor:.2f} para {dados[id_destino]["Nome"]}.')
                        with open('historico.txt', 'a', encoding='utf-8') as historico:
                            historico.write(f'➥{data}\n{nome} fez uma transferência de R${valor:.2f} para {dados[id_destino]["Nome"]}.\n\n')
                    else:
                        print('Transferência cancelada.')
                with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

                return True
            else:
                print('Senha incorreta.')
                return False
    print('Usuário não encontrado.')
    return False

while True:
    print('\n=== MENU ===')
    print('1: Cadastrar')
    print('2: Entrar')
    print('3: Ver informações de todos os usuários')
    print('4: Sair')

    menu = int(input('Digite o menu:\n>>>'))
    while menu not in range(1, 5):
        menu = int(input('Digite corretamente:\n>>>'))
    
    if menu == 1:
        if cadastrar():
            break
    elif menu == 2:
        if entrar():
            break
    elif menu == 3:
        visualizar()
    elif menu == 4:
        break
