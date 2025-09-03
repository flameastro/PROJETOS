import random


def quit_game():
    try:
        playing = input("Deseja continuar? (S/N)\n>>> ").upper().strip()

        while playing not in ["S", "N"]:
            playing = input("Por favor, digite corretamente (S/N):\n>>> ").upper().strip()

        return playing == "N"
    except ValueError as value_e:
        print(f"Erro de valor: {value_e}")
    except KeyboardInterrupt as keyboard_e:
        print(f"Erro de interrupção: {keyboard_e}")
    except Exception as e:
        print(f"Erro: {e}")


def game():
    try:
        try:
            with open("saldo.txt", "r") as f:
                f.seek(0)
                balance = int(f.read())

                if balance == 0:
                    balance = 5
        except:
            with open("saldo.txt", "w") as f:
                balance = 50
                f.write(str(balance))

        running = True

        print(f"Saldo atual: R${balance}")

        while running:
            die = random.randint(1, 6)

            bet_value = int(input("Digite o valor da aposta:\n>>> "))

            while bet_value > balance:
                bet_value = int(input(f"O valor da aposta não pode ser maior que o valor de saldo! ({bet_value} > {balance})\nDigite o valor da aposta:\n>>> "))

            choice = input("O dado vai cair acima de 3 (4, 5, 6) ou abaixo de 4 (3, 2, 1)? [acima/abaixo]:\n>>> ").lower().strip()
            while choice not in ["acima", "abaixo"]:
                choice = input("Por favor, digite corretamente.\nO dado vai cair acima de 3 (4, 5, 6) ou abaixo de 4 (3, 2, 1)? [acima/abaixo]:\n>>> ").lower().strip()
            if choice == "acima" and die > 3:
                print(f"Você ganhou! + {bet_value} reais.")
                balance += bet_value
            else:
                print(f"Você perdeu. - {bet_value} reais.")
                balance -= bet_value

            print(f"Valor do dado: {die}\nSaldo atual: {balance}")

            if balance <= 0:
                with open("saldo.txt", "w") as f:
                    f.write(str(balance))

                print("Saldo esgotado. Você perdeu!")
                break

            if quit_game():
                with open("saldo.txt", "w") as f:
                    f.write(str(balance))

                running = False

    except ValueError as value_e:
        print(f"Erro de valor: {value_e}")
    except KeyboardInterrupt as keyboard_e:
        print(f"Erro de interrupção: {keyboard_e}")
    except Exception as e:
        print(f"Erro: {e}")

game()
