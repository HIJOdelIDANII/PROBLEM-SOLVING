t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    buff = []
    for i in range(n):
        if s[i]=='1':
            buff.append(i)
    toul = len(buff)
    sum = 0
    if toul>0:
        if n==1 or n==2 or n==3:
            print(max(toul,1))
        else:

            if buff[0]==2:
                sum+=1
            elif buff[0]>2:
                sum+= (buff[0]-1)//2
 
            if buff[toul-1]==n-3:
                sum+=1            
            elif buff[toul-1]<n-3:
                sum+= (n-1-buff[toul-1]-1)//2
            if (toul==1):
                print(sum+toul)  
            else:
                for i in range(toul-1):
                    diff = buff[i+1]-buff[i]-2
                    if diff > 0:
                        sum+= diff//2
                print(sum+toul)

    else:
        if n==1 or n==2 or n==3: 
            print(1)
        else: 
            print(n//2)

            
    