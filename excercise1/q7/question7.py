# %%
"""
Question 7
Write a Python program that receives from the keyboard, the name of some text 
file, reads it from its beginning to its end, counts the number of occurrences of every 
word in the text, and prints every word and its number of occurrences, each in a 
different line. 
You are free to define every function that you think is necessary to write the 
program. Use the example file shakespeare.txt, provided to you with this exercises 
sheet. 
Some suggestions for the implementation of your solution
"""

def countWords(filename, delimiter = " "):
    try:
        with open(filename, "r") as file:
            words = file.read().split()
            wordDict = {}
            for word in words:
                word = word.lower().strip(delimiter)
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1 
            return wordDict
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print("An error occurred", e)
        return None

def saveToFile(dict, filename = "word_count.txt"):
    # put dictionary in txt file
    with open(filename, "w") as file: #this also overwrites file if already there
        for word, count in dict.items():
            file.write(f"{word}: {count}\n")

def printResults(dict):
    for word, count in dict.items():
        print(f"{word}: {count}")     #print results to console


def autoRun(delim = " "):
    """
    runs the program with the shakespeare.txt file and saves the results to a file
    """
    fname = "shakespeare.txt"
    res = countWords(fname,delim)
    # printResults(res) 
    saveToFile(res,"wordc_"+ fname)      # put dictionary in txt file

def humanRun(delim = " "):
    """
    runs the program with a file specified by the user and prints to console
    """
    fname = input("Enter the name of the file: ")
    res = countWords(fname,delim)
    printResults(res)
    # saveToFile(res)      # put dictionary in txt file

def main():
    delim = ",.!?:; "
    # autoRun(delim)
    humanRun(delim)
        
if __name__ == "__main__":
    main()