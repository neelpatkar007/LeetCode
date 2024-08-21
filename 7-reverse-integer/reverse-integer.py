class Solution(object):
    def reverse(self, x):
        negative = x < 0
        x_str = str(abs(x))
        rever = x_str[::-1]
        reversedx = int(rever)

        if negative:
            reversedx = - reversedx

        if reversedx > 2**31 - 1 or reversedx < -(2**31):
            return 0

        return reversedx