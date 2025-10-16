class Solution:
    def simplifyPath(self, path: str)-> str:
        list_path = self.parser(path)
        new_list = ['/']
        for i in range(len(list_path)):
            #print(new_list)
            if list_path[i]=='/' and new_list[-1]=='/':
                continue
            if list_path[i][0]==".":
                if len(list_path[i])>2:
                    new_list.append(list_path[i])
                elif len(list_path[i])==2:
                    while new_list and new_list[-1]=='/':
                        new_list.pop()
                    if new_list:
                        new_list.pop()
                else:
                    new_list.pop()
            else:
                new_list.append(list_path[i])
        return "".join(new_list)
    
    def parser(self, path: str) -> list[int]:
        list_path = ['/']    
        for i in range(1,len(path)):
            if path[i]=='.':
                if list_path[-1][0]=='.':
                    list_path[-1]+='.'
                else:
                    list_path.append(path[i])
            elif path[i]=='/':
                if list_path[-1]=='/':
                    continue
                else:
                    list_path.append(path[i])
            else:
                if list_path[-1]=='/':
                    list_path.append(path[i])
                else:
                    list_path[-1]+=path[i]
        if list_path[-1]=='/':
            return list_path[0:-1:1]
        return list_path       