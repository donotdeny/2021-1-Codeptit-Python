arr = [int(i) for i in input().split()]
a = arr[0]
k = arr[1]
n = arr[2]
flag = 0
if(arr[0] >= arr[2]):
    print("-1")
else:
    b = k # start with k to list all multiple of k
    while(a + (b-a) <= n): # check a + ? <= n
        if(b - a > 0): # positive number
            flag = 1 # sign 
            print(b-a, end = " ")
        b += k 
    if(flag != 1): print("-1")
print()
