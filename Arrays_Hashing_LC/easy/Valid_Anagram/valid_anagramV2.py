class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        our_dict = {chr(c):0 for c in range(ord('a'),ord('z')+1)}
        for c in s:
            our_dict[c]+=1
        for c in t:
            our_dict[c]-=1
        return all(v == 0 for v in our_dict.values())