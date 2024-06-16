"""
Generator version of hw4 - poet question from q3
"""
import random

peopleNames = ("Lucy", "Ester", "Pesach", "Howard",
               "Menachem", "Dovid", "Dovi", "Bowser","Harvey")
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

def generateSentence():
    """Generate 1 sentence given a random choice"""
    person = random.choice(peopleNames)
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    object_choice = random.choice((animateObjects + inanimateObjects))
    adverb = random.choice(adverbs)
    return f"{person} {verb} {adjective} {object_choice} {adverb}"



def crPoem(N):
    """
    combine N sentences randomly generated
    """
    for i in range(0,N): # for N sentences
        yield generateSentence() # yield the sentence
    
def main():
    num = int(input("Enter number of lines for poem "))
    if num <= 0:
        print("Invalid number of lines")
        return

    for i in crPoem(num):
        print(i, end="\n")
    print()


if __name__ == "__main__":
    main()