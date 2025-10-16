# don't read it xD
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        unique_set = set()
        nums.sort()
        print(nums)
        final = set()
        n = len(nums)
        for i in range(n):
            if (nums[i] in unique_set):
                continue
            else:
                unique_set.add(nums[i])
            l,r = 0,n-1
            while (l<r):
                if (l==i):
                    if (l+1>=r):
                        break
                    l=l+1
                if (r==i):
                    if (r-1<=l):
                        break
                    r=r-1
                current_sum = nums[l]+nums[r]+nums[i]
                #print("current_sum",current_sum, nums[l],nums[r],nums[i])
                if current_sum == 0:
                    final.add(tuple(sorted([nums[l],nums[i],nums[r]])))
                    l+=1
                    r-=1
                elif current_sum > 0:
                    r-=1
                else:
                    l+=1

        if (len(final)==0):
            return []
        else:
            return [list(i) for i in final]

        