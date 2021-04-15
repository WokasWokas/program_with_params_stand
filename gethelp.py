try: # import modules
    import sys
    import os
    def params(): return sys.argv
    def currentpath(): return os.path.abspath(__file__)
except ModuleNotFoundError:
    exit("program: module 'sys' not found!")

def spaces(minValue: int = 0, maxValue: int = 10): # get spaces for format column
    return ' ' * (maxValue - minValue)

def paramsCheck(params: list = params()): # check params of command line
    for param in params:
        if param == '-h' or param == '--help': gethelp(exit_=True)

def gethelp(exit_: bool = False): # get help menu
    functions = [['-h', '--help', 'Get help menu']]
    print("Thank that use our program!\nIt's help menu need for you to use this program on first steps.")
    print('command', spaces(minValue=len(list('command')), maxValue=25) + 'functions')
    for function in functions:
        print(f'{function[0]}/{function[1]}:', spaces(minValue=len(list(f'{function[0]}/{function[1]}:')),
             maxValue=25) + f'{function[2]}')
    if exit_ == True: exit()
    

def update(): # opening main functions
    pass

def main(): # open program
    paramsCheck()
    update()

main()
