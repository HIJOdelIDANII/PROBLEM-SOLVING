def solution(bandwidth:list[int],dataStreams:int):
    result = 0
    count = 0
    bandwidth.sort(reverse=True)
    if len(bandwidth)==1:
        return dataStreams*bandwidth[0]

    def can_add():
        return (dataStreams > count)

    for i in range(len(bandwidth)-1):
        if not can_add():
            break
        result += bandwidth[i]*2
        count+=1
        for j in range(i+1,len(bandwidth)):
            if not can_add():
                break
            combined = bandwidth[i]+bandwidth[j]
            if combined > bandwidth[i+1]*2:
                count+=1
                result+=combined
                if not can_add():
                    break
                result+=combined
                count+=1

    return result


print(solution([2,2,2],2))
print(solution([5,4,8,4,7],6))
print(solution([5],1))
print(solution([120,14,14,8],4))