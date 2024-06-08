
# %% Question 2 text processing
# Avraham Parshan 341419323
from tailrecurse import *

def categorize_characters(word):
    """Categorize characters in the word into vowels and consonants in specified ranges."""

    vowel_list = [char for char in word if char in 'aeiou']
    consonants_b_to_m = [char for char in word if char in 'bcdefghijklm']
    consonants_n_to_z = [char for char in word if char in 'nopqrstuvwxyz']
    
    return (vowel_list, consonants_b_to_m, consonants_n_to_z)


def treatline(lineNr:int, line:str):
    """Process the line and return a dictionary with categorized characters."""
    if lineNr <= 0:
        return -1
    
    words = line.strip().split()
    
    if not all(word.isalpha() for word in words): #if non ascii chars
        return -1

    word_dict = {word: categorize_characters(word) for word in words} # create the dictionary
    
    return (lineNr, word_dict)  # return the line number and the dictionary
    
def treatxtfile(flname:str):
    """Process the text file and return a list of dictionaries."""
    try:
        with open(flname, 'r') as file:
            return [treatline(i, line) for i, line in enumerate(file, 1)]
    except FileNotFoundError:
        return -1
    
def main():
    # print(treatline(1, "people enjoy programming \n"))
    
    print(treatxtfile("D:\NewComp\DevProjects\JCT\functional_logic\python_code\excercise4\text.txt"))
if __name__ == "__main__":
    main()