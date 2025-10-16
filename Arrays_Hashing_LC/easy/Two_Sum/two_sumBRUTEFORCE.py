class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n-1):
            rest = target-nums[i]
            for j in range(i+1,n):
                if rest == nums[j]:
                    return [i,j]
