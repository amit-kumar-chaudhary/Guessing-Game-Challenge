#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Itroduction and Game Rules

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")


# In[ ]:


#Code

from random import randint

num = randint(1,100)
count = 0
guesses = [0]

while True:     #The 'while True' loop runs indefinitely until the player guesses the correct number and breaks out of the loop.
    
    guess_num = float(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess_num < 1 or guess_num > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue     #If the player's guess is outside the valid range of 1 to 100, the code prints an error message and continues to the next iteration of the loop using 'continue'.
    
    count += 1
    guesses.append(guess_num) 
    
    if num == guess_num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN {count} ATTEMPTS!!')
        break     #If the player's guess matches the target number (guess_num == num), the code congratulates the player on their success, displays the number of guesses made, and exits the loop using 'break'.
        
    if count ==1:
        if abs(num - guess_num) <= 10:
            print('WARM!')      #If it is within 10, it means the guess is close, and 'WARM!' is printed.
        else:
            print('COLD!')      #If it is farther than 10, it means the guess is far from the target, and 'COLD!' is printed.
    else:
        if abs(num-guess_num) < abs(num - guesses[-2]):
            print('WARMER!')      #If the absolute difference of the current guess is smaller than the absolute difference of the previous guess, it means the player is getting closer, and 'WARMER!' is printed.
        else:
            print('COLDER!')      #If the absolute difference of the current guess is larger or equal, it means the player is getting farther away, and 'COLDER!' is printed.


# In[ ]:




