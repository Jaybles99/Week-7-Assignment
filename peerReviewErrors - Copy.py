# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <John Gerkin>
# Creation Date: <22 Sept>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time
#While loop condition is doing an assignment and not a comparison in both of the cases
#The comparison should have double equals for the comparisons
#that identifies the typo of checkcave where it should be camel cases as checkCave
#typo in checkCaves where it says to return "caves" but should be "cave" (singular)
#another typo is the 'Gobbles you down...' which is not setup properly as a parameter to the print function
#add an open paren after the print and a close paren after the string
#it does not currently require the Do your job and any to play again prompt to enter exactly yes or no
#when I type in some random thing it exits silently that is because of the while loop checking properly but no else-if clause at the end checking for yes
#to solve that do not check the variable that the user enters in the while loop and instead have a Boolean value
#and set that value to True when the loop is supposed to continue and false when it is to stop, de-coupling that while loop from the specific user input
# use if __name__ == "main": to set apart the function definitions from the main body of teh program
#there is what may be a typo in your "Thanks for planing" message which I thought would say playing
#if you want to avoid the issue you ran into with the
#time to sleep says it wants two seconds in teh notes but the time.sleep(3) put 3

#def displayIntro():
#    print('''You are in a land full of dragons. In front of you,
#	you see two caves. In one cave, the dragon is friendly
#	and will share his treasure with you. The other dragon
#	is greedy and hungry, and will eat you on sight.''')
#    print()


#def chooseCave():
#    cave = ''
#    while cave != '1' and cave != '2':
#        print('Which cave will you go into? (1 or 2)')
#        cave = input()

#    return cave


#def checkCave(chosenCave):
#    print('You approach the cave...')
#    # sleep for 2 seconds
#    time.sleep(2)
#    print('It is dark and spooky...')
    # sleep for 3 seconds
#    time.sleep(3)
#    print('A large dragon jumps out in front of you! He opens his jaws and...')
#    print()
    # sleep for 2 seconds
#    time.sleep(2)
#    friendlyCave = random.randint(1, 2)

#    if chosenCave == str(friendlyCave):
#        print('Gives you his treasure!')
#    else:
#        print
#        'Gobbles you down in one bite!'


#playAgain = 'yes'
#while playAgain == 'yes' or playAgain == 'y':
#    displayIntro()
#    caveNumber = chooseCave()
#    checkCave(caveNumber)

#    print('Do you want to play again? (yes or no)')
#    playAgain = input()
#    if playAgain == "no":
#        print("Thanks for playing")

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for planing")

