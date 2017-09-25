def is_palindrome(s):
    def to_chars(s):                                    # internal procedure
        s = s.lower()                                   # changes to lowercase, using .lower() method
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c                           # strips non-characters
        return ans

    def is_pal(s):                                       # internal procedure
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])    # palindrome check recursion

    return is_pal(to_chars(s))


print is_palindrome('Able was I, ere I saw Elba!')