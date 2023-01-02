a, b, c, max = map(int, input().split())

workTotal = 0
hpTotal = 0

for i in range(24):
    if((hpTotal + a) > max):
        hpTotal -= c

        if(hpTotal < 0):
            hpTotal = 0
    else:
        hpTotal += a
        workTotal += b
print(workTotal)
