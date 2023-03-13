import math

def solution(progresses, speeds):
    answer = []

    status = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(len(progresses))]
    print(status)

    key = 0
    cnt = 1
    key2 = 1
    while True:
        print(key, cnt, key2)
        if key == len(status) or key2 == len(status):
            answer.append(cnt)
            break

        if status[key] >= status[key2]:
            key2+=1
            cnt+=1
        else:
            key=key2
            answer.append(cnt)
            cnt=0
        
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))