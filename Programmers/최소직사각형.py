def solution(sizes):
    answer = 0

    max_arr = []
    min_arr = []


    for i in range(len(sizes)):

        if sizes[i][0] > sizes[i][1]:
            max_arr.append(sizes [i][0])
            min_arr.append(sizes[i][1])
        else:
            max_arr.append(sizes[i][1])
            min_arr.append(sizes[i][0])

    maxNum = max(max_arr)
    minNum = max(min_arr)

    answer = maxNum * minNum

    return answer
