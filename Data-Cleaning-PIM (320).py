#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv("https://raw.githubusercontent.com/dakshsharmaa/Prevalence-of-Irregular-Menstruation/Data/Prevalence%20of%20Irregular%20Menstruation.csv")


# In[3]:


data.shape


# In[4]:


data.drop("Timestamp",axis=1,inplace=True)


# In[5]:


data.drop("Gender",axis=1,inplace=True)


# In[6]:


data.drop("By selecting 'I agree', you confirm that no coercion was exerted to fill this survey and you consent to provide information voluntarily without any monetary benefits attached to it. Do you agree?",axis=1,inplace=True)


# ###### Cleaning "Height" data

# In[7]:


data.loc[(data["Height (in cm)"] > 10) & (data["Height (in cm)"] < 90),"Height (in cm)"] = None


# In[8]:


for i in data["Height (in cm)"]:
    if i <90:
        data["Height (in cm)"].replace(i,(int(i)*30.48) + ((i-int(i))*2.54),inplace=True)


# In[9]:


data["Height (in cm)"].fillna(data["Height (in cm)"].mean(),inplace=True)


# In[10]:


data.head()


# ##### Calculating BMI

# In[11]:


BMI = (data["Weight (in kg)"] / data["Height (in cm)"] / data["Height (in cm)"])*10000
BMI = round(BMI,1)
BMI.tolist()


# In[12]:


# Adding BMI column
data.insert(1,'BMI',BMI)


# In[13]:


data.head()


# In[14]:


data["Age at Menarche"].unique()


# In[15]:


# Replacing 2016 with the mean
data.loc[data["Age at Menarche"]==2016,"Age at Menarche"] = None
data["Age at Menarche"].fillna(data["Age at Menarche"].mean(),inplace=True)


# In[16]:


data["Age at Menarche"].unique()


# In[17]:


data["Age at Menarche"]=data["Age at Menarche"].round(0)


# In[18]:


data


# In[19]:


data.rename({"What is the length of your menstrual cycle?":"Length of menstrual cycle"},inplace=True,axis=1)
data.head()


# In[20]:


len = data.loc[data["Is your menstrual flow normal?"]=="Yes","Length of menstrual cycle"]
len.replace([4,5,3,10],[30,30,30,60],inplace=True)


# In[21]:


data.loc[data["Is your menstrual flow normal?"]=="Yes","Length of menstrual cycle"] = len


# In[22]:


data.loc[data["Is your menstrual flow normal?"]=="Yes","Length of menstrual cycle"].unique()


# In[23]:


data["For how many days do you bleed?"].value_counts().sort_index()


# In[24]:


data.replace(60,10,inplace=True)   


# In[25]:


data["For how many days do you bleed?"].value_counts().sort_index()


# In[26]:


data["Is your menstrual flow normal?"].value_counts()   


# In[27]:


data["Is your menstrual flow normal?"].replace("No, Heavy Bleeding", "No, Heavy Flow", inplace=True)


# In[28]:


data["Is your menstrual flow normal?"].replace("No, Light Bleeding", "No, Light Flow", inplace=True)


# In[29]:


data["Is your menstrual flow normal?"].value_counts()   


# In[30]:


data.loc[data["Is your menstrual flow normal?"] == "Yes", "Is your menstrual flow normal?"] = 1


# In[31]:


data.loc[data["Is your menstrual flow normal?"] == "No, Heavy Flow", "Is your menstrual flow normal?"] = 2


# In[32]:


data.loc[data["Is your menstrual flow normal?"] == "No, Light Flow", "Is your menstrual flow normal?"] = 0


# In[33]:


data["Is your menstrual flow normal?"].value_counts() 


# In[34]:


data.head()


# In[35]:


data.head()


# In[36]:


data["Have you ever faced irregular menstruation?"].value_counts()  


# In[37]:


data.loc[data["Have you ever faced irregular menstruation?"] == "Yes", "Have you ever faced irregular menstruation?"] = 1


# In[38]:


data.loc[data["Have you ever faced irregular menstruation?"] == "No", "Have you ever faced irregular menstruation?"] = 0


# In[39]:


data["Have you ever faced irregular menstruation?"].value_counts()  


# In[40]:


data.head()


# In[41]:


pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)


# In[42]:


data.loc[data['Have you ever faced irregular menstruation?']== 0,['Have you ever faced irregular menstruation?','For how long have you faced irregular menstruation?','Is your menstrual cycle still irregular?','Do you know the reason behind your irregular menstrual cycle?','Have you tried any medications to regulate your menstruation?']]


# In[43]:


data.loc[data['Have you ever faced irregular menstruation?']== 1,['Have you ever faced irregular menstruation?','For how long have you faced irregular menstruation?','Is your menstrual cycle still irregular?','Do you know the reason behind your irregular menstrual cycle?','Have you tried any medications to regulate your menstruation?']]


# In[44]:


data.loc[data["Have you ever faced irregular menstruation?"]== 0,["Have you ever faced irregular menstruation?","Length of menstrual cycle","For how many days do you bleed?"]].describe()


# In[45]:


data.loc[data["Have you ever faced irregular menstruation?"]== 1,["Have you ever faced irregular menstruation?","Length of menstrual cycle","For how many days do you bleed?"]].describe()


# In[46]:


data['How often do you exercise?'].value_counts()   # No error


# In[47]:


data.loc[data["How often do you exercise?"] == "Alternate days", "How often do you exercise?"] = 2


# In[48]:


data.loc[data["How often do you exercise?"] == "I do not exercise", "How often do you exercise?"] = 0


# In[49]:


data.loc[data["How often do you exercise?"] == "Daily", "How often do you exercise?"] = 3


# In[50]:


data.loc[data["How often do you exercise?"] == "Once a week", "How often do you exercise?"] = 1


# In[51]:


data['How often do you exercise?'].value_counts()


# In[52]:


data.head()


# In[53]:


data["Do you smoke?"].value_counts()  # No error


# In[54]:


data.loc[data["Do you smoke?"] == "Non-Smoker", "Do you smoke?"] = 1


# In[55]:


data.loc[data["Do you smoke?"] == "Current Smoker", "Do you smoke?"] = 0


# In[56]:


data["Do you smoke?"].value_counts()


# In[57]:


data['How often do you consume alcohol?'].value_counts()  # No error


# In[58]:


data.loc[data["How often do you consume alcohol?"] == "Often", "How often do you consume alcohol?"] = 2


# In[59]:


data.loc[data["How often do you consume alcohol?"] == "Occasionally", "How often do you consume alcohol?"] = 1


# In[60]:


data.loc[data["How often do you consume alcohol?"] == "I do not drink", "How often do you consume alcohol?"] = 0


# In[61]:


data['How often do you consume alcohol?'].value_counts()


# In[62]:


data['Lastly, do you think the pandemic has affected your menstrual cycle? '].value_counts()   # No error


# In[63]:


data.loc[data["Lastly, do you think the pandemic has affected your menstrual cycle? "] == "No significant change", "Lastly, do you think the pandemic has affected your menstrual cycle? "] = 1


# In[64]:


data.loc[data["Lastly, do you think the pandemic has affected your menstrual cycle? "] == "Yes, for the worse", "Lastly, do you think the pandemic has affected your menstrual cycle? "] = 0


# In[65]:


data.loc[data["Lastly, do you think the pandemic has affected your menstrual cycle? "] == "Yes, for the better", "Lastly, do you think the pandemic has affected your menstrual cycle? "] = 2


# In[66]:


data['Lastly, do you think the pandemic has affected your menstrual cycle? '].value_counts() 


# In[67]:


data.head()


# ##### Calculation of Stress

# In[68]:


data["In the last month, how often have you felt confident about your ability to handle your personal problems?"].replace({0: 4, 1: 3, 3: 1, 4: 0}, inplace=True)


# In[69]:


data["In the last month, how often have you felt that things were going your way?"].replace({0: 4, 1: 3, 3: 1, 4: 0}, inplace=True)


# In[70]:


data["In the last month, how often have you been able to control irritations in your life?"].replace({0: 4, 1: 3, 3: 1, 4: 0}, inplace=True)


# In[71]:


data["In the last month, how often have you felt that you were on top of things?"].replace({0: 4, 1: 3, 3: 1, 4: 0}, inplace=True)


# In[72]:


data.head()


# In[73]:


data['Stress level']= data.iloc[:, 22:32].sum(axis=1)


# In[74]:


data.head()


# In[75]:


data.drop(data.iloc[:, 22:32], inplace = True, axis = 1)


# In[76]:


data.head()


# In[77]:


temp1 = data['Stress level']
data.drop(labels=['Stress level'], axis=1, inplace = True)
data.insert(22, 'Stress level', temp1)
data


# ##### Converting to numerical data

# In[78]:


data['Is your menstrual cycle still irregular?'].value_counts()


# In[79]:


data.loc[data["Is your menstrual cycle still irregular?"] == "No", "Is your menstrual cycle still irregular?"] = 0


# In[80]:


data.loc[data["Is your menstrual cycle still irregular?"] == "Yes", "Is your menstrual cycle still irregular?"] = 1


# In[81]:


data['Is your menstrual cycle still irregular?'].value_counts()


# In[82]:


data['Have you tried any medications to regulate your menstruation?'].value_counts()


# In[83]:


data.loc[data["Have you tried any medications to regulate your menstruation?"] == "No", "Have you tried any medications to regulate your menstruation?"] = 0


# In[84]:


data.loc[data["Have you tried any medications to regulate your menstruation?"] == "Yes", "Have you tried any medications to regulate your menstruation?"] = 1


# In[85]:


data['Have you tried any medications to regulate your menstruation?'].value_counts()


# In[86]:


data.loc[data["Have you ever used any birth control medication/undergone a surgery?"] == "No", "Have you ever used any birth control medication/undergone a surgery?"] = 0


# In[87]:


data.loc[data["Have you ever used any birth control medication/undergone a surgery?"] == "Yes", "Have you ever used any birth control medication/undergone a surgery?"] = 1


# In[88]:


data['Have you ever used any birth control medication/undergone a surgery?'].value_counts()


# In[89]:


data


# In[136]:


data.loc[data["Reason for irregular cycle"]=="No","Reason for irregular cycle"]=0


# In[138]:


data.loc[data["Reason for irregular cycle"]=="Yes, Stress","Reason for irregular cycle"]=1


# In[139]:


data.loc[data["Reason for irregular cycle"]=="Yes, PCOD/PCOS","Reason for irregular cycle"]=2


# In[140]:


data.loc[data["Reason for irregular cycle"]=="Yes, Hormonal Imbalance","Reason for irregular cycle"]=3


# In[141]:


data.loc[data["Reason for irregular cycle"]=="Yes, Thyroid","Reason for irregular cycle"]=4


# In[147]:


data["Reason for irregular cycle"].value_counts()


# In[159]:


data["Reason for irregular cycle"].isna().sum()


# In[171]:


data.loc[(data["Reason for irregular cycle"]!=0)&(data["Reason for irregular cycle"]!=1)&(data["Reason for irregular cycle"]!=2)&(data["Reason for irregular cycle"]!=3)&(data["Reason for irregular cycle"]!=4)&(data["Reason for irregular cycle"].isna()==False),"Reason for irregular cycle"]=5


# In[175]:


data["Reason for irregular cycle"].value_counts()


# ##### Renaming columns

# In[91]:


data.rename({"For how many days do you bleed?":"Length of periods"},inplace=True,axis=1)


# In[92]:


data.rename({"Is your menstrual flow normal?":"Menstrual flow"},inplace=True,axis=1)


# In[93]:


data.rename({"Have you ever faced irregular menstruation?":"Irregular menstruation (Y/N)"},inplace=True,axis=1)


# In[94]:


data.rename({"For how long have you faced irregular menstruation?":"Irregular menstruation (Months)"},inplace=True,axis=1)


# In[95]:


data.rename({"Is your menstrual cycle still irregular?":"Irregular cycle (Y/N)"},inplace=True,axis=1)


# In[96]:


data.rename({"Do you know the reason behind your irregular menstrual cycle?":"Reason for irregular cycle"},inplace=True,axis=1)


# In[97]:


data.rename({"Have you tried any medications to regulate your menstruation?":"Medications (Y/N)"},inplace=True,axis=1)


# In[98]:


data.rename({"Have you ever used any birth control medication/undergone a surgery?":"Birth control meds/Surgery (Y/N)"},inplace=True,axis=1)


# In[99]:


data.rename({"I eat a balanced diet/ I eat foods that are high in antioxidants, nutrient-dense, and with plenty of protein.":"Consumption of balanced diet"},inplace=True,axis=1)


# In[100]:


data.rename({"I eat enough green vegetables.":"Consumption of green vegetables"},inplace=True,axis=1)


# In[101]:


data.rename({"I eat an ample amount of fruits rich in vitamin C.":"Consumption of vitamin C"},inplace=True,axis=1)


# In[102]:


data.rename({"I often eat junk food.":"Consumption of Junk food"},inplace=True,axis=1)


# In[103]:


data.rename({"I consume chicken and other non-vegetarian food on a regular basis.":"Consumption of non-veg food"},inplace=True,axis=1)


# In[104]:


data.rename({"I drink tea or coffee daily.":"Consumption of tea/coffee daily"},inplace=True,axis=1)


# In[105]:


data.rename({"How often do you exercise?":"Exercise"},inplace=True,axis=1)


# In[106]:


data.rename({"Do you smoke?":"Smoking"},inplace=True,axis=1)


# In[107]:


data.rename({"How often do you consume alcohol?":"Consumption of alcohol"},inplace=True,axis=1)


# In[108]:


data.rename({"Lastly, do you think the pandemic has affected your menstrual cycle? ":"Effect of pandemic on cycle"},inplace=True,axis=1)


# In[109]:


data


# In[110]:


data.dtypes


# ##### Converting Number of months into categories

# In[111]:


data['Irregular menstruation (Months)'].max()


# In[112]:


data['Irregular menstruation (Months)']=pd.cut(data['Irregular menstruation (Months)'], bins=[0, 6, 12, 24, 60, 193], include_lowest=True, labels=[0, 1, 2, 3, 4])


# In[113]:


data.drop("What are some methods or techniques you have tried that helped you to regulate your menstruation?",axis=1,inplace=True)


# In[114]:


data


# In[115]:


cor = data.corr()


# In[116]:


cor


# In[117]:


plt.subplots(figsize=(10,10))
sns.heatmap(cor,cmap="Pastel1", square=True);


# In[118]:


data.to_csv('PIM_(320).csv')


# In[ ]:




