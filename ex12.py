t = int(input())
for index in range(t):
    s = input()
    res = ""
    n = len(s)
    i = 0
    while(i < n):
        alpha = 1
        for j in range(i, n-1):
            if(s[j] == s[j+1]): alpha += 1
            else: break
        i += alpha
        res += str(alpha) + s[i-1]
    print(res)
