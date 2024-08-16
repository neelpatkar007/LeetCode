class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        rever = str(x)[::-1]
        
        return rever == str(x)