class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverse(x):
            if x < 0:
                return reverse(-x)
            output = 0
            while x:
                pop = x % 10
                x = x // 10
                output = output * 10 + pop
            if output > (2**31) - 1 or output < (-2**31):
                return 0
            return output if output <= 0x7fffffff else 0
        x_reversed = reverse(x)
        return x == x_reversed
        
