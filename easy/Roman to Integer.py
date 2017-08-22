d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def romanToInt(s):
    index = "I"
    rest = 0
    for char in s[::-1]:
        if d[char] < d[index]:
            rest -= d[char]
            index = char
        else:
            rest += d[char]
            index = char
    return rest
