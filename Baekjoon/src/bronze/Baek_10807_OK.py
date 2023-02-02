n = int(input())

arr = list(map(int, input().split()))

v = int(input())
cnt = 0
for i in range(len(arr)):
    if v == arr[i]:
        cnt+=1

print(cnt)