n = int(input())
ch = input()


long = 0
res = 0#final out
temp = ""
debug = []
for i in range(len(ch)):
    temp += ch[i]
    long +=1
    if ch[i] in ".?!":
        if long <= n:
            debug.append(len(temp))
            res +=1
        else:
            print("Impossible")
            exit(0)
        long = 0
        temp = ""
merged = []
sum = 0
for i in range(len(debug)):
    sum+= debug[i]

    if sum>n:
        merged.append(sum-debug[i])
        merged.append(debug[i])
        sum = 0
if sum > 0:
    merged.append(5)

print(len(merged))