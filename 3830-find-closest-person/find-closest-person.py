class Solution(object):
    def findClosest(self, x, y, z):
        p1 = abs(x-z)
        p2 = abs(y-z)

        if p1 < p2:
            return 1
        elif p2 < p1:
            return 2
        else:
            return 0