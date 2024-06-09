
# %% Question 2 text processing
# Avraham Parshan 341419323
from tailrecurse import *
from functools import reduce
import operator

vow = set('aeiou')
consonants_b = set('bcdfghjklm')
consonants_n = set('npqrstvwxyz')
    
def categorize_characters(word):
    """Categorize characters in the word into vowels and consonants in specified ranges.
    return tuple and inside are lists of vowel chars in word, consonants b to m and consonants n to z
    """
    return (categorize(word,vow), categorize(word,consonants_b), categorize(word, consonants_n))

def categorize(word, letter_set):
    """Given a word and set, find the occurrences of x and put in a list of chars"""
    return [char for char in word if char in letter_set]

def counter(word, letter_set):
    """counts occurrences of x in word"""
    return sum(1 for char in word if char in letter_set)


def treatline(lineNr: int, line: str):
    """Process the line and return a dictionary with categorized characters."""
    if lineNr <= 0:
        return -1
    line = line.lower()

    words = line.strip().split() # clean the array 
    if not all(word.isalpha() for word in words):  # if non ascii chars
        return -1

    word_dict = {word: categorize_characters(
        word) for word in words}  # create the dictionary

    return (lineNr, word_dict)  # return the line number and the dictionary


def treatxtfile(flname: str):
    """Process the text file and return a list of dictionaries."""
    try:
        with open(flname, 'r') as file: #open for reading
            return [treatline(i, line) for i, line in enumerate(file, 1)]
    except FileNotFoundError:
        return -1

def occursumary(fldict: dict):
    """
    This function receives one parameter: fldict (a dictionary of the kind that the function treatxtfile
    returns). The function will create a new dictionary in which every key is the number of the corresponding 
    line in the text file, and the value bound to it is a tuple containing three elements: the first element is the 
    number of vowels that occur in that line, the second element is the number of consonants between 
    b and m that occur in that line, and the third element is the number of consonants between n and z that 
    occur in that line.
    """
    vow = set('aeiou')
    consonants_b = set('bcdfghjklm')
    consonants_n = set('npqrstvwxyz')

    # Helper function to aggregate counts for a single line
    def aggregate_counts(word_dict):
        vowels_count = sum(map(counter, word_dict.keys(), vow))
        consonants_b_count = sum(
            map(counter, word_dict.keys(), consonants_b))
        consonants_n_count = sum(
            map(counter, word_dict.keys(), consonants_n))
        return (vowels_count, consonants_b_count, consonants_n_count)

    # Using map and reduce to build the summary dictionary without explicit loops
    summary_dict = dict(
        map(lambda line: (line[0], aggregate_counts(line[1])), fldict))

    return summary_dict


def parsedict(fldict: dict):
    """print in readable format without for loop"""
    print("LineNr nr of vowels nr of b-m consonants nr of n-z consonants")
    fn = lambda x: print(f"{x}    {fldict[x]}")
    list(map(fn, fldict.keys()))


def summarydict(fldict: dict):
    print("Nr of Lines in text total nr of vowels total nr of b-m consonants total nr of n-z consonants")
    # print summary without for loops
    lineNr = len(list(fldict.keys()))
    vowels = sum([fldict[line][0] for line in fldict.keys()])
    consonants_b = sum([fldict[line][1] for line in fldict.keys()])
    consonants_n = sum([fldict[line][2] for line in fldict.keys()])
    print(f"{lineNr}     {vowels}       {consonants_b}     {consonants_n}")


def user_inp():
    """Get user input for file path."""
    fl = input("Please enter the file path: ")
    res = occursumary(treatxtfile(fl))
    print("")
    parsedict(res)
    summarydict(res)


def main():
    user_inp()


if __name__ == "__main__":
    main()
