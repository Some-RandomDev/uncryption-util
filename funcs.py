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

if __name__ == '__main__':
    enc = caesarEnc(input(), int(input()))
    print(enc)
    dec = caesarDec(enc, int(input()))
    print(dec)