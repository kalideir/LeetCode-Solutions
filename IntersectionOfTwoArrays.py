class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        def _findIntersection(s1, s2):
            return [e for e in s1 if e in s2]
        
        return _findIntersection(set1, set2)
        
        
        
