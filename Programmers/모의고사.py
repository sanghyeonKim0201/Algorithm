def solution(answers):
    answer = []
    arr = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    cnt = [0, 0, 0]

    for i in range(len(arr)):
        for j in range(len(answers)):
            if answers[j] == arr[i][j&len(arr[i])]:
                cnt[i] += 1
        
    
    max_num = max(cnt)
    for i in range(len(cnt)):
        if max_num == cnt[i]:
            answer.append(i+1)
    return answer