ferro = int(input('Quantos ferros você tem?: '))
ouro = int(input('Quantos ouros você tem?: '))
diamante = int(input('Quantos diamantes você tem?: '))
# E a questão sobre unidades?... E sobre a criação da barrinha de fome e vida?

while True:
    print('Mercante'.center(25, '-'))
    numero = int(input('Digite um número:\n1: bloco       3: armadura\n2: arma        4: suplemento, itens e ferramentas\n'))
    if numero == 1:
        num_bloco = int(input('Qual bloco?:\n1: lã(1 ferro)            3: madeira(4 ouros)\n2: concreto(10 ferros)      4: obsidiana(3 diamantes)\n'))
        
        if num_bloco == 1:
            la = 1 # lã = 1 ferro
            print(f'O preço da lã é {la} ferro')
            quantidade = int(input('Quantas lãs deseja?: '))
            valor = la * quantidade # Lã atual
            if valor > ferro:
                print('Oops! Ferro insuficiente!')
                break
            else:
                resultado = ferro - valor # Ferro atual
                ferro = resultado
                print(f'Você tem {resultado} ferros e {quantidade} lãs')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

        elif num_bloco == 2:
            concreto = 10
            print(f'O preço do concreto são {concreto} ferros')
            quantidade = int(input('Quantos concretos deseja?: '))
            valor = concreto * quantidade
            if valor > ferro:
                print('Oops! Ferro insuficiente!')
                break
            else:
                resultado = ferro - valor
                ferro = resultado
                print(f'Você tem {resultado} ferros e {quantidade} concreto')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

        elif num_bloco == 3:
            madeira = 4
            print(f'O preço da madeira são {madeira} ouros')
            quantidade = int(input('Quantas madeiras deseja?: '))
            valor = madeira * quantidade
            if valor > ouro:
                print('Oops! ouro insuficiente!')
                break
            else:
                resultado = ouro - valor
                ouro = resultado
                print(f'Você tem {resultado} ouros e {quantidade} concretos')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

        elif num_bloco == 4:
            obsidiana = 3
            print(f'O preço da obsidiana é {obsidiana} diamante')
            quantidade = int(input('Quantas obsidianas deseja?: '))
            valor = obsidiana * quantidade 
            if valor > diamante:
                print('Oops! diamante insuficiente!')
                break
            else:
                resultado = diamante - valor
                diamante = resultado
                print(f'Você tem {resultado} diamantes e {quantidade} obsidianas')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

    elif numero == 2:
        num_arma = int(input('Qual a arma?:\n1: espada de madeira(1 ferro)        4: espada de diamante(8 diamantes)\n2: espada de pedra(20 ferros)          5: arco(15 ouros)\n3: espada de ferro(6 ouros)          6: flechas(2 ouros)\n'))
        if num_arma == 1:
            espada_de_madeira = 1
            print(f'O preço da espada de madeira é {espada_de_madeira} ferro')
            quantidade = int(input('Quantas espadas de madeira deseja?: '))
            valor = espada_de_madeira * quantidade
            if valor > ferro:
                print('Oops! Ferro insuficiente!')
                break
            else:
                resultado = ferro - valor
                ferro = resultado
                print(f'Você tem {resultado} ferros e {quantidade} Espada de madeira')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

        elif num_arma == 2:
            espada_de_pedra = 20
            print(f'O preço da espada de pedra são {espada_de_pedra} ferros')
            quantidade = int(input('Quantas espadas de pedra deseja?: '))
            valor = espada_de_pedra * quantidade
            if valor > ferro:
                print('Oops! Ferro insuficiente!')
                break
            else:
                resultado = ferro - valor
                ferro = resultado
                print(f'Você tem {resultado} ferros e {quantidade} espada de pedra')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

        elif num_arma == 3:
            espada_de_ouro = 6
            print(f'O preço da espada de ouro são {espada_de_ouro} ouros')
            quantidade = int(input('Quantas espadas de ouro deseja?: '))
            valor = espada_de_ouro * quantidade
            if valor > ouro:
                print('Oops! Ouro insuficiente!')
                break
            else:
                resultado = ouro - valor
                ouro = resultado
                print(f'Você tem {resultado} ouros e {quantidade} espada de ouro')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

        elif num_arma == 4:
            espada_de_diamante = 8
            print(f'O preço da espada de diamante são {espada_de_diamante} diamante')
            quantidade = int(input('Quantas espadas de diamante deseja?: '))
            valor = espada_de_diamante * quantidade
            if valor > diamante:
                print('Oops! diamantes insuficiente!')
                break
            else:
                resultado = diamante - valor
                diamante = resultado
                print(f'Você tem {resultado} diamantes e {quantidade} espada de diamante')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

        elif num_arma == 5:
            arco = 15
            print(f'O preço do arco são {arco} ouros')
            quantidade = int(input('Quantos arcos deseja?: '))
            valor = arco * quantidade
            if valor > ouro:
                print('Oops! ouro insuficiente!')
                break
            else:
                resultado = ouro - valor
                ouro = resultado
                print(f'Você tem {resultado} ouros e {quantidade} arco')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

        elif num_arma == 6:
            flecha = 2
            print(f'O preço da flecha são {flecha} ouros')
            quantidade = int(input('Quantas flechas deseja?: '))
            valor = flecha * quantidade
            if valor > ouro:
                print('Oops! ouro insuficiente!')
                break
            else:
                resultado = ouro - valor
                ouro = resultado
                print(f'Você tem {resultado} ouros e {quantidade} arco')
                continuar = input('Deseja continuar?: ')
                continuar = continuar.lower()
                if continuar == 'sim':
                    continue
                else:
                    total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                    print(total)
                    break

    elif numero == 3: # Armadura
        parte_armadura = int(input('Qual é a parte da armadura?:\n1: capacete(dependente)        3: calça(dependente)\n2: peitoral(dependente)        4: bota(dependente)\n'))
        if parte_armadura == 1: # capacete
            tipo_armadura = int(input('Qual o tipo?:\n1: couro(1 ferro)        3: ferro(3 ouros)\n2: aluminio(10 ferros)        4: diamante(4 diamantes)\n'))
            if tipo_armadura == 1: # capacete de couro
                capacete_de_couro = 1
                print(f'O preço do capacete de couro é {capacete_de_couro} ferro')
                quantidade = int(input('Quantos capacetes deseja?: '))
                valor = capacete_de_couro * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    ferro = resultado
                    print(f'Você tem {resultado} ferros e {quantidade} capacete de couro')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif tipo_armadura == 2: # capacete de alumínio
                capacete_de_aluminio = 10
                print(f'O preço do capacete de alumínio é {capacete_de_aluminio} ferros')
                quantidade = int(input('Quantos capacetes deseja?: '))
                valor = capacete_de_aluminio * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    ferro = resultado
                    print(f'Você tem {resultado} ferros e {quantidade} capacete de alumínio')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif tipo_armadura == 3: # capacete de ferro
                capacete_de_ferro = 3
                print(f'O preço do capacete de ferro é {capacete_de_ferro} ouros')
                quantidade = int(input('Quantos capacetes deseja?: '))
                valor = capacete_de_ferro * quantidade
                if valor > ouro:
                    print('Oops! ouro insuficiente!')
                    break
                else:
                    resultado = ouro - valor
                    ouro = resultado
                    print(f'Você tem {resultado} ouros e {quantidade} capacete de ferro')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif tipo_armadura == 4: # capacete de diamante
                capacete_de_diamante = 4
                print(f'O preço do capacete de diamante é {capacete_de_diamante} diamantes')
                quantidade = int(input('Quantos capacetes deseja?: '))
                valor = capacete_de_diamante * quantidade
                if valor > diamante:
                    print('Oops! diamante insuficiente!')
                    break
                else:
                    resultado = diamante - valor
                    diamante = resultado
                    print(f'Você tem {resultado} diamantes e {quantidade} capacete de diamante')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break
        
        elif parte_armadura == 2: # peitoral
            tipo_armadura = int(input('Qual o tipo?:\n1: couro(1 ferro)        2: ferro(20 ferros)\n3: ouro(6 ferros)         4: diamante(8 diamantes)\n'))
            if tipo_armadura == 1: # peitoral de couro
                peitoral_de_couro = 1
                print(f'O preço do peitoral de couro são {peitoral_de_couro} ferro')
                quantidade = int(input('Quantos peitorais deseja?: '))
                valor = peitoral_de_couro * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    ferro = resultado
                    print(f'Você tem {resultado} ferros e {quantidade} peitoral de couro')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif tipo_armadura == 2: # peitoral de alumínio
                peitoral_de_aluminio = 20
                print(f'O preço do peitoral de alumínio são {peitoral_de_aluminio} ferros')
                quantidade = int(input('Quantos peitorais deseja?: '))
                valor = peitoral_de_aluminio * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    ferro = resultado
                    print(f'Você tem {resultado} ferros e {quantidade} peitoral de alumínio')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif tipo_armadura == 3: # peitoral de ferro
                peitoral_de_ferro = 6
                print(f'O preço do peitoral de ferro são {peitoral_de_ferro} ouros')
                quantidade = int(input('Quantos peitorais deseja?: '))
                valor = peitoral_de_ferro * quantidade
                if valor > ouro:
                    print('Oops! ouro insuficiente!')
                    break
                else:
                    resultado = ouro - valor
                    ouro = resultado
                    print(f'Você tem {resultado} ouros e {quantidade} peitoral de ferro')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif tipo_armadura == 4: # peitoral de diamante
                peitoral_de_diamante = 8
                print(f'O preço do peitoral de diamante são {peitoral_de_diamante} diamantes')
                quantidade = int(input('Quantos peitorais deseja?: '))
                valor = peitoral_de_diamante * quantidade
                if valor > diamante:
                    print('Oops! diamante insuficiente!')
                    break
                else:
                    resultado = diamante - valor
                    diamante = resultado
                    print(f'Você tem {resultado} diamantes e {quantidade} peitoral de diamante')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

        elif parte_armadura == 3: # calça
            tipo_armadura = int(input('Qual o tipo?:\n1: couro(1 ferro)        2: ferro(20 ferros)\n3: ouro(6 ouros)         4: diamante(8 diamantes)\n'))
            if tipo_armadura == 1: # calça de couro
                calca_de_couro = 1
                print(f'O preço do calca de couro é {calca_de_couro} ferro')
                quantidade = int(input('Quantas calças deseja?: '))
                valor = calca_de_couro * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    ferro = resultado
                    print(f'Você tem {resultado} ferros e {quantidade} calça de couro')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            if tipo_armadura == 2: # calça de aluminio
                calca_de_aluminio = 20
                print(f'O preço do calca de aluminio são {calca_de_aluminio} ferros')
                quantidade = int(input('Quantas calças deseja?: '))
                valor = calca_de_aluminio * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    ferro = resultado
                    print(f'Você tem {resultado} ferros e {quantidade} calça de aluminio')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            if tipo_armadura == 3: # calça de ferro
                calca_de_ferro = 6
                print(f'O preço do calca de ferro são {calca_de_ferro} ouros')
                quantidade = int(input('Quantas calças deseja?: '))
                valor = calca_de_ferro * quantidade
                if valor > ouro:
                    print('Oops! ouro insuficiente!')
                    break
                else:
                    resultado = ouro - valor
                    ouro = resultado
                    print(f'Você tem {resultado} ouros e {quantidade} calça de ferro')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            if tipo_armadura == 4: # calça de diamante
                calca_de_diamante = 8
                print(f'O preço do calca de diamante são {calca_de_diamante} diamantes')
                quantidade = int(input('Quantas calças deseja?: '))
                valor = calca_de_diamante * quantidade
                if valor > diamante:
                    print('Oops! diamante insuficiente!')
                    break
                else:
                    resultado = diamante - valor
                    diamante = resultado
                    print(f'Você tem {resultado} diamantes e {quantidade} calça de diamante')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

        if parte_armadura == 4: # bota
            tipo_armadura = int(input('Qual o tipo?:\n1: couro(1 ferro)        3: ouro(3 ouros)\n2: ferro(20 ferros)         4: diamante(4 diamantes)\n'))
            if tipo_armadura == 1: # bota de couro
                bota_de_couro = 1
                print(f'O preço da bota de couro é {bota_de_couro} ferro')
                quantidade = int(input('Quantas botas deseja?: '))
                valor = bota_de_couro * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    ferro = resultado
                    print(f'Você tem {resultado} ferros e {quantidade} bota de couro')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            if tipo_armadura == 2: # bota de aluminio
                bota_de_aluminio = 10
                print(f'O preço da bota de aluminio são {bota_de_aluminio} ferros')
                quantidade = int(input('Quantas botas deseja?: '))
                valor = bota_de_aluminio * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    ferro = resultado
                    print(f'Você tem {resultado} ferros e {quantidade} bota de aluminio')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            if tipo_armadura == 3: # bota de ferro
                bota_de_ferro = 3
                print(f'O preço da bota de aluminio são {bota_de_ferro} ouros')
                quantidade = int(input('Quantas botas deseja?: '))
                valor = bota_de_ferro * quantidade
                if valor > ouro:
                    print('Oops! ouro insuficiente!')
                    break
                else:
                    resultado = ouro - valor
                    ouro = resultado
                    print(f'Você tem {resultado} ouros e {quantidade} bota de ferro')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            if tipo_armadura == 4: # bota de diamante
                bota_de_diamante = 8
                print(f'O preço da bota de diamante são {bota_de_diamante} diamantes')
                quantidade = int(input('Quantas botas deseja?: '))
                valor = bota_de_diamante * quantidade
                if valor > diamante:
                    print('Oops! diamante insuficiente!')
                    break
                else:
                    resultado = diamante - valor
                    diamante = resultado
                    print(f'Você tem {resultado} diamantes e {quantidade} bota de diamante')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

    elif numero == 4: # consumo e itens
        cons_itens_tools = int(input('Digite um número:\n1: Consumo\n2: Itens'))
        if cons_itens_tools == 1:
            consumo = int(input('Qual suplemento?:\n 1: Pão(+5 fome)\n2: Frango Assado(+8 fome)\n3: HP(+5 vida)\n4: Envenenamento(-1 HP/s)\n5: Velocidade(2x)\n6: Pulo(+2)'))
            if consumo == 1: # Pão
                pao = 10
                print(f'O preço do pão são {pao} ferros')
                quantidade = int(input('Quantos pãos deseja?: '))
                valor = pao * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    print(f'Você tem {resultado} ferros e {quantidade} pão')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif consumo == 2: # Frango Assado
                frango = 1
                print(f'O preço do frango é {frango} ouro')
                quantidade = int(input('Quantos frangos deseja?: '))
                valor = frango * quantidade
                if valor > ouro:
                    print('Oops! ouro insuficiente!')
                    break
                else:
                    resultado = ouro - valor
                    print(f'Você tem {resultado} ouros e {quantidade} frango')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif consumo == 3: # HP
                pocao_hp = 5
                print(f'O preço das poções de hp são {pocao_hp} ouro')
                quantidade = int(input('Quantas poções de hp deseja?: '))
                valor = pocao_hp * quantidade
                if valor > ouro:
                    print('Oops! ouro insuficiente!')
                    break
                else:
                    resultado = ouro - valor
                    print(f'Você tem {resultado} ouros e {quantidade} poção de hp')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif consumo == 4: # Envenenamento
                pocao_envenenamento = 5
                print(f'O preço das poções de envenenamento são {pocao_envenenamento} ouros')
                quantidade = int(input('Quantas poções de envenenamento deseja?: '))
                valor = pocao_envenenamento * quantidade
                if valor > ouro:
                    print('Oops! ouro insuficiente!')
                    break
                else:
                    resultado = ouro - valor
                    print(f'Você tem {resultado} ouros e {quantidade} poção de envenenamento')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif consumo == 5: # Velocidade
                pocao_velocidade = 5
                print(f'O preço das poções de velocidade são {pocao_velocidade} ouros')
                quantidade = int(input('Quantas poções de velocidade deseja?: '))
                valor = pocao_velocidade * quantidade
                if valor > ouro:
                    print('Oops! ouro insuficiente!')
                    break
                else:
                    resultado = ouro - valor
                    print(f'Você tem {resultado} ouros e {quantidade} poção de velocidade')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

            elif consumo == 6: # Pulo
                pocao_pulo = 5
                print(f'O preço das poções de pulo são {pocao_pulo} ouros')
                quantidade = int(input('Quantas poções de pulo deseja?: '))
                valor = pocao_pulo * quantidade
                if valor > ouro:
                    print('Oops! ouro insuficiente!')
                    break
                else:
                    resultado = ouro - valor
                    print(f'Você tem {resultado} ouros e {quantidade} poção de pulo')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                        print(total)
                        break

        elif cons_itens_tools == 2:
            itens = int(input('Qual item quer?:\n1: Picareta\n2: Machado\n3: Tesoura'))
            if itens == 1: # Picareta
                tipo_picareta = int(input('Qual o tipo?:\n1: Madeira\n2: Pedra\n3: Ferro\n4: Diamante'))
                if tipo_picareta == 1: # Picareta de madeira
                    picareta_madeira = 1
                    print(f'O preço da picareta de madeira é {picareta_madeira} ferro')
                    quantidade = int(input('Quantas picaretas deseja?: '))
                    valor = picareta_madeira * quantidade
                    if valor > ferro:
                        print('Oops! ferro insuficiente!')
                        break
                    else:
                        resultado = ferro - valor
                        ferro = resultado
                        print(f'Você tem {resultado} ferros e {quantidade} picareta de madeira')
                        continuar = input('Deseja continuar?: ')
                        continuar = continuar.lower()
                        if continuar == 'sim':
                            continue
                        else:
                            total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                            print(total)
                            break

                if tipo_picareta == 2: # Picareta de Pedra
                    picareta_pedra = 15
                    print(f'O preço da picareta de pedra são {picareta_pedra} ferros')
                    quantidade = int(input('Quantas picaretas deseja?: '))
                    valor = picareta_pedra * quantidade
                    if valor > ferro:
                        print('Oops! ferro insuficiente!')
                        break
                    else:
                        resultado = ferro - valor
                        ferro = resultado
                        print(f'Você tem {resultado} ferros e {quantidade} picareta de pedra')
                        continuar = input('Deseja continuar?: ')
                        continuar = continuar.lower()
                        if continuar == 'sim':
                            continue
                        else:
                            total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                            print(total)
                            break

                if tipo_picareta == 3: # Picareta de Ferro
                    picareta_ferro = 6
                    print(f'O preço da picareta de ferro são {picareta_ferro} ouros')
                    quantidade = int(input('Quantas picaretas deseja?: '))
                    valor = picareta_ferro * quantidade
                    if valor > ouro:
                        print('Oops! ouro insuficiente!')
                        break
                    else:
                        resultado = ouro - valor
                        ouro = resultado
                        print(f'Você tem {resultado} ouros e {quantidade} picareta de ferro')
                        continuar = input('Deseja continuar?: ')
                        continuar = continuar.lower()
                        if continuar == 'sim':
                            continue
                        else:
                            total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                            print(total)
                            break

                if tipo_picareta == 4: # Picareta de Diamante
                    picareta_diamante = 8
                    print(f'O preço da picareta de diamante são {picareta_diamante} diamantes')
                    quantidade = int(input('Quantas picaretas deseja?: '))
                    valor = picareta_diamante * quantidade
                    if valor > diamante:
                        print('Oops! diamante insuficiente!')
                        break
                    else:
                        resultado = diamante - valor
                        diamante = resultado
                        print(f'Você tem {resultado} diamantes e {quantidade} picareta de diamante')
                        continuar = input('Deseja continuar?: ')
                        continuar = continuar.lower()
                        if continuar == 'sim':
                            continue
                        else:
                            total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                            print(total)
                            break

            elif itens == 2: # Machado
                tipo_machado = int(input('Qual o tipo?:\n1: Madeira\n2: Pedra\n3: Ferro\n4: Diamante'))
                if tipo_machado == 1: # Machado de madeira
                    machado_madeira = 1
                    print(f'O preço do machado de madeira é {machado_madeira} ferro')
                    quantidade = int(input('Quantos machados deseja?: '))
                    valor = machado_madeira * quantidade
                    if valor > ferro:
                        print('Oops! ferro insuficiente!')
                        break
                    else:
                        resultado = ferro - valor
                        ferro = resultado
                        print(f'Você tem {resultado} ferros e {quantidade} machado de madeira')
                        continuar = input('Deseja continuar?: ')
                        continuar = continuar.lower()
                        if continuar == 'sim':
                            continue
                        else:
                            total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                            print(total)
                            break

                if tipo_machado == 2: # Machado de Pedra
                    machado_pedra = 15
                    print(f'O preço do machado de pedra são {machado_pedra} ferros')
                    quantidade = int(input('Quantos machados deseja?: '))
                    valor = machado_pedra * quantidade
                    if valor > ferro:
                        print('Oops! ferro insuficiente!')
                        break
                    else:
                        resultado = ferro - valor
                        ferro = resultado
                        print(f'Você tem {resultado} ferros e {quantidade} machado de pedra')
                        continuar = input('Deseja continuar?: ')
                        continuar = continuar.lower()
                        if continuar == 'sim':
                            continue
                        else:
                            total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                            print(total)
                            break

                if tipo_machado == 3: # Machado de Ferro
                    machado_ferro = 6
                    print(f'O preço da machado de ferro são {machado_ferro} ouros')
                    quantidade = int(input('Quantos machados deseja?: '))
                    valor = machado_ferro * quantidade
                    if valor > ouro:
                        print('Oops! ouro insuficiente!')
                        break
                    else:
                        resultado = ouro - valor
                        ouro = resultado
                        print(f'Você tem {resultado} ouros e {quantidade} machado de ferro')
                        continuar = input('Deseja continuar?: ')
                        continuar = continuar.lower()
                        if continuar == 'sim':
                            continue
                        else:
                            total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                            print(total)
                            break

                if tipo_machado == 4: # Machado de Diamante
                    machado_diamante = 8
                    print(f'O preço do machado de diamante são {machado_diamante} diamantes')
                    quantidade = int(input('Quantos machados deseja?: '))
                    valor = machado_diamante * quantidade
                    if valor > diamante:
                        print('Oops! diamante insuficiente!')
                        break
                    else:
                        resultado = diamante - valor
                        diamante = resultado
                        print(f'Você tem {resultado} diamantes e {quantidade} machado de diamante')
                        continuar = input('Deseja continuar?: ')
                        continuar = continuar.lower()
                        if continuar == 'sim':
                            continue
                        else:
                            total = {'Ferros:': ferro, 'Ouros': ouro, 'Diamantes:': diamante}
                            print(total)
                            break

            elif itens == 3: # Tesoura
                tesoura = 2
                print(f'O preço da tesoura é {tesoura} ferros')
                quantidade = int(input('Quantas tesouras deseja?: '))
                valor = tesoura * quantidade
                if valor > ferro:
                    print('Oops! ferro insuficiente!')
                    break
                else:
                    resultado = ferro - valor
                    ferro = resultado
                    print(f'Você tem {resultado} ferros e {quantidade} tesoura')
                    continuar = input('Deseja continuar?: ')
                    continuar = continuar.lower()
                    if continuar == 'sim':
                        continue
                    else:
                        total = {}
                        print(total)

inventario = {
    'Blocos': {
        'lã': 0,
        'concreto': 0,
        'madeira': 0,
        'obsidiana': 0,
    },
    'Arma': {
        'espada_madeira': 0,
        'espada_pedra': 0,
        'espada_ferro': 0,
        'espada_diamante': 0,
        'arco': 0,
        'flecha': 0,
    },
    'Armadura': {
        'capacete': 0,
        'peitoral': 0,
        'calça': 0,
        'bota': 0,
    },
    'Consumo/Itens': {
        'Pão': 0,
        'Frango': 0,
        'HP': 0,
        'Envenenamento': 0,
        'Velocidade': 0,
        'Pulo': 0,
        'Picareta': 0,
        'Machado': 0,
        'Tesoura': 0,
    }
}
inventario['Blocos']['lã'] += quantidade
for a, i in inventario.items():
    print(a, i)

arquivo = open('all/BG.txt', 'a')
arquivo.write(f'ferro: {ferro}, ouro: {ouro}, diamante: {diamante}\n')
arquivo.close()
