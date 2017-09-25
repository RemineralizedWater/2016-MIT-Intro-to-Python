__author__ = 'Animatrix'

epsilon = 0.01
y = 25000000000000.0
guess = y/2.0
numSteps = 0

while abs(guess**2 - y) >= epsilon:     # Close enough?
    guess = guess - (((guess**2) - y)/(2*guess))        # Generate guesses using Newton-Raphson: g = g - p(g)/p'(g)
    numSteps += 1
    print(str(numSteps))
    print(guess)
print('Square root of ' + str(y) + ' is about ' + str(guess))