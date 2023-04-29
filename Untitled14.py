#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import datetime as dt


# In[23]:


df = pd.read_csv("D:\\Minor project\\dataset_fog_release\\dataset\\S01R01.txt", header=None, delimiter=' ')


# In[24]:


column_names = ['time', 'ankle_acc_x', 'ankle_acc_y', 'ankle_acc_z', 'thigh_acc_x', 'thigh_acc_y', 'thigh_acc_z', 'trunk_acc_x', 'trunk_acc_y', 'trunk_acc_z', 'annotations']
df.columns = column_names


# In[25]:


df.head()


# In[26]:


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# In[27]:


df['time'] = pd.to_datetime(df['time'], unit='s')


# In[ ]:





# In[29]:


plt.plot(df['ankle_acc_x'][:50])

# add labels and title
plt.xlabel('time')
plt.ylabel('ankle_acc_x')
plt.title('Ankle Acceleration X')


# In[52]:


plt.figure(figsize=(20, 10))
plt.plot(df['time'], df['ankle_acc_x'], label='ankle_acc_x')
plt.plot(df['time'], df['ankle_acc_y'], label='ankle_acc_y')
plt.xlabel('time')
plt.ylabel('ankle acceleration')
plt.title('Ankle Acceleration X and Y')

plt.legend()

plt.show()


# In[32]:


plt.plot(df['time'][:50], df['ankle_acc_x'][:50], label='ankle_acc_x')
plt.plot(df['time'][:50], df['ankle_acc_y'][:50], label='ankle_acc_y')
plt.xlabel('time')
plt.ylabel('ankle acceleration')
plt.title('Ankle Acceleration X and Y')

plt.legend()

plt.show()


# In[34]:


df_filtered = df[df['annotations'].isin([1,2])]
print(df_filtered)


# In[35]:


plt.plot(df_filtered['time'], df['ankle_acc_x'], label='ankle_acc_x')
plt.plot(df_filtered['time'], df['ankle_acc_y'], label='ankle_acc_y')
plt.xlabel('time')
plt.ylabel('ankle acceleration')
plt.title('Ankle Acceleration X and Y')

plt.legend()

plt.show()


# In[42]:


import matplotlib.pyplot as plt
fig, axs = plt.subplots(11, figsize=(10, 20))

axs[0].plot(df_filtered['time'], df_filtered['ankle_acc_x'])
axs[0].set_title('Ankle Acc X')

axs[1].plot(df_filtered['time'], df_filtered['ankle_acc_y'])
axs[1].set_title('Ankle Acc Y')

axs[2].plot(df_filtered['time'], df_filtered['ankle_acc_z'])
axs[2].set_title('Ankle Acc Z')

axs[3].plot(df_filtered['time'], df_filtered['thigh_acc_x'])
axs[3].set_title('Thigh Acc X')

axs[4].plot(df_filtered['time'], df_filtered['thigh_acc_y'])
axs[4].set_title('Thigh Acc Y')

axs[5].plot(df_filtered['time'], df_filtered['thigh_acc_z'])
axs[5].set_title('Thigh Acc Z')

axs[6].plot(df_filtered['time'], df_filtered['trunk_acc_x'])
axs[6].set_title('Trunk Acc X')

axs[7].plot(df_filtered['time'], df_filtered['trunk_acc_y'])
axs[7].set_title('Trunk Acc Y')

axs[8].plot(df_filtered['time'], df_filtered['trunk_acc_z'])
axs[8].set_title('Trunk Acc Z')

axs[9].plot(df_filtered['time'], df_filtered['annotations'])
axs[9].set_title('Annotations')

axs[10].remove()
plt.show()


# In[49]:


col_to_plot = 'ankle_acc_x'
plt.scatter(df['time'][:500], df['ankle_acc_x'][:500])
plt.xlabel('time')
plt.ylabel('ankle acceleration')
plt.title('Ankle Acceleration X and Y')


plt.show()


# In[47]:


colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'gray', 'brown', 'purple']

for i, col in enumerate(column_names):
    plt.scatter(df_filtered['time'], df[col], c=colors[i], label=col)

plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()

plt.show()


# In[ ]:




