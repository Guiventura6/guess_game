import random
import os 



def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again, Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
       
       
def computer_guess(x): 
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

       
if __name__ == '__main__' :
    answer = 'y'
    while answer == 'y':
        os.system('CLS')
        print('*' * 15)
        print('Guess the name')
        print('*' * 15)
        
        print('Options menu:')
        print('Game mode:')
        print(' [1] You guess the number')
        print(' [2] The computer guess the number')
        print()
        option = 0
        while option != 1 and option != 2: 
            option = int(input('Choose an option: '))
        
        x = int(input('The number options range from 1 to '))
        
        print()
        print('*' * 15)
        print('START GAME !')
        print('*' * 15)
        if option == 1:
            guess(x)
        elif option == 2:
            computer_guess(x)
        
        print()
        answer = input('continue ? yes[y] or no[n]: ') 
    
        
    
        
    

    