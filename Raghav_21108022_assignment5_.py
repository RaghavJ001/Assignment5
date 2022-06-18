# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:21:35 2022

@author: Raghav
"""

#Question 1

s=str(input("Enter a string "))
d=s[::-1]
print("The reverse string is ",d)



#Question 2

l=int(input("Enter the lower limit "))
u=int(input("Enter the upper limit "))
d=int(input("The number should be divisible by "))
for i in range(1,u+1):
    if(i%d==0):
        print(i)
        
        

#Question 3

import math
a=int(input("Enter length of first side of the triangle: "))
b=int(input("Enter length of second side of the triangle: "))
c=int(input("Enter length of third side of the triangle: "))
s=(a+b+c)/2 #s= semi peimeter
if a<b+c and b<a+c and c<a+b:   #checks if the side can form a triangle
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle is ",A)
else:
    print("Not a valid triangle!")



#Question 4

n=5
for i in range(n):
    for j in range(i):
        print('*',end="")
        print('')
for i in range(n,0,-1):
  for j in range(i):
      print('*',end="")
      print('')
      
      
      
 
#Question 5

n=int(input("Enter number of rows: "))
k=65
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k+=1
        if k>90:
            k=65
        print()



#Question 6

print("Prime numbers in an input range.")
start=int(input("Enter starting of range(>=2):"))
end=int(input("Enter ending of range: "))
for i in range(start,end+1):
    for j in range(2,1):
        if i%j==0:
            break
        else:
            print(i)
            
            
        
#Question 7

for i in range(1,501):
    if i%7==0 and i%11==0:
       print(i)




#Question 8

lst=[]
for i in range(0,10):
    ele=int(input("Enter the integer value: "))
    lst.append(ele)
print(lst)    
p=[]
n=[]
odd=[]
even=[]

for j in lst:
    if j>=0:             #adds to positive integer list
        p.append(j)
    if j<0:              #adds to negative integers list
        n.append(j)
    if j%2!=0:           #adds to odd integers list
        odd.append(j) 
    if j%2==0:           #adds to even integers list
        even.append(j)
    
print("a) Positive integers: ",p)
print("b) Negative integers: ",n)
print("c) Odd integers: ",odd)
print("d) Even integers: ",even)
def count(lst):
    counts=dict()
    for word in lst:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
            return counts 
    print(count(lst))       
    



#Question 9

list=input("Enter the words in space separated format: ").split()
d={}              #dictionary to count number of occurences
for i in list:
    if i in d:    #if key already in d, then increment count by 1
        d[i]+=1
    else:         #if key not in d, then count is 1
     d[i]=1
print(d) 

    
        
      
