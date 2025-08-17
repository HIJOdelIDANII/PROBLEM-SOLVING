class Solution:
    def groupAnagrams(self, strs):
        maestro = {}
        new_list = []
        for str in strs:
            freq = [0] * 26
            for c in str:
                freq[ord(c) - ord('a')] += 1
            new_list.append([tuple(freq),str])
        for element in new_list:
            if maestro.get(element[0]) == None:
                maestro[element[0]]=[element[1]]
            else:
                maestro[element[0]].append(element[1])
        return(list(maestro.values()))