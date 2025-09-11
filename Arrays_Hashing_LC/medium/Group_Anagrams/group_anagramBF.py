class Solution:
    def __init__(self):
        self.final_array = []
    def groupAnagrams(self, strs):
        set_caching = set()
        length = len(strs)
        for i in range(length):
            if (not(i in set_caching)):
                sub_array = [strs[i]]
                if (i+1<length):
                    for j in range(i+1,length):
                        if (self.isAnagram(strs[i],strs[j])):
                            set_caching.add(j)
                            sub_array.append(strs[j])
                self.final_array.append(sub_array)
        return self.final_array
                    
    def isAnagram(self, s: str, t: str) -> bool:
        our_dict = {chr(c):0 for c in range(ord('a'),ord('z')+1)}
        for c in s:
            our_dict[c]+=1
        for c in t:
            our_dict[c]-=1
        return all(v == 0 for v in our_dict.values())