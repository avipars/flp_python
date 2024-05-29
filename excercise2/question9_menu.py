# % menu with options for user to run any of the previous hw functions
from helpers import *
import question1_penta as p1

def check_input(inp):
    if isinstance(inp, int) and inp >= 0:
        return inp
    elif isinstance(inp, str) and inp.isnumeric() and int(inp) >= 0:
        return int(inp)
    else:
        return None
def main_menu():
    print("Please select an option from the menu :")
    # choice = int(input())
    print("0. Quit\n1. Penta\n")
    # menu_dict = {0: ("Quit", lambda a: print("1")), 1: ("Penta", print("tbd"))}
    dict2 = {0: p1.main(),5: p2(),3: p2, 2: lambda b: print("1"),1: lambda a: quit, 7: p3}
    # print(*menu_dict)
    # print(menu_dict[0][0])
    print(dict2[0])
    # print the menu options without executing functions
    # for key, value in menu_dict.items():
    #     print(key, value[0])
def p2():
    print("p2")

def p3():
    print("p3")
def quit():
    print("Goodbye!")
    exit()
    
if __name__ == "__main__":
    main_menu()