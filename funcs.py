def caesarEnc(file:str, key:int) -> str:
    out = ''
    for char in file:
        if char.isalpha():
            out+=chr(ord(char)+key-26*(not (chr(ord(char)+key).isalpha() and chr(ord(char)+key).isupper()==char.isupper())))
        else:
            out+=char
    return out


def caesarDec(file:str, key:int) -> str:
    out = ''
    for char in file:
        if char.isalpha():
            out+=chr(ord(char)-key+26*(not (chr(ord(char)-key).isalpha() and chr(ord(char)-key).isupper()==char.isupper())))
        else:
            out+=char
    return out

#PLAYFAIR-----------------------------------------------------------------
#Encryption------------------------------------------
def toLowerCase(text):
    return text.lower()

def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText

def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])

        group = i
    Diagraph.append(text[group:])
    return Diagraph

def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else:
                new_word = text
    return new_word


list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generateKeyTable(word, list1):
    key_letters = []
    for i in word:
        if i not in key_letters:
            key_letters.append(i)

    compElements = []
    for i in key_letters:
        if i not in compElements:
            compElements.append(i)
    for i in list1:
        if i not in compElements:
            compElements.append(i)

    matrix = []
    while compElements != []:
        matrix.append(compElements[:5])
        compElements = compElements[5:]

    return matrix


def search(mat, element):
    for i in range(5):
        for j in range(5):
            if(mat[i][j] == element):
                return i, j


def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4:
        char1 = matr[e1r][0]
    else:
        char1 = matr[e1r][e1c+1]

    char2 = ''
    if e2c == 4:
        char2 = matr[e2r][0]
    else:
        char2 = matr[e2r][e2c+1]

    return char1, char2


def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4:
        char1 = matr[0][e1c]
    else:
        char1 = matr[e1r+1][e1c]

    char2 = ''
    if e2r == 4:
        char2 = matr[0][e2c]
    else:
        char2 = matr[e2r+1][e2c]

    return char1, char2


def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]

    char2 = ''
    char2 = matr[e2r][e1c]

    return char1, char2


def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])

        if ele1_x == ele2_x:
            c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y:
            c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else:
            c1, c2 = encrypt_RectangleRule(
                Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText

def playfairEnc(inp_text, key):
    inp_text = inp_text.split(' ')
    enc_text = ''

    key = toLowerCase(key)
    Matrix = generateKeyTable(key, list1)

    for i in inp_text:
        i = removeSpaces(toLowerCase(i))
        PlainTextList = Diagraph(FillerLetter(i))
        if len(PlainTextList[-1]) != 2:
            PlainTextList[-1] = PlainTextList[-1]+'z'
        
        CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

        CipherText = ""
        for i in CipherList:
            CipherText += i
        enc_text += CipherText + ' '
    return enc_text

#Decryption------------------------------------------
import numpy as np

def to_lower_case(text):	
    return text.lower()

def remove_spaces(text):
    return text.replace(" ", "")

def generate_key_table(key):
    key = remove_spaces(to_lower_case(key))
    key = key.replace('j', 'i')
    key = ''.join(dict.fromkeys(key))

    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key_table = [c for c in key if c in alphabet]

    for char in alphabet:
        if char not in key_table:
            key_table.append(char)

    key_table = np.array(key_table).reshape(5, 5)
    return key_table

def Search(key_table, a, b):
    if a == 'j':
        a = 'i'
    if b == 'j':
        b = 'i'

    p1 = p2 = None
    for i in range(5):
        for j in range(5):
            if key_table[i, j] == a:
                p1 = (i, j)
            elif key_table[i, j] == b:
                p2 = (i, j)
    return p1, p2

def decrypt(cipher, key):
    key_table = generate_key_table(key)
    deciphered = []

    for i in range(0, len(cipher), 2):
        p1, p2 = Search(key_table, cipher[i], cipher[i+1])

        if p1[0] == p2[0]:
            deciphered.append(key_table[p1[0], (p1[1]-1)%5])
            deciphered.append(key_table[p2[0], (p2[1]-1)%5])
        elif p1[1] == p2[1]:
            deciphered.append(key_table[(p1[0]-1)%5, p1[1]])
            deciphered.append(key_table[(p2[0]-1)%5, p2[1]])
        else:
            deciphered.append(key_table[p1[0], p2[1]])
            deciphered.append(key_table[p2[0], p1[1]])

    return ''.join(deciphered)

def playfairDec(cipher, key):
    cipher = cipher.split(' ')
    dec_text = ''

    for i in cipher:
        decrypted_text = decrypt(i, key)
        dec_text += decrypted_text + ' '
    return dec_text


#VIGENERE---------------------------------------
def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenereEnc(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def vigenereDec(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

def enc_vigenere(inp_text, key):
    inp_text = inp_text.split(' ')
    enc_text = ''

    for i in inp_text:
        encrypted_text = encrypt_vigenere(i, key)
        enc_text += encrypted_text + ' '
    return enc_text

def dec_vigenere(inp_text, key):
    inp_text = inp_text.split(' ')
    dec_text = ''

    for i in inp_text:
        decrypted_text = decrypt_vigenere(i, key)
        dec_text += decrypted_text + ' '
    return dec_text


if __name__ == '__main__':
    enc = playfairEnc(input('Text: '), input('Key: '))
    print(enc)
    dec = playfairDec(enc, input('Key: '))
    print(dec)