
# coding: utf-8

# <center><h1> Machine Learning-I (CS/DS 706)-Assignment 1
# <h2>Chetna Jain (MT2016044)<br>
# Kanika Narang   (MT2016069)<br>
# Tehreem Ansari  (MT2016145)<br></h2><h1>
# 
# </center>

# <h2>Question 1 a.</h2>

# Step1: Load the Salary.csv dataset

# In[21]:


import pandas as pd
import numpy as np
import random
import math
import statistics as s
import matplotlib.pyplot as plt


# In[2]:


salary = pd.read_csv(r'/home/kanika/Downloads/Salaries.csv')


# In[3]:


salary = salary[['Id','TotalPay']]


# In[4]:


#Displaying top 5 rows
salary[:5]


# Step2: Calculate the Aggregate function on the entire column 'Total Pay'. The Agggregate function we picked is **mean**

# In[4]:


mean = salary['TotalPay'].mean()
print("Mean of the entire column 'TotalPay' = ",mean)


# Step 3  Pick a fraction in the range ρ ∈ (0, 1) : Let ρ =0.6

# In[5]:


p=0.6
n= int(salary.shape[0])
np= n*p
np


# Step 4 Randomly (uniform) sample nρ elements from the dataset:

# In[69]:


#Done ceil to get rounded number of rows
np=math.ceil(np)
#using sample function to generate the random number of rows
sample =random.sample(range(n), int(np))


# In[79]:


# to select the values of the column 'TotalPay' respective to the row numbered sampled above
sampleTotalPay = salary[salary['Id'].isin(sample)]
sampleTotalPay = sampleTotalPay['TotalPay']


# Step5 Compute the sample statistic τci:

# In[82]:


sample_mean =sampleTotalPay.mean()
print("Mean of the sampled data is = ",sample_mean)


# Step6 Repeating step 5 m times :<br>
# Let m= 100
# 

# In[121]:


sampled_mean_vector = []
for i in range(100):
    sample =random.sample(range(n), int(np))
    sampleTotalPay = salary[salary['Id'].isin(sample)]
    sampleTotalPay = sampleTotalPay['TotalPay']
    sample_mean =float(sampleTotalPay.mean())
    sampled_mean_vector.append(sample_mean)
print("List of m means is as follows \n",sampled_mean_vector)


# Step 7 Calculating the average mean:

# In[127]:


average_mean =s.mean(sampled_mean_vector)
print("Average Mean = ", average_mean)


# Step 8 Generate plots to illustrate how τc∗ converges to τc∗ for different values of ρ and m:
# <br>
# We need to do the sampling for different value of p
# <br>
# First we generate the 100 different values of p with a gap of 0.01
# 

# In[18]:


p_vector = np.arange(0.01,1.01,0.01)
p_vector


# In[19]:


# y is the list which will store the average mean of the different values of p
y = []
for p in p_vector:
    np=n*p
    sampled_mean_vector=[]
    for i in range(100):
        sample =random.sample(range(n), int(np))
        sampleTotalPay = salary[salary['Id'].isin(sample)]
        sampleTotalPay = sampleTotalPay['TotalPay']
        sample_mean =float(sampleTotalPay.mean())
        sampled_mean_vector.append(sample_mean)
        mean= float(s.mean(sampled_mean_vector))
    y.append(mean)
    
y    


# Now to plot the values we used the plot function on the y-axis the average mean values are plotted and x-axis the p values.

# In[20]:


plt.plot(p_vector,y,'gs')
plt.axhline(y=mean, xmin=0, xmax=1,lw=2,c="red")
plt.ylabel('Average Mean Value')
plt.xlabel('p value')
plt.show()


# **Observation:** 
# 
# As the value of p increases and gets close to 1, the value of the average mean from the m iterations of experiment generated gets close to value of the mean of the entire column ‘TotalPay’ also . This shows the Law of Large numbers.That is as the sample size increases the sample mean will start converging to the mean of the population (entire column).
# 

# In[8]:


# doing samping for different values of m
m_vector =[1,5,10,50,100,500,1000,1500,2000]
my= []
for m in m_vector:
    np=n*p
    sampled_mean_vector=[]
    for i in range(m):
        sample =random.sample(range(n), int(np))
        sampleTotalPay = salary[salary['Id'].isin(sample)]
        sampleTotalPay = sampleTotalPay['TotalPay']
        sample_mean =float(sampleTotalPay.mean())
        sampled_mean_vector.append(sample_mean)
        mean= float(s.mean(sampled_mean_vector))
    my.append(mean)
    


# In[9]:


my


# In[13]:


plt.plot(m_vector,my,'gs')
plt.axhline(y=mean, xmin=0, xmax=1,lw=2,c="red")
plt.ylabel('Average Mean Value')
plt.xlabel('m value')
plt.show()


# **Observation:** The above plots shows as we increase the value of m the average mean value will start getting closer to the mean value of the entire column.

# In the below code we are Trying for more values of m to get more insight,which shows me as we increase the value of m the sample means comes out to be close to the mean of the population i.e. entire column.This happens because of central limit theorem.

# In[25]:


m_vector2 = np.arange(1,1000,5)
m_vector2 =m_vector2[:162]
len(m_vector2)


# In[ ]:


# doing samping for different values of m

my2= []
for m in m_vector2:
    np=n*p
    sampled_mean_vector=[]
    for i in range(m):
        sample =random.sample(range(n), int(np))
        sampleTotalPay = salary[salary['Id'].isin(sample)]
        sampleTotalPay = sampleTotalPay['TotalPay']
        sample_mean =float(sampleTotalPay.mean())
        sampled_mean_vector.append(sample_mean)
        mean= float(s.mean(sampled_mean_vector))
    my2.append(mean)


# In[17]:


my2


# In[19]:


len(my2)


# In[26]:


plt.plot(my2,m_vector2,'gs')
plt.axvline(x=mean, ymin=0, ymax=1,lw=2,c="red")
plt.annotate('mean of entire column = 74768.32', xy=(74768,0), xytext=(74790,100),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.xlabel('Average Mean Value')
plt.ylabel('m value')
plt.show()


# **Observation:** Here we can see that as the value of m increases the sample mean gets close to the mean of entire column. This is because of central limit theorem which means, the distribution of the average of a large number of independent, identically distributed variables will be approximately normal, regardless of the underlying distribution. Red line shows the mean of entire column.
