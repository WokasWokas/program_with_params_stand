try: # import modules
    import sys
    import os
    def params(): return sys.argv
    def currentpath(): return os.path.abspath(__file__)
except ModuleNotFoundError:
    exit("ls: module 'sys' not found!")

def spaces(minValue: int = 0, maxValue: int = 10): # get spaces for format column
    return ' ' * (maxValue - minValue)

def paramsCheck(params: list = params()): # check params commands
    for param in params:
        if param == '-h' or param == '--help': gethelp(exit_=True)
        if param == '-cp' or param == '--curpath': getfiles(path='cur')

def gethelp(exit_: bool = False): # get help menu
    functions = [['-h', '--help', 'Get help menu'], ['-cp', '--curpath', 'Get files on current path']]
    print("Thank that use our program!\nIt's help menu need for you to use this program on first steps.")
    print('command', spaces(minValue=len(list('command')), maxValue=25) + 'functions')
    for function in functions:
        print(f'{function[0]}/{function[1]}:', spaces(minValue=len(list(f'{function[0]}/{function[1]}:')),
             maxValue=25) + f'{function[2]}')
    if exit_ == True: exit()

def getfiles(path: str): # get files with path
    if path == 'cur': path = '\\'.join([elem for elem in currentpath().split('\\') if elem != 'ls.py'])
    

def update(): # opening main functions
    pass

def main(): # open program
    paramsCheck()
    update()

main()
