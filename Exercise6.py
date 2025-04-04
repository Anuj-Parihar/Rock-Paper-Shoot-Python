import random
print("stone, Paper, and Scessior Game\n let's start😍")
permission = str(input("enter YES or yes  for staritng the game:"))
userWinCount=0
computerWinCount=0

def roles():
    print("\n\nThe game of Stone, Paper, Scissors follows these common roles:") 
    print("1. Rock beats Scissors: Rock smashes scissors, so rock wins against scissors.")  
    print("2. Scissors beats Paper: Scissors cut paper, so scissors win against paper.  ")
    print("3. Paper beats Rock: Paper wraps rock, so paper wins against rock. ") 
    print("4. Tie rule: If both players choose the same item, the round is a tie. ") 
    print("5. Best of rounds: The game is usually played in rounds, and the player with the most wins is the overall winner.")
    print("6. rounds: each game contain three rounds")

def game(n):
    print(f"\n\n\nthis is a round: {n}")
    print("Number 1 for Stone \t Number 2 for Paper \t Number 3 for Scissors")
    user = int(input("Enter the Number between 1 to 3 : "))
    computer_genrated_number = random.choice([1,2,3])
    print(f"user select Number: {user}")
    print(f"computer select Number: {computer_genrated_number}")
    if( user == computer_genrated_number):
        print("Particular round is draw")
    elif(user == 1 and computer_genrated_number == 3 or user == 2 and computer_genrated_number == 1 or user == 3 and computer_genrated_number == 2):
        print("user win the particular round.")
        global userWinCount 
        userWinCount += 1
    else:
        print("Computer win the particular round")
        global computerWinCount
        computerWinCount += 1
     
def totalScore():
    if(userWinCount == computerWinCount):
        return " Match is Tie..."
    elif(userWinCount > computerWinCount):
        return"User Win the match Sucessfully..."
    else:
        return "Computer win the match Sucessfully..."

if(permission == 'yes' or permission =='YES'):
    roles()
    i=1
    while(i<=3):
        game(i)
        i=i+1
    print("\n\nTotal Score- \n")
    print(f"User Total Win's: {userWinCount}")
    print(f"Computer Total Win's: {computerWinCount}")
    result = totalScore()
    print(f"Result: {result}")

else:
    print("try again and entered valid input")