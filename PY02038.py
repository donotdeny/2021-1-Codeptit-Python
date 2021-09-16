def gt(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def ckn(n, k):
    return int(gt(n)/(gt(k)*gt(n-k)))

n = int(input())
arr = []
res = 0
for x in range(n):
    arr.append(input())
for i in range(n):
    count = 0
    for j in range(len(arr)):
        if(arr[i][j] == 'C'): count += 1
    res += ckn(count, 2)
for i in range(n):
    count = 0
    for j in range(n):
        if(arr[j][i] == 'C'): count += 1
    res += ckn(count, 2)
print(res)
