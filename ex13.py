t = ['1', '']
dic = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11,
'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22,
'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26, '_' : 27, '.' : 28}
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '.']
while(t[0] != '0'):
    t = input().split()
    if(t[0] == '0'): break
    k = int(t[0])
    s = t[1]
    res = ""
    for i in range(len(s)):
        index = (dic.get(s[i]) + k) % 28
        res += alphabet[index-1]
    print(res[::-1])
