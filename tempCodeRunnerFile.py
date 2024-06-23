int(f"You choose {reverseDict[you]} \nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("It is a draw")
else:
    if(computer == -1 and you == 1):
        print("You win")
    elif(computer == -1 and you == 0):
        print("You Lose")
    if(computer == 1 and you == -1):
        print("You Lose")
    elif(computer == 1 and you == 0):
        print("You win")
    if(computer == 0 and you == -1):
        print("You Win")
    elif(computer == 0 and you == 1):
        print("You Lose")
    else:
  