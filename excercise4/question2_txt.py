
# %% Question 2 text processing
# Avraham Parshan 341419323
from tailrecurse import *


def categorize_characters(word):
    """Categorize characters in the word into vowels and consonants in specified ranges."""
    vow = set('aeiou')
    consonants_b = set('bcdfghjklm')
    consonants_n = set('npqrstvwxyz')
    vowel_list = [char for char in word if char in vow]
    consonants_b_to_m = [char for char in word if char in consonants_b]
    consonants_n_to_z = [char for char in word if char in consonants_n]

    return (vowel_list, consonants_b_to_m, consonants_n_to_z)


def treatline(lineNr: int, line: str):
    """Process the line and return a dictionary with categorized characters."""
    if lineNr <= 0:
        return -1

    words = line.strip().split()

    if not all(word.isalpha() for word in words):  # if non ascii chars
        return -1

    word_dict = {word: categorize_characters(
        word) for word in words}  # create the dictionary

    return (lineNr, word_dict)  # return the line number and the dictionary


def treatxtfile(flname: str):
    """Process the text file and return a list of dictionaries."""
    try:
        with open(flname, 'r') as file:
            return [treatline(i, line) for i, line in enumerate(file, 1)]
    except FileNotFoundError:
        return -1

# def occursumary(fldict:dict):
#     """
#     This function receives one parameter: fldict (a dictionary of the kind that the function treatxtfile
#     returns). The function will create a new dictionary in which every key is the number of the corresponding
#     line in the text file, and the value bound to it is a tuple containing three elements: the first element is the
#     the number of vowels that occur in that line, the second element is the number of consonants between
#     b and m that occur in that line, and the third element is the number of consonants between n and z that
#     occur in that line.
#     """
#     #TODO finish this
#     new_dict = {}
#     for key, value in fldict.items():
#         new_dict[key] = (sum(len(word[0]) for word in value.values()), sum(len(word[1]) for word in value.values()), sum(len(word[2]) for word in value.values()))
#     return new_dict


def occursumary(fldict: dict):
    """
     This function receives one parameter: fldict (a dictionary of the kind that the function treatxtfile
     returns). The function will create a new dictionary in which every key is the number of the corresponding 
     line in the text file, and the value bound to it is a tuple containing three elements: the first element is the 
     the number of vowels that occur in that line, the second element is the number of consonants between 
     b and m that occur in that line, and the third element is the number of consonants between n and z that 
     occur in that line.
    """
    summary_dict = {}
    for lineNr, word_dict in fldict:
        vowel_count = sum(len(word[0]) for word in word_dict.values())
        consonants_b_count = sum(len(word[1]) for word in word_dict.values())
        consonants_n_count = sum(len(word[2]) for word in word_dict.values())
        summary_dict[lineNr] = (
            vowel_count, consonants_b_count, consonants_n_count)
    return summary_dict


def user_inp():
    """Get user input for file path."""
    fl = input("Please enter the file path: ")
    print(occursumary(treatxtfile(fl)))
    print("")


def main():
    # print(treatline(1, "people enjoy programming \n"))
    # escape the file path
    fpath = "D:\\NewComp\\DevProjects\\JCT\\functional_logic\\python_code\\excercise4\\text.txt"
    # # print(treatxtfile(fpath))
    # print("LineNr nr of vowels nr of b-m consonants nr of n-z consonants")
    # print(occursumary(treatxtfile(fpath)))

    user_inp()


if __name__ == "__main__":
    main()
