t = int(input())

for _ in range(t):
    n = int(input())
    buff = [0] * (n+1)
    if n % 2 == 1:
        z = n
    else:
        z = n-1
    j=0
    
    for i in range(0,z,2):
        buff[n-i]=n-j
        buff[n-i-1]=j+1
        j+=1
    
    print(" ".join(map(str,buff[1:])))
