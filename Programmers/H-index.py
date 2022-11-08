def solution(citations):
    answer = 0

    big = 0
    small = 0

    citations.sort()

    n = len(citations)

    for i in range(n):
        
        big = 0
        small = 0

        for j in citations:

            if(j < i):
                small+=1
            elif(j > i):
                big+=1
            elif (j == i):
                big+=1
                small+=1
            
            if(i == big and i == small):
                answer = i

    return answer

print(solution([0, 1, 2, 5, 3]))