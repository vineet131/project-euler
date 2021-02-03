from math import floor

def f(k, n):
    num = [1]
    if n == 0:
        return num[0]
    for i in range(1, k):
        num.append(i + 1)
    for j in range(k, n + 1):
        num.append(num[floor(j/k)] + num[j-1])
    if k > n:
        return num[n]
    return num[-1]