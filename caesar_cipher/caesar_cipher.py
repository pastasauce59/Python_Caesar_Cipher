from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = True
print(logo)

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        def caesar(text, shift, direction):
            cipher_text = ""
            for letter in text:
                if direction.lower() == "encode":
                    shift_num = alphabet.index(letter) + shift
                    cipher_text += alphabet[shift_num]
                elif direction.lower() == "decode":
                    shift_num = alphabet.index(letter) - shift
                    cipher_text += alphabet[shift_num]
            print(f"Your {direction}d message is: {cipher_text}")

        caesar(text, shift, direction)

        continue_ = input("Do you want to continue ciphering/deciphering? Type \"Yes\" or \"No\" \n")
        if continue_.lower() != "yes":
            restart = False
        
    else:
        print("Please select \"encode\" or \"decode\".")