# % menu with options for user to run any of the previous hw functions
from helpers import *
import question1_penta as q1
import question2_sum as q2
import question3_reverse as q3
import question4_palin as q4
import question5_series as q5
import question6_pi as q6
import question7_twin as q7
import question8_dict as q8


def check_input(inp):
    """
    basic input check
    """
    if isinstance(inp, int) and inp >= 0:
        return inp
    elif isinstance(inp, str) and inp.isnumeric() and int(inp) >= 0:
        return int(inp)
    else:
        return None


def main_menu():
    """
    main menu for user to select which function to run (recursion)
    """
    print("Please select an option from the menu :")
    print("""
          0: Quit
          1: Pentagonal Numbers
          2: Sum Digits
          3: Reverse Digits
          4: Palindrome
          5: Series
          6: Pi Digits
          7: Twin Primes
          8: Dictionaries
          """)

    options = {0: quit,
               1: q1.main,
               2: q2.main,
               3: q3.main,
               4: q4.main,
               5: q5.main,
               6: q6.main,
               7: q7.main,
               8: q8.main
               }
    
    inp = check_input(input("Enter your choice: "))
    if inp is not None and inp in options.keys():
        options[inp]() # run the function
        main_menu()
    else:
        print("Invalid input")
        main_menu()

def quit():
    print("Goodbye!")
    exit()

if __name__ == "__main__":
    main_menu()