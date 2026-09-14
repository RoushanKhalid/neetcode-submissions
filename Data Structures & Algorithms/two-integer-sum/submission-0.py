class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lst = []

        for i in range(len(nums)):
            # if i >= target:
            #     continue
            # else:
            #     j = 0

                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        lst.append(i)
                        lst.append(j)

        return lst
