counter = 0
import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.50)

print("It's a guessing game!")
time.sleep(2.00)
print("This program generates a number from 1 to 20. Can you guess it?")
time.sleep(2.00)
print ("Loading", end= ' ') 
delay_print (" ...")
print (end='\r')
print ("               ", end='\r')
print ("Loading", end= ' ') 
delay_print (" ...")
print(end="\n")
time.sleep(1.00)

import random
number = random.randint(1,20)
restart = True
while restart == True:
    if counter < 3:
        counter += 1
        guess_no = input ("Guess the number! ")
        guess = int(guess_no)
        answer_no = guess - number
        answer = abs(answer_no)
        if answer == 0:
            print(f"Correct! The answer is {number}. It took you {counter} tries to guess.")
            restart = False
            exit()
        if answer != 0:
            print(f"You are off by {answer}. Try again!")
            restart = True
    else:
        print(f"You've ran out of tries! The answer was {number}.")
        exit()
    
