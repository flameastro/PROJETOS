LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar_cipher(text: str, quantity: int):
    if quantity > 15 or quantity < 1:
        return "The required amount is more than 1 and less than 15."

    final_text = ""

    try:
        for letter in text:
            if letter.isalpha():
                initial_pos = LETTERS.index(letter)
                final_pos = initial_pos+quantity

                calc_text = final_pos - 26

                if calc_text >= 0:
                    final_letter = LETTERS[calc_text]
                else:
                    final_letter = LETTERS[final_pos]

                final_text += final_letter

            else:
                final_text += letter

        return final_text

    except Exception as e:
        return f"error: {e}"

try:
    user_text = input("Enter the text you want to encrypt:\n>>>")
    user_quantity = int(input("Enter the amount of encryption:\n>>>"))
except Exception as e:
    print(f"error: {e}")

print(cesar_cipher(user_text, user_quantity))
