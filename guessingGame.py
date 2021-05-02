import random
number = random.randint(1, 9)
chances = 0
print("Number Guessing Game")
print("Remember, you only have 5 chances!")
while chances<5:
	guess = int(input("Enter your guess: "))
	if guess==number:
		print("You won! Congratulations!!")
		break
	elif guess<number:
		print("Number is too low. Choose a higher number.")
	else:
		print("Number is too high. Choose a lower number.")
	chances+=1
if chances>=5:
	print("Chances are finished. You lose!!")