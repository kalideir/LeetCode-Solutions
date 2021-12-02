# [-2, 0, 3, 5, 11] => return [0, 4, 9, 25, 121]

class Solution:
    def sortedSquares(arr):
        
        left = 0
        right = len(arr) - 1
        result = []
        
        while left <= right:
            if arr[left] ** 2 >= arr[right] ** 2:
                result.append(arr[left] ** 2)
                left += 1
                
       else:
            result.append(arr[right] ** 2)
            right -= 1
            
       return result[::-1]
              
              
          
        
    
