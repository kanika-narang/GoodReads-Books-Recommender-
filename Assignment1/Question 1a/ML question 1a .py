
# coding: utf-8

# <center><h1> Machine Learning-I (CS/DS 706)-Assignment 1
# <h2>Chetna Jain (MT2016044)<br>
# Kanika Narang   (MT2016069)<br>
# Tehreem Ansari  (MT2016145)<br></h2><h1>
# 
# </center>

# Question 1 a.

# Step1: Load the Salary.csv dataset

# In[214]:


import pandas as pd
import numpy as np
import random
import math
import statistics as s
import matplotlib.pyplot as plt


# In[9]:


salary = pd.read_csv(r'/home/kanika/Downloads/Salaries.csv')


# In[13]:


salary = salary[['Id','TotalPay']]


# In[15]:


#Displaying top 5 rows
salary[:5]


# Step2: Calculate the Aggregate function on the entire column 'Total Pay'. The Agggregate function we picked is **mean**

# In[186]:


mean = salary['TotalPay'].mean()
print("Mean of the entire column 'TotalPay' = ",mean)


# Step 3  Pick a fraction in the range ρ ∈ (0, 1) : Let ρ =0.6

# In[57]:


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
print("List of m means is as follows \n",sampled_mean_vector    )


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

# In[215]:


p_vector = np.arange(0.01,1.01,0.01)
p_vector


# In[216]:


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

# In[217]:


plt.plot(p_vector,y,'gs')
plt.axhline(y=mean, xmin=0, xmax=1,lw=2,c="red")
plt.ylabel('Average Mean Value')
plt.ylabel('p value')
plt.show()


# Observation: 
# 
# As the value of p increases and gets close to 1, the value of the average mean from the m iterations of experiment generated gets close to value of the mean of the entire column ‘TotalPay’ also .
# 

# In[ ]:




