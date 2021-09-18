def equalStr(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in range(len(s1)):
        if(s1[i] != s2[i]):
            return False
    return True

t = int(input())
index = 1
while(t > 0):
    s1 = input()
    s2 = input()
    if(len(s1) != len(s2)):
        print("Test " + str(index) + ": NO")
        index += 1
        t -= 1
        continue
    if(equalStr(s1, s2)):
        print("Test " + str(index) + ": YES")
    else:
        print("Test " + str(index) + ": NO")
    index += 1
    t -= 1
