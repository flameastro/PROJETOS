print("==== Bem vindo ao jogo da forca ====")
print("Você pode digitar letra por letra, ou simplesmente chutar a palavra, mas se errar a palavra, perde na hora. Boa Sorte!\n")
import random
escolha = random.randint(1, 4)

def forca():
    if tentativas < 6:
        pos1 = 'o'
    else:
        pos1 = ' '

    if tentativas < 5:
        pos2 = '|'
    else:
        pos2 = ' '

    if tentativas < 4:
        pos3 = '-'
    else:
        pos3 = ' '

    if tentativas < 3:
        pos4 = '-'
    else:
        pos4 = ' '

    if tentativas < 2:
        pos5 = '/'
    else:
        pos5 = ' '

    if tentativas < 1:
        pos6 = '\\'
    else:
        pos6 = ' '
    print(f"""
_ _ _ _ _     {f"Letras: {', '.join(letras)}"}
|       |
|       {pos1}
|      {pos3}{pos2}{pos4}
|      {pos5} {pos6}
|
""")

animais = ["cachorro", "gato", "tigre", "elefante", "girafa", "zebra", "cavalo", "porco", "vaca", "coelho", "urso", "raposa", "lobo", "jacaré", "pato", "ganso", "coruja", "cobra", "pinguim", "golfinho", "baleia", "polvo", "lagarto", "rinoceronte", "hipopótamo", "macaco", "tartaruga"]

objetos = ["caneta", "caderno", "livro", "celular", "notebook", "controle", "teclado", "mouse", "carregador", "garrafa", "copo", "mochila", "estojo", "janela", "porta", "espelho", "chave", "panela", "prato", "garfo", "colher", "fone", "lanterna"]

comidas = ["arroz", "pizza", "lasanha", "frango", "bife", "salada", "batata frita", "ovo", "peixe", "cenoura", "banana", "melancia", "abacaxi", "uva", "morango", "queijo", "presunto", "bolo", "sorvete", "pipoca", "iogurte", "chocolate", "biscoito"]

moveis = ["cadeira", "mesa", "cama", "estante", "banco", "prateleira", "espelho", "geladeira"]
if escolha == 1:
    dica = 'animal'
    palavra = random.choice(animais)
elif escolha == 2:
    dica = 'objeto'
    palavra = random.choice(objetos)
elif escolha == 3:
    dica = 'comida'
    palavra = random.choice(comidas)
elif escolha == 4:
    dica = 'móvel'
    palavra = random.choice(moveis)

for letra in palavra:
    letra = palavra.split(' ')

ficticio = []
for repeticao in palavra:
    repeticao = repeticao.lower()
    if repeticao == ' ':
        ficticio.append('-')
    else:
        ficticio.append('_')

print(f'Dica: {dica}')

letras = []
tentativas = 6
while tentativas > 0:
    forca()

    if '_' not in ficticio:
        print('Você acertou!!')
        break

    print(' '.join(ficticio))
    
    letra = input('Digite uma letra: ').strip().lower()
    if letra == palavra:
        print('Você acertou!')
        break
    elif len(letra) == len(palavra):
        print('Você errou!')
        break
    else:
        while len(letra) != 1 or not letra.isalpha() or letra in letras:
            if letra == palavra:
                print('Você errou!')
                break
            elif len(letra) == len(palavra):
                print('Você acertou!')
                break
            print('Digite novamente.')
            letra = input('Digite uma letra: ').strip().lower()
        if len(letra) == len(palavra) or letra == palavra:
            break


    letras.append(letra)

    contador = 0
    for repeticao in palavra:
        if repeticao == letra:
            ficticio[contador] = letra
        contador += 1

    if letra not in palavra:
        tentativas -=1
        if tentativas != 0:
            print(f'Tentativas restantes: {tentativas}')

if tentativas == 0:
    print(f'A palavra era {palavra}')
    forca()
print(f'Resposta: {palavra}')
