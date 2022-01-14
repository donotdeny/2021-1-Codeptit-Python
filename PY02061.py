t = int(input())
while(t > 0):
    arr = [int(i) for i in input().split()]
    a = []
    for i in range(arr[0]):
        a.append([int(j) for j in input().split()])
    k = []
    for i in range(3):
        k.append([int(j) for j in input().split()])
    res = 0
    for i in range(arr[0] - 2):
        for j in range(arr[1] - 2):
            tmp = 0
            for m in range(3):
                for n in range(3):
                    tmp += k[m][n]*a[m+i][n+j]
            res += tmp
    print(res)
    t -= 1
