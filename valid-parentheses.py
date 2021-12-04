class Solution(object):
    def isValid(self, s):
        
        stack = []
        parentheses = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        
        for char in s:
            print(char)
            if char in parentheses:
                if stack and stack[-1] == parentheses[char]:
                    stack.pop()
                
                else:
                    return False
                
            else:
                stack.append(char)
        
        return True if not stack else False
