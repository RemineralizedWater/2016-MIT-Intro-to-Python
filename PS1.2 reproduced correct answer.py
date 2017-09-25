s = 'bobob'
num_bob = 0

for i in range(0, len(s)-2):        # len() = the actual length as an int, last char of range = len()+1
    if s[i: i+3] == 'bob':          # array [0 = starting char, len() + 1 = last char]
        num_bob += 1

print num_bob