import string

plain_text = input("Write the text you want to encrypt: ")
shift = 3

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)
