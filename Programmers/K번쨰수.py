def solution(array, commands):
    answer = []
    for arr in commands:
        i = arr[0]
        j = arr[1]
        k = arr[2]

        temp = array[i-1:j]
        temp.sort()
        
        answer.append(temp[k-1])
        
    return answer