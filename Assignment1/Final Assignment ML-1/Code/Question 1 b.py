
# coding: utf-8

# b). Repeat the above experiment but for varying sample sizes in the same ’run’. Specifically,
# pick m samples as above but the sample sizes are in turn randomly sampled from a Gaussian. Generate plots showing how convergence changes with μ, σ and m where μ, are the mean and variance of the Gaussian from which the sample sizes are picked.
# 
# Solution:
# 

# In[3]:


import pandas as pd
import numpy as np
import random
import math
import statistics as s
import matplotlib.pyplot as plt


# Step1: Load the Salary.csv dataset

# In[4]:


salary = pd.read_csv(r'/home/kanika/Downloads/Salaries.csv')
salary = salary[['Id','TotalPay']]
#Displaying top 5 rows
salary[:5]


# Step2: Calculate the Aggregate function on the entire column 'Total Pay'. The Agggregate function we picked is mean

# In[5]:


mean = salary['TotalPay'].mean()
print("Mean of the entire column 'TotalPay' = ",mean)


# To generate random sample size from the gaussian we can use random.randn() function from the numpy library
# 

# In[7]:


#sigma * np.random.randn(...) + mu
#mean=1000 and sd =100
n=len(salary['Id'])
S=100 * np.random.randn() +1000
print("The random number generated from the gaussian with mean=1000 and standard deviation=100= ",S)
#Since we nee the size of sample so lets take the ceil of S
S= math.ceil(S)
print("The randomly generated sample size is = ",S)


# Step 4 Randomly (uniform) sample S elements from the dataset:

# In[8]:


#using sample function to generate the random number of rows
sample =random.sample(range(n), int(S))


# In[9]:


# to select the values of the column 'TotalPay' respective to the row numbered sampled above
sampleTotalPay = salary[salary['Id'].isin(sample)]
sampleTotalPay = sampleTotalPay['TotalPay']


# Step5 Compute the sample statistic τci:

# In[10]:


sample_mean =sampleTotalPay.mean()
print("Mean of the sampled data is = ",sample_mean)


# Step6 Repeating step 5 m times :
# Let m= 100

# In[11]:


sampled_mean_vector = []
for i in range(100):
    S=100 * np.random.randn() +1000
    S= math.ceil(S)
    sample =random.sample(range(n), int(S))
    sampleTotalPay = salary[salary['Id'].isin(sample)]
    sampleTotalPay = sampleTotalPay['TotalPay']
    sample_mean =float(sampleTotalPay.mean())
    sampled_mean_vector.append(sample_mean)
print("List of m means is as follows \n",sampled_mean_vector)


# Step 7 Calculating the average mean:

# In[12]:


average_mean =s.mean(sampled_mean_vector)
print("Average Mean = ", average_mean)


# Step 8 showing how convergence changes with μ, σ and m

# First looking at the convergence by just changing μ and keeping  σ and m same.

# In[13]:


#Generating  μ values in the range of 101 to 148554 in a gap of 1485
mu_vector = np.arange(101,148554,1485)
mu_vector


# In[14]:


# Here we now doing the sampling for different values of μ
mu_vector_mean =[]
for mu in mu_vector:
    sampled_mean_vector = []
    for i in range(100):
        S=100 * np.random.randn() + mu
        S= math.ceil(S)
        if S > n:
            S=n
        elif S<= 0:
            S=1
        sample =random.sample(range(n), int(S))
        sampleTotalPay = salary[salary['Id'].isin(sample)]
        sampleTotalPay = sampleTotalPay['TotalPay']
        sample_mean =float(sampleTotalPay.mean())
        sampled_mean_vector.append(sample_mean)
    average_mean =s.mean(sampled_mean_vector)
    mu_vector_mean.append(average_mean)
mu_vector_mean
    


# In[15]:


# this is done to enhance the look of plots and to increase the number of ticks on y-axis
from pylab import rcParams
rcParams['figure.figsize'] = 15, 7
plt.yticks(np.arange(min(mu_vector_mean), max(mu_vector_mean)+1, 100))


# In[17]:


plt.plot(mu_vector,mu_vector_mean,'go')
plt.axhline(y=mean, xmin=0, xmax=1,lw=2,c="red")
plt.annotate('mean of entire column = 74768.32', xy=(0, 74768), xytext=(100, 75000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.ylabel('Average Mean Value')
plt.xlabel(' μ value')
plt.show()


# **Observation:** This plot shows that as the value of μ increases and gets close to the number of total number of rows in the column. The average mean gets close to the mean of entire column. This is because the sample size picked from the gaussian will start getting closer to the number of total rows  in the column. According to the law of large numbers as the sample size increases the sample mean gets close to the mean of the population.

# Now looking at the convergence by just changing σ and keeping μ and m same.

# In[7]:


#Generating  σ values in the range of 100 to 100000 in a gap of 1000 mean is fixed at 
n=len(salary['Id'])
sg_vector = np.arange(100,100000,1000)
mu=int(n/2)
sg_vector


# In[8]:


len(sg_vector)


# In[9]:


# Doing the sampling experiment for different values of σ
sg_vector_mean =[]
sample_size=[]
for sg in sg_vector:
    sampled_mean_vector = []
    for i in range(100):
        S= sg * np.random.randn() + mu
        S= math.ceil(S)
        if S > n:
            S=n
        elif S<= 0:
            S=1
        sample_size.append(S)    
        sample =random.sample(range(n), int(S))
        sampleTotalPay = salary[salary['Id'].isin(sample)]
        sampleTotalPay = sampleTotalPay['TotalPay']
        sample_mean =float(sampleTotalPay.mean())
        sampled_mean_vector.append(sample_mean)
    average_mean =s.mean(sampled_mean_vector)
    sg_vector_mean.append(average_mean)
sg_vector_mean
    


# In[31]:


len(sample_size,range)
len(sg_vector_mean)


# In[15]:


plt.plot(sg_vector,sg_vector_mean,'go')
plt.axhline(y=mean, xmin=0, xmax=1,lw=2,c="red")
plt.annotate('mean of entire column = 74768.32', xy=(0, 74750), xytext=(100, 76000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.ylabel('Average Mean Value')
plt.xlabel('σ value')
plt.show()


# Now for different values of m
# First we need to generate differnt values of m

# In[83]:


#Generating different values of m in the range of 1 to 1000 in a gap of 10 keeping μ=n/2 and σ=100 same for all the m
m_vector = np.arange(1,1000,150)
mu=int(n/2)
m_vector


# In[84]:


# Doing the sampling experiment for different values of m
m_vector_mean =[]
for m in m_vector:
    sampled_mean_vector = []
    for i in range(m):
        S= 100 * np.random.randn() + mu
        S= math.ceil(S)
        if S > n:
            S=n
        elif S<= 0:
            S=1
        sample =random.sample(range(n), int(S))
        sampleTotalPay = salary[salary['Id'].isin(sample)]
        sampleTotalPay = sampleTotalPay['TotalPay']
        sample_mean =float(sampleTotalPay.mean())
        sampled_mean_vector.append(sample_mean)
    average_mean =s.mean(sampled_mean_vector)
    m_vector_mean.append(average_mean)
m_vector_mean
    


# In[85]:


plt.plot(m_vector,m_vector_mean,'go')
plt.axhline(y=mean, xmin=0, xmax=1,lw=2,c="red")
plt.annotate('mean of entire column = 74768.32', xy=(0, 74750), xytext=(100, 75000),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.ylabel('Average Mean Value')
plt.xlabel('m value')
plt.show()


# **Observation : ** Here we can observe as the value of m increases the average mean value gets close to the mean of the entire column. Red line shows the mean of the entire column. The above plot also shows that sample mean values are following a normal distribution. That is what central limit theorem says, the distribution of the average of a large number of independent, identically distributed variables will be approximately normal, regardless of the underlying distribution.
# 
# 

# In[22]:


#Generating different values of m in the range of 1 to 1000 in a gap of 10 keeping μ=n/2 and σ=100 same for all the m
m_vector2 = np.arange(1,200,5)
mu=int(n/2)
m_vector2


# In[23]:


# Doing the sampling experiment for different values of m
m_vector_mean2 =[]
for m in m_vector2:
    sampled_mean_vector = []
    for i in range(m):
        S= 100 * np.random.randn() + mu
        S= math.ceil(S)
        if S > n:
            S=n
        elif S<= 0:
            S=1
        sample =random.sample(range(n), int(S))
        sampleTotalPay = salary[salary['Id'].isin(sample)]
        sampleTotalPay = sampleTotalPay['TotalPay']
        sample_mean =float(sampleTotalPay.mean())
        sampled_mean_vector.append(sample_mean)
    average_mean =s.mean(sampled_mean_vector)
    m_vector_mean2.append(average_mean)
m_vector_mean2
    


# In[24]:


plt.plot(m_vector_mean2,m_vector2,'go')
plt.axvline(x=mean, ymin=0, ymax=1,lw=2,c="red")
plt.xlabel('Average Mean Value')
plt.ylabel('m value')
plt.show()


# **Observation: ** Here we can see that as the value of m increases the sample mean gets close to the mean of entire column. This is because of central limit theorem which means the distribution of the average of a large number of independent, identically distributed variables will be approximately normal, regardless of the underlying distribution. Red line shows the mean of entire column.
