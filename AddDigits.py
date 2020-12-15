class Solution:
    def addDigits(self, num: int) -> int:
        root = 0
        while num > 0: # iteratively find mod op
            
            root += num % 10 # 500 mod 10 =0, 5 mod 10 = 5
            num = num // 10 # 5 // 10 = 0
            
            if num == 0 and root > 9:
                num = root
                root = 0
                
        return root
        

class Solution: # constant time algorithm follows from the fact that a number is a divisble by 9 if the sum of its digits eqs 9
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
