from datetime import datetime
import json

data = datetime.now().strftime('%d, %B/%Y -> %H:%M:%S')

with open('login.json', 'a+', encoding='utf-8') as login:
    login.seek(0)
    conteudo = login.read()

    if 'Nome' not in conteudo:
        nome = input('Digite o seu nome:\n>>>').strip().title()

        dados = {
            'Nome': nome
        }

        json.dump(dados, login)
    
with open('login.json', 'r', encoding='utf-8') as login:
    dados = json.load(login)
    name = dados['Nome']

def visualizar():
    with open('tarefas.txt', 'r', encoding='utf-8') as tarefas:
        tarefas.seek(0)
        conteudo = tarefas.read()
        print('=== LISTA DE TAREFAS ===')
        print(conteudo)

def escrever():
    with open('tarefas.txt', 'a', encoding='utf-8') as tarefas:
        escrita = input('Qual tarefa?\n>>>').strip()
        tarefas.write(f'➥ {escrita}\n')

def remover():
    with open('tarefas.txt', 'r', encoding='utf-8') as tarefas:
        tarefas.seek(0)
        conteudo = tarefas.read()
        if conteudo == '':
            print('Não é possível remover tarefas. A lista de tarefas está vazia')
        else:
            remocao = input('Digite a tarefa que deseja remover:\n>>>').strip()
            if remocao in conteudo:
                conteudo = conteudo.replace(f'➥ {remocao}\n', '')

                with open('tarefas.txt', 'w', encoding='utf-8') as tarefas:
                    tarefas.write(conteudo)
            else:
                print('Não foi possível achar a tarefa!')

def tarefas_concluidas():
    with open('concluidas.txt', 'a+', encoding='utf-8') as concluidas:
        concluidas.seek(0)
        conteudo = concluidas.read()
        tarefa = input('Digite a tarefa concluida:\n>>>').strip()

        with open('tarefas.txt', 'r', encoding='utf-8') as tarefas:
            tarefas.seek(0)
            conteudo = tarefas.read()

            if conteudo == '':
                print('Não é possível marcar tarefas como concluídas. A lista de tarefas está vazia')
            else:
                if tarefa in conteudo:
                    conteudo = conteudo.replace(f'➥ {tarefa}\n', '')
                    concluidas.write(f'{data}\n{name} conclui a tarefa "{tarefa}"\n\n')
                    print('Tarefa marcada como concluída com sucesso.')

                    with open('tarefas.txt', 'w', encoding='utf-8') as tarefas:
                        tarefas.write(conteudo)
                else:
                    print('Não foi possível achar a tarefa!')

while True:
    visualizar()
    print('\n=== MENU ===\n')
    print('1: Adicionar uma tarefa')
    print('2: Remover uma tarefa')
    print('3: Marcar tarefa como concluida')
    print('4: Sair')

    menu = int(input('O que deseja fazer?\n>>>'))
    while menu not in range(1, 5):
        menu = int(input('Digite corretamente:\n>>>'))

    if menu == 1:
        escrever()
    elif menu == 2:
        remover()
    elif menu == 3:
        tarefas_concluidas()
    elif menu == 4:
        break
