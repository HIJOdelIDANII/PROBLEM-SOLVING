n = int(input())
ch = [int(i) for i in input().split()]

l = 0 
nf = 0 #number folder
nef = [] #number of elements in each folder
sum=0
i = 0
for e in ch:
    i+=1
    if e<0:
        l+=1
    if l<=2:
        temp.append(e)
    else:

        nf+=1
        l=0 if e<0 else 1
        print("temp:",temp)
        nef.append(temp)
        temp = [e]
if i<len(ch):
    nf+=1
    nef.append(ch[i:])
print("nef:",nef)
print(nf)
for e in nef:
    print(len(e),end=" ")   
