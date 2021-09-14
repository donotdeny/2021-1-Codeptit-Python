s1 = input()
s2 = input()
pos = int(input())
s = s1[:pos-1] + s2 + s1[pos-1:]
print(s)
