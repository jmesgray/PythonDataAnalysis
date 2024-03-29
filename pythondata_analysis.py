# -*- coding: utf-8 -*-
"""pythondata_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Bd0eEPEktJLAp5ooiZgZvfxCdB65EF3

# Data Analysis using Python

# 1.1
"""

# Commented out IPython magic to ensure Python compatibility.
# Importing and reading housing.header.txt as a dataframe
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from google.colab import files 
uploaded = files.upload()

# Reporting the number of instances and features
import io
dataset = pd.read_csv(io.BytesIO(uploaded['housing.header.csv']))
print(dataset)
print(dataset.shape) # 506 rows and 14 columns

"""# 1.2 """

# Reporting all samples with respect to Crim index on a plot
y = dataset['Crim']
x=np.arange(y.shape[0])

plt.scatter(x, y, marker='o')

"""# 1.3"""

# Showing histogram of Crim index and density of Crim index on a 1x2 frame
import seaborn as sns

# Index
plt.subplot(1,3,1)
sns.distplot(dataset['Crim'], hist=True, kde=False, bins=20,color='blue',
             hist_kws={'edgecolor':'black'}) 
# Density
plt.subplot(1, 3, 3)
sns.distplot(dataset['Crim'], hist=True, kde=True, bins=20, color='blue',
             hist_kws={'edgecolor': 'red'})

"""# 1.4"""

# Reporting correlation to medium house value Medv via scatterplots
plt.figure(figsize=(20, 5))

features = ['Crim', 'Rm', 'Age', 'Tax']
target = dataset['Medv']

for i, col in enumerate(features):
  plt.subplot(1, len(features) , i+1)
  x = dataset[col]
  y = target
  plt.scatter(x, y, marker='o')
  plt.title(col)
  plt.xlabel(col)
  plt.ylabel('Medium House Value')

"""#### To conclude, the variable that shows the strongest correlation with the medium house value is Rm. The number of rooms per dwelling creates an increase in price of a house, as shown by the positive correlation between the two attributes. 
#### Crim, Age, and Tax attributes do not show a clear correlation based upon their scatterplots. A conclusion can not be made from their plots.

# 1.5
"""

# Creating a subset with Crim less than 1 and Rm greater than 6
dataset.filter = dataset[(dataset['Crim']<1) & (dataset['Rm']>6)] 
subset = dataset.filter
subset.head 
# Subset dataset with filter applied now has a total of 236 rows and 14 columns

"""# 1.6"""

# Showing scatterplot between Rm and Medv;
# 7 or larger Rm values as red; rest is black
plt.figure(figsize=(20, 5)) # creating the size of the graph
x = dataset['Rm'].values
y = dataset['Medv'].values
plt.xlabel('Rm')
plt.ylabel('Medv')
plt.title('Rm vs Medv')
plt.scatter(x, y, color=["red" if val >= 7 else "black" for
                         val in dataset['Rm']])
plt.show()

"""# 1.7"""

# Another scatterplot between Rm and Crim with all 506 properties on the plot. 
# When Medv is greater than or equal to 24, color red. Rest is black

plt.figure(figsize=(20, 5))
plt.scatter(dataset['Rm'], dataset['Crim'], color=["red" if val >= 24 else
                                         "black" for val in dataset['Crim']])
plt.title('Rm vs Crim')
plt.xlabel('Rm')
plt.ylabel('Crim')

"""# 1.8"""

# Reporting pairwise correlation between every two variables as a matrix
from pandas.plotting import scatter_matrix
scatter_matrix(dataset, figsize=(15, 15))
plt.show()

"""# 1.9 
#### Rm is most positively correlated to Medv. This can be concluded based upon the correlation matrix, which gave a value of 0.70. The most negatively correlated to Medv is Lstat, with a correlation value of -0.74. 
"""

correlation_matrix = dataset.corr().round(2) # This is the code to answer 6.9
correlation_matrix

"""# 1.10"""

# Drawing scatterplots to show relationship between each attribute and Medv
plt.figure(figsize=(20, 5))

features = ['Crim', 'Zn', 'Indus', 'Chas', 'Nox', 'Rm', 'Age', 'Dis', 'Rad', 
            'Tax', 'Ptratio', 'B', 'Lstat', 'Medv']
target = dataset['Medv']

for i, col in enumerate(features):
  plt.subplot(1, len(features) , i+1)
  x = dataset[col]
  y = target
  plt.scatter(x, y, marker='o')
  plt.title(col)
  plt.xlabel(col)
  plt.ylabel('Medv')

"""# 1.11
#### You can use scatterplots to find attributes which are positively correlated by looking at the direction of the slope created by the aggregation of data points. If a correlation is present between two attributes, then the data points on the plot will resemble a diagonal line across the graph. You can do this in python by running a series of scatterplots using the python library pandas and matplotlib. If the data points do not create a sloped line, very little to no correlation is present between the two variables. 
#### You can also create a correlation matrix, which will display all the attributes' correlations with each other. Lowest negatives and highest positives will give you your solution for the least and most correlated attributes repectively. Values closest to 0 resemble attributes that show none to very little correlation.

# 1.12
"""

# Creating a new instance for the original dataset 
new_instance = {'Crim':1, 'Zn':0.2, 'Indus':6, 'Chas':0, 'Nox':6.5, 'Rm':5,
                'Age':100, 'Dis':4.1, 'Rad':4.5, 'Tax':21, 'Ptratio':20,
                'B':300, 'Lstat':12, 'Medv':20.5}
updated_dataset1 = dataset.append(new_instance, ignore_index=True)
print(updated_dataset1)
print(updated_dataset1.shape) # 507 rows and 14 columns in updated dataset1

"""# 1.13"""

# Creating a new feature named "Dummy" onto the original dataset
import random # This is the library needed to generate the random integers 
updated_dataframe = pd.DataFrame(dataset)
print(updated_dataframe.shape)

Dummy = [random.randrange(0, 5, 1) for i in range(506)] 
# Displaying the newly created list to be appended to the orignal dataset. 
updated_dataframe['Dummy'] = Dummy
print(updated_dataframe) 
# Updated dataframe now has 506 rows and 15 columns