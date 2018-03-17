class Solution(object):
    def lengthOfLastWord(self, s):
        return 0 if len(s.split()) == 0 else len(s.split()[-1])