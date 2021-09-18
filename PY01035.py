s = input()
if(len(s) % 3 == 1):
    s = "00" + s
elif(len(s) % 3 == 2):
    s = "0" + s
res = ""
n = len(s)-1
i = 0
tmp = 0
while(n >= 0):
    if(s[n] == '1'):
        tmp += 2**i
    if(i == 2):
        res += str(tmp)
        i = 0
        tmp = 0
    else:
        i += 1
    n -= 1
print(res[::-1])
