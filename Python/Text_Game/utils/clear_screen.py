import os, platform
def cls():
    system = platform.system()
    match system:
        case 'Linux':
            os.system('clear')
        case 'Windows':
            os.system('cls')
