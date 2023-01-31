exp = input().split("-")

num = []

for i in exp:
    sum = 0
    for j in i.split("+"):
        sum += int(j)
    num.append(sum)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)