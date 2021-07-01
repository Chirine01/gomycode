#!/usr/bin/env python
# coding: utf-8

# In[2]:


firstname=str(input("first name"))
lastname=str(input("last name"))
print (lastname, firstname)


# In[51]:


n=(input("Your number : "))
nn= n*2
nnn= n*3
n=int(n)
nn=int(nn)
nnn=int(nnn)
S=n+nn+nnn
print (S)


# In[49]:


x=int(input('your number : '))
if x%2==0:
    print("even number detected")
else:
    print("odd number detected")


# In[47]:


for i in range (2000,3201):
    if i%7==0 and (i%5!= 0):
            print (i)


# In[23]:


x=1
number=int(input("your number : "))
if number <0:
    print("factorial does not exist for negative numbers")
else:
    if number==0:
        print("the factorial of 0 is 1")
    elif number >0:
        for i in range (1,number+1):
            x=x*i
        print("the factorial of",number,"is",x)


# In[ ]:


phrase=str(input("your senten : "))

def remove(phrase):
    x=""
    for i in range (len(phrase)):
        if i%2==0:
            x=x+phrase[i]
    return x
print(remove(phrase))
        


# In[41]:


number=int(input("your number: "))
if number<0: 
    print ("no discount possible")
else:
    if number>500:
        print(number/2)
    elif number <=200:
        print(number-number*0.1)
    elif 200<=number<=500:
        print(number*70/100)
    else:
        print(number/2)


# In[37]:


X=6


# In[38]:


X

