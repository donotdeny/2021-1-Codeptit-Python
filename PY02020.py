n = int(input())
count = 0
sum = 0
arr = [float(i) for i in input().split()]
for i in range(n):
    if(arr[i] == min(arr) or arr[i] == max(arr)): count += 1
    else: sum += arr[i]
print('%.2f' % float(sum/(n-count)))
