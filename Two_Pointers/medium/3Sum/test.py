import time
from three_sum import Solution
from array_test import nums
s = Solution()
start = time.time()
result = s.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10])
result = s.threeSum(nums)
end = time.time()
print(result)
print(f"Runtime: {end - start:.6f} seconds")