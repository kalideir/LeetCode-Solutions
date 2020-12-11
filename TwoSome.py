class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashTable:
                return [i, hashTable[diff]]
            hashTable[nums[i]] = i
