#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# read the csv file into a Pandas DataFrame
df = pd.read_csv('C:/Users/Windows 10/Desktop/WHO-COVID-19-global-data.csv')


# In[3]:


# view the first 5 rows of the DataFrame
df.head()


# In[5]:


#Check the size and shape of the dataset
print(f"Size: {df.size}")
print(f"Shape: {df.shape}")


# In[6]:


#Check for missing values
df.isnull().sum()


# In[8]:


#Filter the data to include only certain columns
new_df = df[['Country', 'Date_reported', 'New_cases', 'New_deaths']]


# In[9]:


#Filter the data to include only rows where the country is "United States":
us_df = df[df['Country'] == 'United States']


# In[10]:


#Group the data by country and calculate the total cases and deaths
grouped_df = df.groupby(['Country']).agg({'New_cases': 'sum', 'New_deaths': 'sum'})


# In[11]:


#Plot a line chart of the total cases and deaths by date
import matplotlib.pyplot as plt

date_df = df.groupby(['Date_reported']).agg({'New_cases': 'sum', 'New_deaths': 'sum'})
date_df.plot(kind='line', figsize=(10, 5))
plt.title('Total Cases and Deaths by Date')
plt.xlabel('Date')
plt.ylabel('Number of Cases/Deaths')
plt.show()


# In[12]:


#Plot a bar chart of the top 10 countries with the most cases
top10_df = grouped_df.sort_values(by='New_cases', ascending=False).head(10)
top10_df.plot(kind='bar', y='New_cases', figsize=(10, 5))
plt.title('Top 10 Countries with the Most Cases')
plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.show()


# In[15]:


#Calculate the total cases, deaths, and recoveries for each country and region
grouped_df = df.groupby(['Country', 'WHO_region']).agg({'New_cases': 'sum', 'New_deaths': 'sum' })

# Display the results
print(grouped_df)


# In[ ]:




