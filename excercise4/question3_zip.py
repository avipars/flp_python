
# %% Question 3
# Avraham Parshan 341419323
from tailrecurse import *


def sortedzip(L):
    """
    This function receives a list of lists, sorts each one of the sub-lists in ascending order (using the sorted
    built-in function, and not the sort method), applies the built-in zip function upon them, and returns the
    resulting list.
    """
    return zip(*[sorted(sublist) for sublist in L])


def reversedzip(L):
    """
     function receives a list of lists, reverses each one of the sub-lists (using the reversed built-in function,
and not the reverse method), applies the built-in zip function upon them, and returns the resulting list.
    """
    return zip(*[reversed(sublist) for sublist in L])


def funczip(func, L):
    """
     receives two parameters: a functional object func (which behaves similarly to sortedzip and
reversedzip), and a list of lists. The function will call func and pass L to it, and returns the result returned
by func.
    """
    return func(L)  # TODO see if right
    # return zip(*[func(sublist) for sublist in L])


def unzippy(L):
    """
This function receives a list of tuples L, of the kind that funczip returns. The function builds a list of lists
of the same kind that sortedzip or reversedzip expects to receive as parameter.
Note: At the beginning of the solution, you should create a list of empty lists. You could think that such a
list can be created by using N*[ ], but this does not work as you may expect; try to create that list of empty
lists using some alternative way    """
    if not L:
        return []

    # Transpose the list of tuples into a list of lists
    transposed = list(zip(*L))

    # Sort each list in the transposed structure
    sorted_lists = list(map(sorted, transposed))

    return sorted_lists


def done():
    print("Bye")
    sys.exit(0)


def main():
    L = [[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']]
    print(list(sortedzip(L)))

    print(list(reversedzip(L)))

    print(list(funczip(reversedzip, L)))

    print(list(unzippy(list(reversedzip(L)))))

    print("Menu")

    while True:
        li = eval(
            input("Enter a list of lists (each inside list is of same size N): "))
        if not isinstance(li, list):
            print("Input must be a list")
            return
        if not all(isinstance(sublist, list) for sublist in li):
            print("All elements must be lists")
            return
        elif not all(len(sublist) == len(li[0]) for sublist in li):
            print("All sublists must be of same size")
            return
        menu = {
            0: done,
            1: sortedzip,
            2: reversedzip,
        }
        print("1: sortedzip\n2: reversedzip\n 0: Exit")
        choice = int(input("Enter your choice: "))
        if choice == 0:
                break
        elif choice not in menu:
                print("Invalid choice")

        else:
                print(f"After function {menu[choice].__name__}:")
                print(list(menu[choice](li)))
            # apply unzippy & print
                print("After unzippy:")
                print(list(unzippy(menu[choice](li))))


if __name__ == "__main__":
    main()
