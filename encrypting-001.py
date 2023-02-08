### Program developed by Prof. MSc. Paulo O. Formigoni, PhD ###
### profpauloformigoni@gmail.com ###

### This program uses the input function to read the user's passphrase and key.
### Then the program uses a for loop to go through each letter in the phrase and encrypt it using the key.
### The alphabet variable stores the letters of the alphabet for easy encryption.
### The index function is used to find the position of the letter in the alphabet string.
### Next, the position of the cipher letter is calculated using the formula (pos + key) % 26.
### Finally, the cipher letter is added to the cipher_phrase string.

# Asking user to enter phrase
frase = input("Type a phrase: ")

# Pedindo ao usuário para digitar a chave
chave = int(input("Enter key (integer): "))

# Encrypting the sentence
alfabeto = "abcdefghijklmnopqrstuvwxyz"
frase_cifrada = ""
for letra in frase:
    if letra.lower() in alfabeto:
        pos = alfabeto.index(letra.lower())
        pos = (pos + chave) % 26
        letra_cifrada = alfabeto[pos]
        if letra.isupper():
            letra_cifrada = letra_cifrada.upper()
        frase_cifrada += letra_cifrada
    else:
        frase_cifrada += letra

# Creating the text file
with open("criptoFormigoni01.txt", "w") as arquivo:
    arquivo.write(frase_cifrada)

print("The cipher phrase has been successfully saved to the file 'criptoFormigoni01.txt'.")