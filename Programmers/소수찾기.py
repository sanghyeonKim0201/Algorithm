def solution(numbers):
    answer = 0

    arr = []
    check = [False for i in range(len(arr))]

    recursive(arr, "", numbers)
    
    arr = set(arr)

    for i in arr:
        
        if isDecimal(i):
            answer+=1

    return answer

def recursive(arr, comb, others):

    if comb != "":
        arr.append(int(comb))
        set(arr)
    for i in range(len(others)):
        recursive(arr, comb + others[i], ("").join(str(j) for j in others[0:i]) +  ("").join(str(j) for j in others[i+1:]))

def isDecimal(num):

    if num < 2:
        return False
    
    for i in range(2, num):
        
        if num % i == 0:
            return False
    return True
    