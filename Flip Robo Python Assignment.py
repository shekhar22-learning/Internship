#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 11
# -----------

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=int(input("Enter a Number: "))
result=fact(x)
print(result)


# In[ ]:


# Question 12
# -----------

num=int(input("Enter a Number: "))
count=0
i=1

while i<=num:
    if num%i==0:
        count=count+1
    i=i+1

if count==2:
    print("It's a Prime No. ")
else:
    print("It's a Composite No. ")


# In[ ]:


# Question 13
# -----------

def palindrome(p):
    t=p.lower()
    left=0
    right=len(t)-1
    
    while right>=left:
        if t[left]=='':
            left+=1
        if t[right]=='':
            right-=1
        if t[left] != t[right]:
            return False
        left+=1
        right-=1
    return True

print(palindrome('KANAK'))
print(palindrome('SHEKHAR'))


# In[ ]:


# Question 14
# -----------

import math

s1 = float(input("Enter base: "))
s2 = float(input("Enter height: "))

h = math.sqrt(s1 ** 2 + s2 ** 2)

print("Hypotenuse =", h)


# In[ ]:


# Question 15
# -----------

input_string =input("Enter a Number: ")
frequencies = {} 
  
for char in input_string:
    if char in frequencies:
        frequencies[char] += 1
    else:
        frequencies[char] = 1

# Show Output
print ("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))


# In[ ]:




