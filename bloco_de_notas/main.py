# Bloco de notas
from datetime import datetime
data = datetime.now().strftime('%d, %B %Y -> %H:%M:%S')

def view():
    global linhas
    linhas = 0

    for linha in arquivo.readlines():
        linhas += 1
        if linhas == 1:
            continue
        print(linha.strip())

with open('bloco-notas.txt', 'a+', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    conteudo = arquivo.read()

    senha = None
    if 'Senha' not in conteudo:
        senha = input('Defina uma senha: ').strip()
        arquivo.write(f'Senha: {senha}᚛\n')
        print('Senha Cadastrada!')

    inicio = conteudo.find(' ')
    fim = conteudo.find('᚛')

    password = conteudo[inicio+1:fim]

    verificacao = input('Digite a sua senha:\n>>>').strip()

    if verificacao == password or verificacao == senha:
        print('Acesso confirmado')
    else:
        while True:
            print('Acesso negado. Tente novamente ou digite "sair" para sair.')
            verificacao = input('Digite a sua senha:\n>>>').strip()

            if verificacao.lower() == 'sair':
                break

            elif verificacao == password or verificacao == senha:
                print('Acesso confirmado')
                break


    while True:
        if verificacao.lower() == 'sair':
            break

        # Opção de menus
        print('Opções do menu\n[1]: Ver meu bloco de notas\n[2]: Escrever no meu bloco de notas\n[3]: Sair')
        menu = int(input('O que deseja fazer?\n>>>'))

        while menu not in [1, 2, 3]:
            menu = int(input('Digite corretamente!\n>>>'))

        if menu == 1:
            arquivo.seek(0)
            if conteudo == '':
                print('Vazio!')
            else:
                view()
        elif menu == 2:
            texto = input('Modo escrita ativado. Digite no seu bloco de notas! [OBS: "/" para pular linha]\n>>>').strip()
            texto = texto.replace('/', '\n')
            arquivo.write(f'{data}\n{texto}\n\n')
            print('Enviado com sucesso!')
            break
        elif menu == 3:
            break
