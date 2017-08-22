class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        else:
            commonPrefix = ""
            shortest = min(strs, key=len)
            if shortest == "":
                return commonPrefix
            else:
                for idx, _ in enumerate(shortest):
                    items = []
                    for string in strs:
                        items.append(string[idx])
                    if len(list(set(items))) == 1:
                        commonPrefix = commonPrefix + items[0]
                    else:
                        break
                return commonPrefix


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)