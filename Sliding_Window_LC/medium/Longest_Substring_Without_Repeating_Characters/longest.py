class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) in [0,1]):
            return len(s)
        l, r= 0,1
        tracker = {s[0]:0}
        max_length = 1
        while (r<len(s)):
            #print(tracker)
            if (s[r] not in tracker):
                tracker[s[r]]=r
                max_length = max(max_length, r-l+1)
                r+=1
            elif ((s[r] in tracker) and (tracker[s[r]]<l)):
                tracker[s[r]]=r
                max_length = max(max_length, r-l+1)
                r+=1
            else:
                position = tracker[s[r]] 
                l = position+1
                tracker[s[r]] = r
                r +=1            
        return max_length

        