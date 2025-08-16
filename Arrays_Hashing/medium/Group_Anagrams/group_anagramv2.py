def turn_dict_tuple(dicto):
    #o(m)
    alphabet_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    lista = []
    for c in alphabet_set:
        if dicto.get(c) == None:
            lista.append(0)
        else:
            lista.append(dicto[c])
    return tuple(lista)
    
class Solution:
    
    def groupAnagrams(self, strs):
        maestro = {}
        final_list = []
        new_list = []
        for str in strs:
            obj_str = {}
            for c in str:
                if obj_str.get(c) == None:
                    obj_str[c] = 1
                else :
                    obj_str[c] = obj_str[c]+1
            new_list.append([turn_dict_tuple(obj_str),str])
        for element in new_list:
            if maestro.get(element[0]) == None:
                maestro[element[0]]=[element[1]]
            else:
                maestro[element[0]].append(element[1])
        for element in maestro:
            final_list.append(maestro[element])
        print(final_list)
        return(0)