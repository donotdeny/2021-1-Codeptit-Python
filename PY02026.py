def checkEqual(arr, brr):
    for i in range(len(arr)):
        if(arr[i] != brr[i]): return False
    return True

arr = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
arr = list(set(a))
brr = list(set(b))
if(len(arr) != len(brr)): print("NO")
else:
    if(checkEqual(arr, brr)): print("YES")
    else: print("NO")
