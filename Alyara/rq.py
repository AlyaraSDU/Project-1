#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd


# In[58]:


df = pd.read_excel('Project/job_listings_all_pages.xlsx')
df


# In[59]:


count_c = df['Company'].value_counts(dropna=False)
print(count_c)


# In[60]:


mh_company = df[df['Company']=='АО Народный банк Казахстана']
mh_company.loc[mh_company['Experience']=='Опыт более 6&nbsp;лет', 'Experience'] = 'Опыт более 6 лет'
mh_company


# In[61]:


experience = mh_company['Experience'].unique().tolist()
experience


# In[62]:


count_level = mh_company['Experience'].value_counts(dropna=False)
count_level


# In[74]:


results = [count_c.head(1), count_level]
results


# In[ ]:




