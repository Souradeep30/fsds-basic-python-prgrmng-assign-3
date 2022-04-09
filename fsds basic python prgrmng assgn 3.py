#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer 1
num = 30

if(num > 0):
    print(num, "is Positive")
elif(num < 0):
    print(num, "is Negative")
else:
    print(num, "is Zero")


# In[2]:


num = 0

if(num > 0):
    print(num, "is Positive")
elif(num < 0):
    print(num, "is Negative")
else:
    print(num, "is Zero")


# In[3]:


num = -7

if(num > 0):
    print(num, "is Positive")
elif(num < 0):
    print(num, "is Negative")
else:
    print(num, "is Zero")


# In[4]:


#Answer 2
num = int(input("Enter a number: "))

if(num % 2 == 0):
    print(num, "is a Even Nummber")
else:
    print(num, "is an Odd Number")


# In[5]:


#Answer 3
year = int(input("Enter year"))

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print("Leap Year")
else:
    print("Not a Leap Year")


# In[7]:


#Answer 4
num = int(input("Enter a number: "))

isPrime = True

if num <= 1:
    print(num, "is neither prime nor composite")
else:
    d = 2
    while(d*d <= num):
        if(num%d==0):
            isPrime = False
            break
        d = d + 1

if(num > 1):
    if(isPrime):
        print(num, "is prime number")
    else:
        print(num, "is not prime number")


# In[13]:


#Answer 5
lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
        
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
         print(num)
        
           
       


# In[ ]:





# In[ ]:




