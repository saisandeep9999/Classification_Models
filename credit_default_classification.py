#Setting the working directory
import os 
os.chdir("D:\\Insofe_Resources\\Practice\\Amazon_Dataset")

#Importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd
import re

#Reading the dataset
xl = pd.ExcelFile('default of credit card clients.xls')
xl.sheet_names

dataset = xl.parse("Data")
dataset.head()
list(dataset)

#Setting the column names
dataset.drop(dataset.index[[0]], inplace = True)
col_names = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', "PAY_5", 'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3',  'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6', 'default payment next month']
dataset.columns = col_names
len(col_names)
#Glancing through the dataset
dataset.head()
dataset.tail()
dataset.dtypes
dataset.describe()

#Changing the column datatypes in the dataset
values = [0, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
num_vars =[]
for i in values:
    num_vars.append(col_names[i])
print(num_vars)

vals = [1, 2, 3, 5, 6, 7, 8, 9, 10, 23]
cat_vars = []
for i in vals:
    cat_vars.append(col_names[i])
print(cat_vars)

for i in num_vars:
    dataset[i] = dataset[i].astype('float')
for i in cat_vars:
    dataset[i] = dataset[i].astype('category')

#Descriptive analysis on the data
#Payment Delays
pattern = re.compile("^PAY_[0-9]+$")
pay_status_columns = [ x for x in dataset.columns if (pattern.match(x))]
dataset[pay_status_columns].head(10)

#Plotting pay status columns
pattern = re.compile("^PAY_[0-9]+$")
pay_status_columns = [ x for x in dataset.columns if (pattern.match(x))]

fig, ax = plt.subplots(2,3)
fig.set_size_inches(15,5)
fig.suptitle('Distribution of dalays in the past 6 months')

for i in range(len(pay_status_columns)):
    row,col = int(i/3), i%3
    d  = dataset[pay_status_columns[i]].value_counts()
    ax[row,col].bar(d.index, d, align='center', color='g')
    ax[row,col].set_title(pay_status_columns[i])

plt.tight_layout(pad=3.0, w_pad=0.5, h_pad=1.0)
plt.show()

#Bill columns
pattern = re.compile("^BILL_AMT[0-9]+$")
bill_status_columns = [x for x in dataset.columns if (pattern.match(x))]
dataset[bill_status_columns].head(10)
dataset[bill_status_columns].describe()

#pay amt columns
pattern = re.compile("^PAY_AMT[0-9]+$")
pay_amount_columns = [ x for x in dataset.columns if (pattern.match(x))]
dataset[pay_amount_columns].describe()

#visualizing the dependent variable default payment next month
sns.countplot(x = 'default payment next month', data = dataset)
plt.show()

dataset['default payment next month'].value_counts(1)


