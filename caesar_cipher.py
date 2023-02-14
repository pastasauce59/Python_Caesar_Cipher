alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
else:
    print("Please select \"encode\" or \"decode\".")


def encrypt(text, shift):
    #Creating a slice range with 'x', then slicing range from alphabet with 'y' and then adding it to alphabet to make 'new_alphabet'
    #This is to avoid index being out of range when letters in the alphabet are close to the end, such as z, based on the assumption
    #that the alphabet variable above cannot be hard coded changed.
    x = slice(shift)
    y = alphabet[x]
    new_alphabet = alphabet + y
    cipher_text = ""
    for letter in text:
        shift_num = new_alphabet.index(letter) + shift
        cipher_text += new_alphabet[shift_num]
    print(cipher_text)

def decrypt(text, shift):
    print("decoding...")


if direction.lower() == "encode":
    encrypt(text, shift)
elif direction.lower() == "decode":
    decrypt(text, shift)