import random

def intro():
    print("Guessing Game! Guess the number.")
    print()
    print()
    print()

def play(Max_num):
    number = random.randint(1, Max_num)
    print(f"The number is between 1 and {Max_num}\n")
    count = 1
    guess = int(input("Pick a number: "))

    while guess != number:
        if guess < number:
            print("Too low. Try again.")
            count +=1
        elif guess > number:
            print("Too high! Try again.")
            count +=1

        guess = int(input("Your guess: "))
    print(f"You guessed it in {count} tries. \n")

def main():
    intro()
    again = "y"
    while again.lower() == "y":
        Max_num = int(input("Enter the highest possible number: "))
        play(Max_num)
        again = input("Play again? (y/n): ")
        print()
        print()
    print("Goodbye!")

if __name__ == "__main__":
    main()



