class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            r = False
        else:
            input_num = x
            num_list = []
            final_num = 0
            buffer = 1
            while x != 0:
                last_num = x % 10
                x = x // 10
                num_list.append(last_num)
            for i in range(len(num_list)):
                final_num = final_num + num_list[len(num_list) -i -1] * buffer
                buffer = buffer * 10

            if final_num == input_num:
                r = True
            else:
                r = False
        return r
