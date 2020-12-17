class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        """
        The idea is to find on each iteration whether you have completed giving each level its full
        deserved values of coints, if that's the case return n as the level, else return n - 1
        Sum of coins is calculated using the gauss series
        """
        while left <= right: 
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
