s = 'ooxobobeboobzb'
bob_count = 0
x = 0

while x <= len(s)-3:
    if s[x:x+3] == 'bob':
        bob_count += 1
    x += 1

print("Number of times 'bob' occurs is: " + str(bob_count))