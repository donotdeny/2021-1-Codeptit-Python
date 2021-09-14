def abs(a, b):
    if(a < b): return b-a
    else: return a-b

n = int(input())
array_input = []
for x in range(n):
    array_input.append([int(y) for y in input().split()])
k = int(input())
sumUp = 0
sumDown = 0
for i in range(n):
    for j in range(n):
        if(j < n-i-1): sumUp += array_input[i][j]
        elif(j > n-i-1): sumDown += array_input[i][j]
if(abs(sumUp, sumDown) <= k): print("YES")
else: print("NO")
print(abs(sumDown, sumUp))
