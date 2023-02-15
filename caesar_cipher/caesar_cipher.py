from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = True
def caesar(text, shift, direction):
    cipher_text = ""
    #This clever piece of logic below will divide any shift number greater than 26 into a remainder that will fit inside the alphabet list above.
    shift = shift % 26
    for char in text:
        if char in alphabet:
            if direction.lower() == "encode":
                shift_num = alphabet.index(char) + shift
                cipher_text += alphabet[shift_num]
            elif direction.lower() == "decode":
                shift_num = alphabet.index(char) - shift
                cipher_text += alphabet[shift_num]
        else:
            cipher_text += char
    print(f"Your {direction}d message is: {cipher_text}")
print(logo)

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(text, shift, direction)

        continue_ = input("Do you want to continue ciphering/deciphering? Type \"Yes\" or \"No\" \n")
        if continue_.lower() != "yes":
            restart = False
            print("Goodbye.")
        
    else:
        print("Please select \"encode\" or \"decode\".")