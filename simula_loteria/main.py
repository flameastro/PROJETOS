from random import randint


def get_machine_sorted_numbers():
    """
    Essa função retorna os números sorteados da máquina de 1 a 60.
    """

    machine_numbers = []

    for _ in range(6):
        sorted_number = randint(1, 60)
        while sorted_number in machine_numbers:
            sorted_number = randint(1, 60)

        machine_numbers.append(sorted_number)

    return machine_numbers


def get_user_sorted_numbers():
    """
    Essa função retorna os números que o usuário escolheu.
    """

    user_numbers_list = []

    for _ in range(6):
        try:
            user_number = int(input("Digite um número:\n>>>"))

            while user_number > 60 or user_number < 1:
                user_number = int(input("O número deve ser entre 1 a 60.\n"
                                        "Digite um número:\n>>>"))

            while user_number in user_numbers_list:
                user_number = int(input("Este número já foi sorteado.\n"
                                        "Digite um número:\n>>>"))

            user_numbers_list.append(user_number)
        except Exception as error:
            return f"Erro: {error}. Tente Novamente."

    return user_numbers_list


def verify_correct_numbers():
    """
    Essa função é responsável por verificar quais números o
    usuário acertou em relação aos números da máquina.
    """
    machine_numbers = get_machine_sorted_numbers()
    user_numbers_list = get_user_sorted_numbers()

    correct_answers = 0
    money = 0
    correct_numbers = []

    for machine_number in machine_numbers:
        for user_number in user_numbers_list:
            if user_number == machine_number:
                correct_numbers.append(user_number)
                correct_answers += 1
                money += 750000

    return (
        f"Sua lista de números: {user_numbers_list}\n"
        f"A lista de números do computador: {machine_numbers}\n"
        f"Números em comum: {"Nenhum" if not correct_numbers else
                             correct_numbers}\n"
        f"Quantidade de acertos: {correct_answers}\n"
        f"Dinheiro: {money}"
    )


print(verify_correct_numbers())
