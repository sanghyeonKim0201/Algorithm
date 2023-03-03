
def solution(clothes):
    answer = 1
    types = [y for x, y in clothes]

    count = [types.count(i) for i in set(types)]
    
    for c in count:
        answer *= c + 1
        print(answer)

    return answer - 1 

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
