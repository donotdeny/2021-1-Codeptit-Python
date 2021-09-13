n = int(input())
arr = [int(i) for i in input().split()]
Hash = dict()
for i in range(n):
    if(arr[i] in Hash.keys()): Hash[arr[i]] += 1
    else: Hash[arr[i]] = 1
i = 1
while(True):
    if(i in Hash.keys()):
        i += 1 
        continue
    else: 
        print(i)
        break
