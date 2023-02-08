n = list(input())

for i in range(len(n)):
    if n[i].islower():
        n[i] = n[i].upper()
    else:
        n[i] = n[i].lower()
print("".join(n))

