def sumOfDigits(n):
    sum = 0
    while(n > 0):
        sum += n %10
        n = int(n/10)
    return sum

t = int(input())
while(t > 0):
    n = int(input())
    arr = [int(i) for i in input().split()]
    for i in range(0, n-1):
        for j in range(i+1, n):
            if(sumOfDigits(arr[i]) > sumOfDigits(arr[j])):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            if(sumOfDigits(arr[i]) == sumOfDigits(arr[j]) and arr[i] > arr[j]):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    for i in range(n):
        print(arr[i], end = " ")
    print()
    t -= 1
