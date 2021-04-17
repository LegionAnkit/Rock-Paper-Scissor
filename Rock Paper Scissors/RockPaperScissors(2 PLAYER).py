print("\t\trock...")
print("\t\tpaper...")
print("\t\tscissor...")
print("Choose from the above 3 choices")
act=0
while act!='n':
    player1_choice = input("Player 1, Make your Choice :")
    player2_choice = input("Player 2, Make your Choice :")
    print("Shoot!!")
    # REFACTORED CODE
    if player1_choice and player2_choice:  # TO CHECK CHOICE VARIABLE ARE NOT EMPTY
        if player1_choice == player2_choice:
            print("Its a Tie.....")
        elif player1_choice == "rock":
            if player2_choice == "paper":
                print("Player 2 Wins.....")
            elif player2_choice == "scissor":
                print("Player 1 Wins.....")
        elif player1_choice == "paper":
            if player2_choice == "rock":
                print("Player 1 Wins.....")
            elif player2_choice == "scissor":
                print("Player 2 Wins.....")
        elif player1_choice == "scissor":
            if player2_choice == "rock":
                print("Player 2 Wins.....")
            elif player2_choice == "paper":
                print("Player 1 Wins.....")
        else:
            print("Something went wrong....!!")
    else:
        print("Please Make a Choice..!!")
    act = input("Want to play again (y/n)").lower()

print("THANK YOU FOR PLAYING")


# THIS WAS THE INITIAL CODE WHICH WAS REFACTORED INTO ABOVE CODE


# if player1_choice and player2_choice:
# 	if player1_choice=="rock" and player2_choice=="paper":
# 		print("Player 2 Wins.....")
# 	elif player1_choice=="rock" and player2_choice=="scissor":
# 		print("Player 1 Wins.....")
# 	elif player1_choice=="paper" and player2_choice=="rock":
# 		print("Player 1 Wins.....")
# 	elif player1_choice=="paper" and player2_choice=="scissor":
# 		print("Player 2 Wins.....")
# 	elif player1_choice=="scissor" and player2_choice=="rock":
# 		print("Player 2 Wins.....")
# 	elif player1_choice=="scissor" and player2_choice=="paper":
# 		print("Player 1 Wins.....")
# 	elif player1_choice==player2_choice:
# 		print("Its a Tie.....")
# 	else:
# 		print("Something went wrong....!!")
# else:
# 	print("Please Make a Choice..!!")


# ANOTHER APPROACH FOR RPS IS GIVEN BELOW
# p1 = input("Player 1: rock, paper, or scissors ")
# p2 = input("Player 2: rock, paper, or scissors ")

# if p1 == p2:
#     print("Draw")
# elif p1 == "rock" and p2 == "scissors":
#     print("p1 wins")
# elif p1 == "paper" and p2 == "rock":
#     print("p1 wins")
# elif p1 == "scissors" and p2 == "paper":
#     print("p1 wins")
# else:
#     print("p2 wins")
