class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashTable:
                return [i, hashTable[diff]]
            hashTable[nums[i]] = i

            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while (i < j):
            sum = nums[i] + nums[j]
            if (sum == target):
                return [i, j]
            elif sum < target:
                i += 1;
            else:
                j -= 1;
        return []
        
