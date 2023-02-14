alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction == "encode" or direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
else:
    print("Please select \"encode\" or \"decode\".")


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        shift_num = alphabet.index(letter) + shift
        cipher_text += alphabet[shift_num]
    print(f"The encoded text is: {cipher_text}")

def decrypt(text, shift):
    decipher_text = ""
    for letter in text:
        shift_num = alphabet.index(letter) - shift
        decipher_text += alphabet[shift_num]
    print(f"The decoded text is: {decipher_text}")


if direction.lower() == "encode":
    encrypt(text, shift)
elif direction.lower() == "decode":
    decrypt(text, shift)