__author__ = 'Animatrix'

test = 'test'

mod_test = test.capitalize()
print mod_test

mod_test = test.center(40, '$')
print mod_test

mod_test = test.count('t', 0, 4)
print mod_test

print test
mod_test = test.encode('base64', 'strict')
print "Encoded String: " + mod_test

mod_test = test.decode('base64', 'strict')
print "Decoded String: " + test.decode('base64', 'strict')      # Not decoding properly
print "Decoded String: " + mod_test                             # Not decoding properly

mod_test = 0
print mod_test

mod_test = test.endswith('s', 2, 3)
print mod_test

# https://docs.python.org/2/library/stdtypes.html#string-methods