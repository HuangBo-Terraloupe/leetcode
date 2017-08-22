def largestPalindrome(n):
    if n == 1: return 9
    for a in xrange(2, 9*10**(n-1)):
        upper = 10**n - a
        lower = int(str(upper)[::-1])
        if a**2 - 4*lower < 0: continue
        if (a + (a**2 - 4*lower)**0.5)*0.5 == int((a + (a**2 - 4*lower)**0.5)*0.5):
            return (upper*10**n + lower)%1337


print largestPalindrome(2)