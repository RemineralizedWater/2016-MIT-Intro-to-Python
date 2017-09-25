s = 'boobbobobobobobooboofjbmbobbxboboboqxpf'
bobString = ''
bobCount = 0
for letter in s:
    if bobString == 'bo' and letter == 'b':
        bobCount += 1
        bobString = 'b'
        print(str(bobCount))
    elif bobString == 'b' and letter == 'o':
        bobString = bobString + letter
    elif letter == 'b' and bobString != 'bo':
        bobString = 'b'
    else:
        bobString = ''
print("Number of times bob occurs is: " + str(bobCount))