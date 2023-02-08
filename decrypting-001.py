### Program developed by Prof. MSc. Paulo O. Formigoni, PhD ###
### profpauloformigoni@gmail.com ###

### This program uses the input function to read the user's key.
### Then, the program uses the with clause to open the file "cryptoFormigoni01.txt" and read
### the content of the cipher phrase. Then the program uses a for loop to go through each letter
### of the cipher phrase and decrypt it using the key. The calculation of the position of the decrypted
### letter is similar to the previous program, but uses the formula (pos - key) % 26 instead of (pos + key) % 26.
### Finally, the decrypted phrase is printed on the screen


# Asking the user to enter the key
chave = int(input("Enter key (integer): "))

# Abrindo o arquivo de texto
with open("criptoFormigoni01.txt", "r") as arquivo:
    frase_cifrada = arquivo.read()

# Descriptografando a frase
alfabeto = "abcdefghijklmnopqrstuvwxyz"
frase = ""
for letra in frase_cifrada:
    if letra.lower() in alfabeto:
        pos = alfabeto.index(letra.lower())
        pos = (pos - chave) % 26
        letra_descifrada = alfabeto[pos]
        if letra.isupper():
            letra_descifrada = letra_descifrada.upper()
        frase += letra_descifrada
    else:
        frase += letra

# Printing the decrypted phrase
print("Decrypted phrase:")
print(frase)