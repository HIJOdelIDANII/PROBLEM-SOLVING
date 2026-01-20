t = int(input())

for _ in range(t):
    
    n,x = map(int, input().split())
    all = [int(i) for i in input().split()]
    all.sort()
    
    sum = 0
    i = 0
    while (sum<x) and (i<len(all)):
        if sum+all[i]<=x:
            sum+=all[i]
        i+=1
            
    i-=1
    print("i",i)
        