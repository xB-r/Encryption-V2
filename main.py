import random
import string
import re

print("**********_Encryptor V2_**********")

key = []
cipher_text = ""

while True:
    try:
        choice = int(input("Encryption(0) or Decryption(1) or 2 to exit: "))
    except ValueError:
        print("Invalid Choice, try again!")


    def encrypt():
        global cipher_text
        plain_text = str(input("Enter text: "))
        replace_num_list = []

        def generate_random_string(length):
            characters = string.ascii_letters + string.digits + string.punctuation
            final_string = ''.join(random.choice(characters) for _ in range(length))
            return final_string

        plain_text_length = int(len(plain_text) * random.uniform(2, 10))
        generated_string = [*generate_random_string(plain_text_length)]
        plain_text_split = [*plain_text]

        for z in range(plain_text_length):  # flag system needed to prevent overlap of replaces
            replace_num_list.append(z)

        for y in plain_text_split:
            replace_index = random.choice(replace_num_list)
            generated_string[replace_index] = y
            replace_num_list.remove(replace_index)
            key.append(replace_index)

        for x in range(0, len(generated_string)):
            cipher_text += generated_string[x]

        def key_creation():
            key_characters = string.ascii_letters + string.punctuation
            final_key = random.choice(key_characters).join(map(str, key))
            return final_key

        print("Encrypted text: " + cipher_text)
        print("Encryption key: " + key_creation())


    def decrypt():
        encrypted_text = str(input("Encrypted text: "))
        encryption_key = str(input("Encryption key: "))
        numbers = re.findall(r'\d+', encryption_key)
        split_key = [int(num) for num in numbers]

        decrypted_text = ''
        for i in split_key:
            decrypted_text += encrypted_text[i]

        print("Decrypted text: " + decrypted_text)

    # noinspection PyUnboundLocalVariable
    if choice == 0:
        encrypt()
    elif choice == 1:
        decrypt()
    elif choice == 2:
        break
    else:
        print("Invalid Choice, try again!")
