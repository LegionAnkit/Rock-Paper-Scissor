from random import randint
print("\t\trock...")
print("\t\tpaper...")
print("\t\tscissor...")
print("Choose from the above 3 choices")
act=0 
while act!='n':
	player = input("Player, make your move: ").lower()
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissor"

	print(f"Computer plays {computer}" )
	#AFTER REFRACTING
	if player:
		if player == computer:
			print("It's a tie!")
		elif player == "rock":
			if computer == "scissor":
				print("player wins!")
			else:
				print("computer wins!")
		elif player == "paper":
			if computer == "rock":
				print("player wins!")
			else:
				print("computer wins!")
		elif player == "scissor":
			if computer == "paper":
				print("player wins!")
			else:
				print("computer wins!")	
		else:
			print("Please enter a valid move!")
	else:
		print("Please Make a Choice...!!")
	act = input("Want to play again (y/n)").lower()
 
print("THANK YOU FOR PLAYING")


#BEFORE REFRACTING 

# if player: 
# 	if player==computer:
# 		print("Its a Tie.....")
# 	elif player=="rock":
# 		if computer=="paper":
# 			print("Computer Wins.....")
# 		elif computer=="scissor":
# 			print("Player Wins.....")
# 	elif player=="paper":
# 		if computer=="rock":
# 			print("Player Wins.....")
# 		elif computer=="scissor":
# 			print("Computer Wins.....")
# 	elif player=="scissor":
# 		if computer=="rock":
# 			print("Computer Wins.....")
# 		elif computer=="paper":
# 			print("Player Wins.....")
# 	else:
# 		print("Something went wrong....!!")
# else:
# 	print("Please Make a Choice..!!")


