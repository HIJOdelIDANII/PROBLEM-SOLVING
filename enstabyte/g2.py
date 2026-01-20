n = int(input())
ch = [int(i) for i in input().split()]

res = []
temp = 0
neg = 0
for e in ch:
    if e < 0:
        if neg < 2:
            neg += 1
            temp += 1
        else:
            res.append(temp)
            temp = 1
            neg = 1
    else:
        temp += 1
if temp > 0:
    res.append(temp)

print(len(res))
for a in res:
    print(a, end=" ")
