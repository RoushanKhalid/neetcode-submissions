class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        unique = set(nums)
        flag = True

        if len(unique) == len(nums):
            flag = False
        else:
            flag = True

        return flag