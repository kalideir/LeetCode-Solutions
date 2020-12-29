class Solution(object):
    def reverse(self, x):
        if x < 0:
            return -self.reverse(-x)
        output = 0
        while x:
            pop = x % 10
            x = x // 10
            output = output * 10 + pop
        if output > (2**31) - 1 or output < (-2**31):
            return 0
        return output
