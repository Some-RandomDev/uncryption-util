import sys
from funcs import *
mode = sys.argv[1]
algo = sys.argv[2]
match mode:
    case '-e':
        match algo:
            case '-c':
                print(caesarEnc(sys.argv[3], int(sys.argv[4])))
            case '-r13':
                print(caesarEnc(sys.argv[3], 13))
            case '-a':
                print(caesarEnc(sys.argv[3], 1))
    case '-d':
        match algo:
            case '-c':
                print(caesarDec(sys.argv[3], int(sys.argv[4])))
            case '-r13':
                print(caesarDec(sys.argv[3], 13))
            case '-a':
                print(caesarDec(sys.argv[3], 1))