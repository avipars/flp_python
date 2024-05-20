# %% Question 8 random tuples
# avi parshan
# i switched to snake case to get used to python conventions
import random

def generate_random_tuple(min_choice, min_size, max_size):
    """
    program which creates a tuple containing N numbers (3 <= N <= 9) which will be randomly chosen from the closed interval [1,9]
    """
    tuple_size = random.randint(min_size, max_size) #includes both endpoints
    n = tuple_size
    print(tuple_size)

    rand_list = []
    while tuple_size > 0:
        tuple_size -= 1
        rand_list.append(random.randint(min_choice,max_size)) 
    rand_tuple = tuple(rand_list)
    return rand_tuple



def guess_test(rand_tuple,guess_tuple):
    """
    args: randomly generated tuple
    user guessed tuple
    return tuple with all guessed numbers that are in right space, and "X" in all not correct places
    """
    newList = []
    success = 0
    for i in range(len(rand_tuple)):
        if rand_tuple[i] == guess_tuple[i]:
            newList.append(rand_tuple[i])
            success += 1
        else:
            newList.append("X")

    return (tuple(newList), (success/len(rand_tuple) )*100)
    
def print_end_game(rand_tuple, perc):
    """
    print the end game message
    """
    print("the correct tuple is: ", rand_tuple)
    print("highest success rate is: ", perc, "%")


def user_guess(rand_tuple, n, min_choice, max_size):
    """
    user guessing stage
    """
    keep_going = True
    highest_percentage = 0
    while keep_going:
        # guess = eval(input(f"enter {n} integers in closed interval [{min_choice},{max_size}] as a tuple ie (1,2,1): "))
        guess_list = []
        # run from 0 to n-1 and ask user to input n numbers
        for i in range(n):
            user_input = input(f"enter a positive integer in closed interval [{min_choice},{max_size}]")
            if(user_input == "-1"): #if user inputs -1, exit the game
                keep_going = False #exit condition
                break
            else:
                guess_list.append(int(user_input))
        
        if not keep_going: #exit clause
            print("you exited the game") 
            print_end_game(rand_tuple, highest_percentage)
            keep_going = False
            break #exit the game

        # print the guess tuple and percentage of correct guesses
        retTuple, rate = guess_test(rand_tuple,tuple(guess_list))
        if(rate > highest_percentage):
            highest_percentage = rate

        print(retTuple)
        print("success rate: ", rate, "%")

        if rate == 100:
            print("you won!")
            print_end_game(rand_tuple, highest_percentage)
            keep_going = False
            break
        else:
            print("try to guess again")
            # repeat until user wins 
            keep_going = True
            continue

def main():
    min_choice = 1
    min_size = 3
    max_size = 9
    rand_tuple = generate_random_tuple(min_choice, min_size, max_size)
    print(rand_tuple) #only for debug purposes
    user_guess(rand_tuple, len(rand_tuple), min_choice, max_size)

if __name__ == "__main__":
    main()


# %%
