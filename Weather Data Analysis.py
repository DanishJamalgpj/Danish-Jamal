#!/usr/bin/env python
# coding: utf-8

# # Weather Data Analysis with python

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("Weather Data.csv")


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.shape


# In[6]:


data.value_counts()


# In[7]:


#to show the all columns available in data
data.columns


# In[8]:


#data types of every columns in the data
data.dtypes


# In[9]:


#data cleaning >> cheaking if there is null value in data and how many times it is in data
data.isnull().sum()


# In[10]:


#>>> so there is no null value in the data
#we can also cheak with 'notnull()' method to check all column have value or not


# In[11]:


#showing the unique value (elements) of columns('Weather')
data['Weather'].unique()


# In[12]:


#showing the unique value(elements available) in each column 
data.nunique()


# In[13]:


#Showing how many (elements) in 'Weather' Column
weather_data=data['Weather']
weather_data.nunique()


# In[14]:


#Showing how much time Weather changes and which weather mostly appeared 
data['Weather'].value_counts()


# In[15]:


#Basic information about our dataset ('Weather_Data')
data.info()


# In[16]:


#Showing the all unique values of column 'WindWind Speed_km/h' from data
data['Wind Speed_km/h'].nunique()


# In[17]:


data['Wind Speed_km/h'].unique()


# # Showing how many time 'Weather is exactly clear'

# In[18]:


#first cheaking data head to know about column name
data.head(2)


# In[19]:


#Now cheaking for column(Weather) values and elements
data['Weather'].value_counts()


# In[20]:


#Now >> Showing how many time 'Weather is exactly clear'
data[data['Weather']=='Clear'].head(50)


# In[21]:


#Cheaking same value by using groupby method
data.groupby('Weather').get_group('Clear').head(50)


# # Showing the number of times when 'Wind Speed_km/h was exactrly 4 km/h'

# In[22]:


data.head(4)


# In[23]:


data[data['Wind Speed_km/h']== 4]   #we can use .head(474) method to show all the row which have result '4'


# In[24]:


# Renaming a column name ('Weather'  with 'Weather Condition') >> In case client ask to change name
data.rename(columns={'Weather':'Weather Condition'},inplace=True) #>>inplace-True is for permanent rename otherwise it will rename only temporary


# In[25]:


data.head(2)


# In[26]:


#showing the mean value of 'Visibility_km' using mean()
data['Visibility_km'].mean()


# In[27]:


#Showing the the standard deviation of '(Press_kPa)' in the DataFrame.using std() Note Press_kPa stand for 'Pressure' 
data['Press_kPa'].std()


# In[28]:


#Showing the variance of 'Relative Humidity'in the data using var()
data['Rel Hum_%'].var()


# In[29]:


#Showing all the instances when 'Snow' was recorded
data.head(2)


# In[30]:


data[data['Weather Condition']=='Snow']  #we can use .head(390) for show all the record


# In[31]:


#their is more elements with word snow.. like 'Snow Fog', 'Rain,Snow','Snow,Haze' etc
#Showing all the record which is contains word 'Snow'
data[data['Weather Condition'].str.contains('Snow')].head(50)


# In[32]:


#showing all instances when 'Wind speed' is 24 and 'Visibility' above 25
data.head(2)


# In[33]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)].head(50)


# In[34]:


#showing the mean value of each column against each 'Weather Condition'
data.groupby('Weather Condition').mean()


# In[35]:


#Showing the min and max value of each column against each 'Weather Condtition'
# 1st Min Value
data.groupby('Weather Condition').min()


# In[36]:


#2nd Max Value
data.groupby('Weather Condition').max()


# In[37]:


#Showing all recode when 'Weather Condition' was Fog;
data[data['Weather Condition']=='Fog']


# In[38]:


#Showing all instances when 'Weather is clear' or 'Visibility is above 40'
data.head(2)


# In[39]:


data[(data['Weather Condition']=='Clear') | (data['Visibility_km'] > 40)]


# In[40]:


#Showing all instances when : >> weather is clear and relative humidity is greater than 50' or visibility is above 40.
data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%']>50 ) | (data['Visibility_km']>40)]


# In[41]:


import matplotlib
from matplotlib import pyplot as plt

final_weather = data[(data['Weather Condition']=='Clear')].head(10)
WindSpeed = data[(data['Wind Speed_km/h']>4)]


# In[42]:


final_weather


# In[43]:


WindSpeed 


# In[44]:


Weather = data[data['Weather Condition']=='Clear'].head(20)
rel_hum = data['Rel Hum_%'].head(20)
visibility = data['Visibility_km'].head(20)


# In[45]:


plt.subplot(1,2,1)
plt.hist(data['Rel Hum_%'].head(10),color='r',bins=6)
plt.title('RelationHumidity')
plt.subplot(1,2,2)
plt.hist(visibility,bins=10)
plt.title=('Visibility_km')
plt.show()


# In[46]:


plt.pie(data['Rel Hum_%'].head(20),labels=data['Weather Condition'].head(20),autopct='%0.1f%%',shadow=True,startangle=190)
#plt.title('Top 20 Rel Humidity Percantage Against Weather Condition pie chart')
fig = plt.gcf()
fig.set_size_inches(10,10)
plt.show()


# In[47]:


d1=data.groupby('Weather Condition')=='Clear','Fog','Cloudy','Haze'


# In[48]:


d1


# In[49]:


data.head(2)


# In[50]:


plt.pie(data['Wind Speed_km/h'].head(10),labels=data['Weather Condition'].head(10),autopct='%0.1f%%',shadow=True)
#plt.title('TOP 20 WIND SPEED PER % AGAINST WEATHER CONDITION')
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.show()


# In[51]:


data


# In[52]:


data['Weather Condition']


# In[53]:


data.head(2)


# In[54]:


c=data[(data['Weather Condition']=='Clear') & (data['Wind Speed_km/h']>4)]


# In[55]:


c


# In[56]:


plt.pie(c['Wind Speed_km/h'].head(10),labels=c['Weather Condition'].head(10),autopct='%0.1f%%')
plt.show


# In[57]:


data.head(2)


# In[58]:


data['Date/Time'].head(2)


# In[59]:


data['Date/Time'].unique()


# In[65]:





# In[61]:





# In[ ]:





# In[ ]:




