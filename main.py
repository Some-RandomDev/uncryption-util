def ceaserEnc(file:str, key:int) -> str:
    out = ''
    for char in file:
        if char.isalpha():
            out+=chr(ord(char)+key-26*int(not chr(ord(char)+key).isalpha()))
        else:
            out+=char
    return out


def ceaserDec(file:str, key:int) -> str:
    out = ''
    for char in file:
        if char.isalpha():
            out+=chr(ord(char)-key+26*int(not chr(ord(char)+key).isalpha()))
        else:
            out+=char
    return out

if __name__ == '__main__':
    enc = ceaserEnc(input(), int(input()))
    print(enc)
    dec = ceaserDec(enc, int(input()))
    print(dec)