class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        our_set = {target-nums[0]:0}
        for i in range (1,len(nums)):
            if our_set.get(nums[i]) != None:        
                return [our_set[nums[i]],i]
            our_set[target-nums[i]]=i

            