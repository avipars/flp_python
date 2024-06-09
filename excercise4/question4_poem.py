
# %% Question 4 poem
# Avraham Parshan 341419323
from tailrecurse import *
import random
peopleNames = ("Lucy", "Ester", "Pesach", "Howard",
               "Menachem", "Dovid", "Dovi", "Bowser")
verbs = ("loves", "eats", "admires", "fears",
         "respects", "hugs", "lifts", "slays", "reads")
adjectives = ("beautiful", "ugly", "wise", "stupid",
              "cunning", "small", "tall", "red", "green")
adverbs = ("slowly", "now", "soon", "suddenly",
           "never", "cunningly", "smartly", "stupidly")
animateObjects = ("oranges", "dogs", "cats", "birds",
                  "fishes", "elephants", "flowers", "computers")
inanimateObjects = ("a stone", "a chair", "a car", "a sword",
                    "a bag", "a bus", "a hat", "a cat")


# Generate a single sentence
def generate_sentence():
    person = random.choice(peopleNames)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    object_choice = random.choice((animateObjects + inanimateObjects))
    adverb = random.choice(adverbs)
    return f"{person} {verb} {adjective} {object_choice} {adverb}"

# Recursive function to create N sentences


@tail_call_optimized
def crPoem(N, poem=""):
    if N <= 0:  # base case, no more poems to print
        return poem
    sentence = generate_sentence()  # generate 1 sentence
    # call 1 level down (append to string)
    return crPoem(N - 1, poem + sentence + "\n")


def theHumblePoet(N):
    poem = crPoem(N)  # calls recursive function
    print(poem)  # print all


def main():
    num = int(input("Enter number of lines for poem "))
    if num <= 0:
        print("Invalid number of lines")
        return

    theHumblePoet(num)  # call function


if __name__ == "__main__":
    main()
