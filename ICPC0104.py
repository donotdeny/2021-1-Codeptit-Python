import re

t = int(input())
while(t > 0):
    string = input()
    regex = '\d+'               
    match = re.findall(regex, string) 
    min = 99999999999999999999
    for i in match:
        if(min > int(i)):
            min = int(i)
    print(min)
    t -= 1
