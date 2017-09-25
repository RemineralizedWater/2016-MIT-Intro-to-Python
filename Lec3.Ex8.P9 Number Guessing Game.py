__author__ = 'Animatrix'


print('Please think of a number between 0 and 100! ')
epsilon = ''
low = 0
high = 100
ans = (high + low)/2
while epsilon != 'c':       # am I too far apart
    print('Is your secret number ' + str(ans) + '?')
    epsilon = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                        "Enter 'c' to indicate I guessed correctly. ")
    if epsilon == 'c':
        print('Game over. Your secret number was: ' + str(ans))
        break
    elif epsilon == 'l':
        low = ans
        ans = (high + low)/2
    elif epsilon == 'h':
        high = ans
        ans = (high + low)/2
    else:
        print('Sorry, I did not understand your input.')