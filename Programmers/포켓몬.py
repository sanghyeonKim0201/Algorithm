
def solution(nums):
    answer = 0

    arr = set(nums)

    l = int(len(nums)/2)

    answer = len(arr)

    if l < len(arr):
        answer = l


    return answer


print(solution([3,1,2,3]))
