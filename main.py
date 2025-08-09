''' 
1 for rock
2 for paper
3 for scissor
'''
import random  # To let computer pick a random choice

# Dictionary to map user input (full word now) to numbers
yourdict = {"rock": 1, "paper": 2, "scissor": 3}

# Dictionary to map numbers back to string for printing
reversedict = {1: "rock", 2: "paper", 3: "scissor"}

choice = True  # Loop control variable

print("Welcome to Rock-Paper-Scissors Game!")
print("Rules: Rock beats Scissor, Paper beats Rock, Scissor beats Paper.")
print("---------------------------------------------------------------")

while choice:
    # Computer randomly chooses 1, 2, or 3
    computer = random.choice([1, 2, 3])
    
    # Asking user for choice (full word now)
    youstr = input("Enter your choice (rock, paper, scissor): ").lower()

    # Convert user choice from string to number
    you = yourdict[youstr]

    # Display both choices
    print(f"You chose {reversedict[you]}")
    print(f"Computer chose {reversedict[computer]}")

    # Compare choices to decide result
    choice = False
    if computer == you:
        print("It's a draw!")
    else:
        if computer == 1 and you == 2:
            print("🎉 You won!")
        elif computer == 1 and you == 3:
            print("😢 You lost!")
        elif computer == 2 and you == 1:
            print("😢 You lost!")
        elif computer == 2 and you == 3:
            print("🎉 You won!")
        elif computer == 3 and you == 1:
            print("🎉 You won!")
        else:
            print("😢 You lost!")

    # Ask if user wants to continue
    again = input("Do you want to continue? (y or n): ").lower()
    if again == "y":
        choice = True
    else:
        print("Thanks for playing! Have a great day! 😊")
