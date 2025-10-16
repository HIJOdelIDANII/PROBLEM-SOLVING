class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while (l<=r):
            med = (l+r)//2
            if nums[med]==target:
                return med
            elif nums[med]>target:
                r=med-1
            else:
                l=med+1
        return -1

            