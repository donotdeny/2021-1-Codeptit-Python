test=10 
arr = []
Hash = dict()
while test>0: 
    data=input() # read 1 line 
    base=data.split() # split() method return a list, base is a list in 1 line
    for i in range(len(base)):
        num = int(base[i]) % 42
        if(num in Hash.keys()): Hash[num] += 1
        else: Hash[num] = 1
    test-=len(base) # read remaining elements
print(len(Hash))
