def solution(arr):
    answer = []
    
    answer.append(arr[0])
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != answer[cnt]:
            answer.append(arr[i])
            cnt+=1

    return answer
print(solution([1,1,3,3,0,1,1]))
# print(solution([4,4,4,3,3]))