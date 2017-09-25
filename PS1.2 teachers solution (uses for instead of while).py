s = 'ooxobobeboobzb'
numBobs = 0

for i in range(0, len(s)-2):
    if s[i:i+3] == 'bob':
        numBobs += 1

print 'Number of times bob occurs is:', numBobs