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
    case '-d':
        match algo:
            case '-c':
                outF.write(caesarDec(inpF.read(), int(sys.argv[4])))
            case '-r13':
                outF.write(caesarDec(inpF.read(), 13))
            case '-a':
                outF.write(caesarDec(inpF.read(), 1))
