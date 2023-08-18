num = int(input())
s1, s2 = 0, 0
while num > 0:
    r = num % 10
    if r % 2 == 0:
        s1 += r
    else:
        s2 += r
    num //= 10
print(s1, ' ', s2)
