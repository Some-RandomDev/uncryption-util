import sys
from funcs import *
mode = sys.argv[1]
algo = sys.argv[2]
inpF = open(sys.argv[3],"r")
outF = open(sys.argv[4],"w")
match mode:
    case '-e':
        match algo:
            case '-c':
                outF.write(caesarEnc(inpF.read(), int(sys.argv[5])))
            case '-r13':
                outF.write(caesarEnc(inpF.read(), 13))
            case '-a':
                outF.write(caesarEnc(inpF.read(), 1))
            case '-p':
                outF.write(playfairEnc(inpF.read(), sys.argv[5]))
            case '-v':
                outF.write(vigenereEnc(inpF.read(), sys.argv[5]))
    case '-d':
        match algo:
            case '-c':
                outF.write(caesarDec(inpF.read(), int(sys.argv[5])))
            case '-r13':
                outF.write(caesarDec(inpF.read(), 13))
            case '-a':
                outF.write(caesarDec(inpF.read(), 1))
            case '-p':
                outF.write(playfairDec(inpF.read(), sys.argv[5]))
            case '-v':
                outF.write(vigenereDec(inpF.read(), sys.argv[5]))
