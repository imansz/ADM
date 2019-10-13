***Say "Hello, World!" With Python
print("Hello, World!")


***Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n%2!=0:
    print("Weird")

elif n in range(2,6):
    print("Not Weird")

elif n in range(6,21):
    print("Weird")
elif n > 20:
    print("Not Weird")


***Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)

***Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a//b)
print(a/b)

***Loops
if __name__ == '__main__':
    n = int(input())
for i in range(0,n):
    print(i*i)

***Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0 and (year%100!=0):
        leap=True
                
    elif year%100==0 and year%400==0:
        leap=True            
            
    else:
        leap=False


    return leap

***Print Function

if __name__ == '__main__':
    n = int(input())
x= range(1, n+1)
for i in x:
    print(i, end="") 

***List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print ([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k !=n])

***Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())


arr = list(map(int,input().strip().split()))[:n]
i=0
a=max(arr)
ar=[]
b=len(arr)
for i in range(0,b) :
    if arr[i]==a:
        continue
    else:
        ar.append(arr[i])

print (max(ar))

***Nested Lists
marks = []
for _ in range(0,int(input())):
    marks.append([input(), float(input())])
second_highest = sorted(list(set([marks for name, marks in marks])))[1]
print('\n'.join([a for a,b in sorted(marks) if b == second_highest]))

***Finding the percentage
marks = {}
for _ in range(int(input())):
    line = input().split()
    marks[line[0]] = list(map(float, line[1:]))
print('%.2f' %(sum(marks[input()])/3))

***Tuples
if __name__ == '__main__':
  n = int(input())
print(hash(tuple(map(int, input().split()))))

***sWAP cASE
def swap_case(s):
    
    temp = ""
    for c in s:
        if c.isupper() == True:
            temp+=(c.lower())
        else:
            temp+=(c.upper())
    return temp

***String Split and Join
def split_and_join(line):
    # write your code here
 return "-".join(line.split())

***What's Your Name?
def print_full_name(first_name, last_name):
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))

***Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

***String Validators
if __name__ == '__main__':
    s = input()
methods = [str.isalnum,  str.isalpha,  str.isdigit, str.islower, str.isupper]

for res in map(lambda m: any(map(m,s)), methods):
    print(res)

***Introduction to Sets
def average(array):
    return sum(set(array))/len(set(array))

***Calendar Module
import calendar
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())

***Exceptions
for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except BaseException as err:
        print("Error Code:", err)

***Symmetric Difference
input()
a1=set(map(int, ((input().split()))))
input()
a2=set(map(int, ((input().split()))))
a3 = sorted(a1 ^ a2)
for i in a3:
    print(i)

***Set .add()
print(len(set(input() for i in range(int(input())))))

***Integers Come In All Sizes
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print((a**b)+(c**d))


***Triangle Quest
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*(10**i -1)//9)


***Zipped!
[print(sum(i) / len(i)) for i in zip(*[map(float, input().split()) for _ in range(int(input().split()[1]))])]

***Detect Floating Point Number
from re import match, compile
patt = compile('^[-+]?[0-9]*\.[0-9]+$')
for _ in range(int(input())):
    print(bool(patt.match(input())))


***Map and Lambda Function
cube = lambda x: x**3
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b=b,a+b


***XML 1 - Find the Score


def get_attr_number(node):
    a=len(node.attrib)
    return a+sum((get_attr_number(child) for child in node))


***XML2 - Find the Maximum Depth


maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    
    for child in elem:
        depth(child, level)


***Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        decorated_l = ['+91 {} {}'.format(n[-10: -5], n[-5:]) for n in l]
        return f(decorated_l)
    return fun

***Arrays
def arrays(arr): return(numpy.array(arr[::-1], float))
   
***Shape and Reshape
import numpy as np
x=np.array(list(map(int,input().split())))
x.shape=(3,3)
print(x)
