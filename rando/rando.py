# generate random number within range - use decimals too and seed by time
import random
import time

def main():
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    # Seed the random number generator with the current time
    random.seed(time.time())

    # Generate a random number within a specified range including decimals
    random_number = random.uniform(start, end)  # Example range from 0 to 100

    print(random_number)
    
    
if __name__ == "__main__":
    main()