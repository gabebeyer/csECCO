import random 

numberToGuess = random.randrange(0,50)

tries = 3

while tries >= 0:

	if tries == 0:
		print "you lose!!! my number was %s" %numberToGuess
		break
	
	print "you have %s tries left" %tries

	guess = input("guess my number")
	
	if guess > numberToGuess:
		print "my number is smaller"
		tries -= 1
	elif guess < numberToGuess :
		print "my number is bigger"
		tries -=1
	else:
		print "you win!"

