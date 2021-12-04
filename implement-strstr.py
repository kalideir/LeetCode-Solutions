class Solution(object):
    def strStr(self, haystack, needle): # needle = 'll', haystack = 'hello';
        if needle == '':
            return 0
        for i in range(len(haystack) + 1 - len(needle)): # ignore very last last char in haystack
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                 
                if j == len(needle) - 1:
                  return i
                
        return -1
      

      
class Solution(object):
  def strStr(self, haystack, needle):
    if needle == '':
        return 0
    for i in range(len(haystack) + 1 - len(needle)):
            if haystack[i: i + len(needle)] == needle:
                return i
              
    return -1
      
    
        
