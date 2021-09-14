t = int(input())
while(t > 0):
    s = input()
    sum = 0
    char = []
    for i in range(len(s)):
        if(s[i] >= 'A' and s[i] <= 'Z'):
            char.append(s[i])
        else: sum += int(s[i])
    char = sorted(char)
    for i in range(len(char)):
        print(char[i], end = "")
    print(sum)
    t -= 1
