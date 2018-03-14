class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)<len(needle):
            return -1
        if haystack == needle:
            return 0
        output = -1
        for i in range(len(haystack)):
            found = haystack[i:i+len(needle)]
            if found == needle:
                output = i
                break

        return output