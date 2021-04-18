from random import randint
player_wins=0
computer_wins=0
winning_score=3

while player_wins<winning_score and computer_wins<winning_score:
	print("\t\trock...")
	print("\t\tpaper...")
	print("\t\tscissor...")
	print("Type quit or q while in game to quit..")
	print("Choose from the above 3 choices")
	
	player = input("Player, make your move: ").lower()
	if player=="quit" or player=="q":
		break
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
				print("Player wins!")
				player_wins+=1
			else:
				print("Computer wins!")
				computer_wins+=1
		elif player == "paper":
			if computer == "rock":
				print("Player wins!")
				player_wins+=1
			else:
				print("Computer wins!")
				computer_wins+=1
		elif player == "scissor":
			if computer == "paper":
				print("Player wins!")
				player_wins+=1
			else:
				print("Computer wins!")	
				computer_wins+=1
		else:
			print("Please enter a valid move!")
	else:
		print("Please Make a Choice...!!")
print(f"FINAL SCORE :  Player Score: {player_wins}  Computer Score: {computer_wins}")

if player_wins > computer_wins:
    print("CONGRATS :), YOU WON..!!")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else: 
    print("OH NO :( THE COMPUTER WON...")
   