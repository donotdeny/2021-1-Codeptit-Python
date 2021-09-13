fibo = [0 for i in range(93)]
fibo[1] = 1
fibo[2] = 1
for i in range(3, 93):
    fibo[i] = fibo[i-1] + fibo[i-2]
t = int(input())
while(t > 0):
    arr = [int(i) for i in input().split()]
    a = arr[0]
    b = arr[1]
    for i in range(a, b+1):
        print(fibo[i], end = " ")
    print()
    t -= 1
