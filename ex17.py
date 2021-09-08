def gcd(a, b):
    if(b == 0): return a
    else: return gcd(b, a%b)

n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
for i in range(n-1):
    for j in range(i+1, n):
        if(gcd(arr[i], arr[j]) == 1): print(arr[i], arr[j])
