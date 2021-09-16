nm = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
A = set(a)
B = set(b)
res1 = list(A & B)
res2 = list(A - B)
res3 = list(B - A)
res1.sort()
res2.sort()
res3.sort()
for i in range(len(res1)):
    print(res1[i], end = " ")
print()
for i in range(len(res2)):
    print(res2[i], end = " ")
print()
for i in range(len(res3)):
    print(res3[i], end = " ")
print()
