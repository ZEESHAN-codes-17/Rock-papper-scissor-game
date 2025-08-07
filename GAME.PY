import random

print("welcome to Rock,Papper,Scissor")

print("press (S)cissors, (R)ock, (P)apper")


number = random.randint(1,3)

score = 0
computer_score = 0
choice = 0

while choice != 2:
  choice = int(input("press 1 to play and 2 to quit: "))  

  if choice == 1:
     USER = input("Choose your move: ").upper()
     if USER == "S" and number == 1:
       print("Mine was Scissor")
       print("its a tie")

     elif USER == "S" and number == 2:
        print("mine was paper")
        print("you won")
        score = score+1
     elif USER == "S" and number == 3:
        print("mine was rock")
        print("you lost")
        computer_score = computer_score + 1
  if choice == 1:
    #  USER = input("Choose your move: ")
     if USER == "R" and number == 1:
       print("Mine was Scissor")
       print("You won")
       score = score + 1
     elif USER == "R" and number == 2:
        print("mine was paper")
        print("you lost")
        computer_score += 1
     elif USER == "R" and number == 3:
        print("mine was rock")
        print("Its a tie")
  if choice == 1:
    # USER = input("Choose your move: ")
    if USER == "P" and number == 1:
      print("Mine was Scissor")
      print("YOU LOST")
      computer_score = computer_score +1

    elif USER == "P" and number == 2:
        print("mine was paper")
        print("ITS a tie")
    elif USER == "P" and number == 3:
        print("mine was rock")
        print("You won")
        score = score +1
        
  elif choice == 2:
     print("game closed")
  else:
    print("wrong choice")    


print("YOUR SCORE IS: ", score)
print("COMPUTER SCORE: ",computer_score)
if score > computer_score:
   print("user won")
elif computer_score > score:
   print("COMPUTER WON")
else:
   print("its a tie")          

              
      



