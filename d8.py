# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

N = int(input())
phoneBook = dict()
for i in range(N):
    line = input()
    name = line.split()[0]
    number = line.split()[1]
    phoneBook[name] = number

#print(phoneBook)
lst = list()
for line in stdin:
    lst.append(line.strip())

#print(lst)
for i in lst:
    if i in phoneBook:
        print(i.strip()+'='+phoneBook[i])
    else:
        print('Not found')  