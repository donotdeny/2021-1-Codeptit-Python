def equal(a, b): # a == b?
    if(len(a) != len(b)): return False
    for i in range(len(a)):
        if(a[i] != b[i]): return False
    return True

def smaller(a, b): # a < b?
    if(len(a) > len(b)): return False
    elif(len(a) < len(b)): return True
    for i in range(len(a)):
        if(len(a) > len(b)): return False
    return True

def equalArr(arr): # all elements is equal
    for i in range(len(arr)-1):
        if(equal(arr[i], arr[i+1]) == False): return False
    return True

n = 1
while(n != 0):
    n = int(input())
    if(n == 0): break
    arr = []
    for i in range(n):
        tmp = input()
        news = ""
        for i in range(len(tmp)):
            if(tmp[i] != '0'):
                news = tmp[i::]
                break
        arr.append(news)
    for i in range(n-1):
        for j in range(i+1, n):
            if(equal(arr[i], arr[j])):
                continue
            elif(smaller(arr[i], arr[j]) == False):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
    if(equalArr(arr)):
        print("BANG NHAU")
    else:
        print(arr[0], arr[len(arr)-1])
