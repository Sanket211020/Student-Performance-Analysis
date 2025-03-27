#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data= pd.read_excel("C:/Users/SAINATH/Downloads/student performace excel.xlsx")


# In[3]:


data


# In[4]:


data.describe()


# In[5]:


data.info()


# In[6]:


type(data)


# In[7]:


data.shape


# In[8]:


data.isnull().sum()


# In[9]:


data.duplicated().sum()


# In[10]:


data["Parent_Education_Level"].fillna("Uneducated", inplace=True)


# In[11]:


data.isnull().sum()


# In[12]:


att_min = data["Attendance (%)"].min()


# In[13]:


att_min


# In[14]:


data["Attendance (%)"].fillna(att_min,inplace=True)


# In[15]:


data.isnull().sum()


# In[16]:


ass_min=data["Assignments_Avg"].min()


# In[17]:


ass_min


# In[18]:


data["Assignments_Avg"].fillna(ass_min, inplace=True)


# In[19]:


data


# In[20]:


data.isnull().sum()


# In[21]:


data.set_index("Student_ID")


# In[22]:


df1=data[data["Gender"]=="Male"]
df1
df1.shape


# In[23]:


df2=data[(data["Gender"]=="Male") & (data["Department"]=="CS")]
df2
df2.shape


# In[24]:


df3= data[(data["Total_Score"]>=90) & (data["Grade"]=="A")]
df3


# In[25]:


df4= data.sort_values("Projects_Score",ascending=False)


# In[26]:


df4


# In[27]:


df4= data.groupby(["Department","Gender"])[["Total_Score","Final_Score"]].mean()


# In[28]:


df4


# In[29]:


df5= data.groupby("Parent_Education_Level")["Sleep_Hours_per_Night"].min()
df5


# In[30]:


data


# In[31]:


import matplotlib.pyplot as plt


# In[32]:


df6= data["Department"].value_counts()
df6


# In[33]:


data.columns


# In[34]:


df6.index


# In[35]:


df7= data.groupby("Department")[["Midterm_Score","Final_Score"]].agg({"sum","min", "max","count"})


# In[36]:


df7


# In[37]:


df8= data.groupby("Department")[["Midterm_Score","Final_Score"]].agg({"max"})


# In[38]:


df8.plot.bar()
plt.show()


# In[39]:


df10=data.groupby("Department")["Study_Hours_per_Week"].count()
df10


# In[40]:


df10.plot.bar(x=["Department"], y=["Study_Hours_per_Week"])
plt.show()


# In[41]:


df10.plot.bar()
plt.show()


# In[42]:


df10.plot.line()
plt.show()


# In[43]:


df10.plot.pie(autopct="%.2f%%")
plt.show()


# In[ ]:




