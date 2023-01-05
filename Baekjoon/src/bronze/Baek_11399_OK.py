n = int(input())
p = list(map(int, input().split()))
time = [0 for i in range(n)]
p.sort()

min = 0
for i in range(n):
    min += p[i]
    time[i] = min
print(sum(time))