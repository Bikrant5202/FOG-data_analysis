#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import datetime as dt


# In[63]:


df = pd.read_csv("D:\\Minor project\\dataset_fog_release\\dataset\\S01R01.txt", header=None, delimiter=' ')


# In[64]:


column_names = ['time', 'ankle_acc_x', 'ankle_acc_y', 'ankle_acc_z', 'thigh_acc_x', 'thigh_acc_y', 'thigh_acc_z', 'trunk_acc_x', 'trunk_acc_y', 'trunk_acc_z', 'annotations']
df.columns = column_names


# In[65]:


df.head()


# In[66]:


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# In[27]:


#df['time'] = pd.to_datetime(df['time'], unit='s')


# In[ ]:





# In[67]:


plt.plot(df['ankle_acc_x'][:50])

# add labels and title
plt.xlabel('time')
plt.ylabel('ankle_acc_x')
plt.title('Ankle Acceleration X')


# In[75]:


pwd


# In[79]:


plt.figure(figsize=(20, 10))
plt.plot(df['time'], df['ankle_acc_x'], label='ankle_acc_x')
plt.plot(df['time'], df['ankle_acc_y'], label='ankle_acc_y')
plt.xlabel('time')
plt.ylabel('ankle acceleration')
plt.title('Ankle Acceleration X and Y')

plt.legend()
plt.savefig("minor project\plt.png")
plt.show()


# In[69]:


plt.plot(df['time'][:50], df['ankle_acc_x'][:50], label='ankle_acc_x')
plt.plot(df['time'][:50], df['ankle_acc_y'][:50], label='ankle_acc_y')
plt.xlabel('time')
plt.ylabel('ankle acceleration')
plt.title('Ankle Acceleration X and Y')

plt.legend()

plt.show()


# In[70]:


df_exp = df[df['annotations'].isin([2])]
print(df_exp)


# In[71]:


plt.figure(figsize=(20, 10))
plt.plot(df_exp['time'], df_exp['ankle_acc_x'], label='ankle_acc_x')
plt.plot(df_exp['time'], df_exp['ankle_acc_y'], label='ankle_acc_y')
plt.xlabel('time')
plt.ylabel('ankle acceleration')
plt.title('Ankle Acceleration X and Y')

plt.legend()

plt.show()


# In[57]:


import matplotlib.pyplot as plt
fig, axs = plt.subplots(11, figsize=(10, 20))

axs[0].plot(df_exp['time'], df_exp['ankle_acc_x'])
axs[0].set_title('Ankle Acc X')

axs[1].plot(df_exp['time'], df_exp['ankle_acc_y'])
axs[1].set_title('Ankle Acc Y')

axs[2].plot(df_exp['time'], df_exp['ankle_acc_z'])
axs[2].set_title('Ankle Acc Z')

axs[3].plot(df_exp['time'], df_exp['thigh_acc_x'])
axs[3].set_title('Thigh Acc X')

axs[4].plot(df_exp['time'], df_exp['thigh_acc_y'])
axs[4].set_title('Thigh Acc Y')

axs[5].plot(df_exp['time'], df_exp['thigh_acc_z'])
axs[5].set_title('Thigh Acc Z')

axs[6].plot(df_exp['time'], df_exp['trunk_acc_x'])
axs[6].set_title('Trunk Acc X')

axs[7].plot(df_exp['time'], df_exp['trunk_acc_y'])
axs[7].set_title('Trunk Acc Y')

axs[8].plot(df_exp['time'], df_exp['trunk_acc_z'])
axs[8].set_title('Trunk Acc Z')

axs[9].plot(df_exp['time'], df_exp['annotations'])
axs[9].set_title('Annotations')

axs[10].remove()
plt.show()


# In[56]:


col_to_plot = 'ankle_acc_x'
plt.scatter(df_exp['time'][:500], df_exp['ankle_acc_x'][:500])
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


# In[80]:


df1 = df_exp.iloc[:, 0:15]
axs[0].plot(df1['time'], df1['ankle_acc_x'])
axs[0].set_title('Ankle Acc X')

axs[1].plot(df1['time'], df1['ankle_acc_y'])
axs[1].set_title('Ankle Acc Y')

axs[2].plot(df1['time'], df1['ankle_acc_z'])
axs[2].set_title('Ankle Acc Z')

axs[3].plot(df1['time'], df1['thigh_acc_x'])
axs[3].set_title('Thigh Acc X')

axs[4].plot(df1['time'], df1['thigh_acc_y'])
axs[4].set_title('Thigh Acc Y')

axs[5].plot(df1['time'], df1['thigh_acc_z'])
axs[5].set_title('Thigh Acc Z')

axs[6].plot(df1['time'], df1['trunk_acc_x'])
axs[6].set_title('Trunk Acc X')

axs[7].plot(df1['time'], df1['trunk_acc_y'])
axs[7].set_title('Trunk Acc Y')

axs[8].plot(df1['time'], df1['trunk_acc_z'])
axs[8].set_title('Trunk Acc Z')

axs[9].plot(df1['time'], df1['annotations'])
axs[9].set_title('Annotations')

axs[10].remove()
plt.show()


# In[81]:


df_exp


# In[85]:


grouped_data = [df.iloc[i:i+15] for i in range(0, len(df), 15)]
grouped_stats_rows = []
for group_df in grouped_data:
    mean = group_df.mean()
    median = group_df.median()
    stats_row = {'time': group_df.index[0], 'mean': mean, 'median': median}
    grouped_stats_rows.append(stats_row)

grouped_stats = pd.concat([pd.DataFrame(row, index=[0]) for row in grouped_stats_rows], ignore_index=True)

grouped_stats = grouped_stats[['time', 'mean', 'median']]
print(grouped_stats)


# In[86]:


import numpy as np


# In[87]:


grouped_data = [df_exp.iloc[i:i+15] for i in range(0, len(df_exp), 15)]
grouped_stats_rows = []
for group_df in grouped_data:
    mean = group_df.mean()
    std = group_df.std()
    stats_row = {'time': group_df.index[0]}
    for col in df_exp.columns[1:]:
        stats_row[col + '_mean'] = mean[col]
        stats_row[col + '_std'] = std[col]
    grouped_stats_rows.append(stats_row)

grouped_stats = pd.DataFrame(grouped_stats_rows)
print(grouped_stats)


# In[91]:


print(grouped_stats.head())


# In[96]:


plt.figure(figsize=(50, 20))
means = grouped_stats.mean()
plt.scatter(x=means.index[1:], y=means[1:])
plt.xlabel('Attribute')
plt.ylabel('Mean Value')
plt.show()


# In[97]:


plt.figure(figsize=(20, 10))
means = grouped_stats.mean()
plt.plot(means.index[1:], means[1:], 'o-')
plt.xlabel('Attribute')
plt.ylabel('Mean Value')
plt.show()


# In[98]:


plt.figure(figsize=(20, 10))
std_devs = grouped_stats.std()
plt.plot(std_devs.index[1:], std_devs[1:], '-o')
plt.xlabel('Attribute')
plt.ylabel('Standard Deviation')
plt.show()


# In[ ]:




