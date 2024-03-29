import random   

def guess(x):
    random_Number = random.randint(1, x)
    guess = 0
    while guess != random_Number:
        guess = int(input(f'Guess a number 1 and {x}: '))
        if guess<random_Number:
            print('Sorry, guess again. Too low. ')
        elif guess>random_Number:
            print("Sorry, guess again. Too high. ")
    print("Yay, congrats. You have guessed the number {random_number} correctly ")

def computer_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high :
            guess = random.randint(low, high )
        else :
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} to high (H), too low (L), or correct (c)?? ' ).lower()
        if feedback == 'h': 
            high  = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guess your number, {guess}, correctly!')

computer_guess(10)
guess(10)