t = int(input())
while(t > 0):
    n = int(input())
    arr = [int(i) for i in input().split()]
    Hash = dict()
    for i in range(n):
        if(arr[i] in Hash.keys()):
            Hash[arr[i]] += 1
        else: Hash[arr[i]] = 1
    for i in Hash:
        if(Hash.get(i) % 2 != 0): 
            print(i)
            break
    t -= 1
