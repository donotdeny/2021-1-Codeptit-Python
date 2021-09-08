def Abs(a, b):
    if(a > b): return a-b
    return b-a

def testDiff(s1, s2):
    for i in range(len(s1)-1):
        tmp1 = Abs(ord(s1[i]), ord(s1[i+1]))
        tmp2 = Abs(ord(s2[i]), ord(s2[i+1]))
        if(tmp1 != tmp2): return False
    return True

t = int(input())
while t > 0:
    s = input()
    reverse = s[::-1]
    if(testDiff(s, reverse) == True): print("YES")
    else: print("NO")
    t -= 1
