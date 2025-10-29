def power(a,b):
    if b==1:
        return a
    if b & 1:
        return (a* power(a,b-1))
    res = power(a,b>>1)
    res = res*res 
    return res

print(power(2,5))