def solution(babbling):
    answer = 0
    arr = ["aya","ye","woo","ma"]

    for i in range(len(babbling)):
        check = True
        for j in arr:
            babbling[i] = babbling[i].replace(j, "0")

        for j in babbling[i]:
            if j not in "0":
                check = False
                break
        
        if check == True:
            answer += 1

    return answer