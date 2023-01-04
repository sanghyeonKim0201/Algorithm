n = int(input())
shops = list(map(int, input().split()))
milk = [0, 1, 2]

num = 0

for i in range(n):
    if(shops[i] == milk[num%3]):
        num+=1
    
print(num)