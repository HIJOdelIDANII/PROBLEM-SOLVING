class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final = []
        nums.sort()
        #print(nums)
        n = len(nums)
        for i in range(n-2):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = n-1
            while (l<r):
                current_sum = nums[i]+nums[l]+nums[r]
                if current_sum == 0:
                    final.append([nums[i],nums[l],nums[r]])
                    l+=1
                    # i used those two while loops to avoid duplication between the two pointers
                    while (nums[l]==nums[l-1] and l<r):    
                        l+=1
                    r-=1
                    while (nums[r]==nums[r+1] and l<r):
                        r-=1
                elif current_sum > 0:
                    r-=1
                else:
                    l+=1
        return final
