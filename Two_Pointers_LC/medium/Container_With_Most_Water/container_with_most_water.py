class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_volume = 0
        n = len(height)
        l,r = 0,n-1
        while (l<r):
            d = r-l
            current_volume = d*(min(height[l],height[r]))
            max_volume = max(current_volume,max_volume)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max_volume