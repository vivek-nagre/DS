import pandas as pd
import numpy as np
import seaborn as snb

import matplotlib.pyplot as plt
print(".....first assignment..."*4)
print("Q>1 version of pandas?")
print("answer:->version of pandas is:",pd.__version__)
arr=np.array([[12,23,43],[15,69,90]])
print("my one dimentional array is:",arr)
print("size of my arr :",np.size(arr))
print("dimention of arr:",np.ndim(arr))
# i have converted the 2-D array into 1d array
print()
print()
One_D=np.hstack(arr)
print("my one dimentional array is:",One_D)
print("shape of my one dimentional array is:",np.shape(One_D))
print("size of my one dimentional array is:",np.size(One_D))
print("dimention of One_D is:",np.ndim(One_D))


print(".....Secound question.... "*4)
print("make a series of the array using pandas")
print("series of array:")
print(pd.Series(One_D))

print(".....Third question.... "*4)
print("How to convert the index of a series into a column of a dataframe?")
dataset={'rno':['Er001','Er003','Er003','Er004',],'name':['shree','sanjay','shubam','amit'],'mark':[30,43,56,78],'grade':['C','B','B','A']}
# print(dataset)
for x in dataset:
    print (x)
    # print(y)
df=pd.DataFrame(dataset)
print(df)

print("index series into data frame")
print(arr)
print(pd.DataFrame(arr))
print("being crazy..")
print(pd.DataFrame(One_D)[0][1])
print()
print()
print(".....Fourth Question..."*5)

print("following dataset avaliable in the seaborn:\n",snb.get_dataset_names())
for a in snb.get_dataset_names():
    print(a)
print()
print()
print("...Question number 5..."*5)
ds=snb.load_dataset('mpg')
print(ds)
print("country count in the\'mpg' data set")
print("all the count ")
print(ds['origin'].describe())
print()
print("country of the car is in the dataset......")
print()
print()
for cont in  ds['origin'].unique():
    print(cont)
print("distribution of count for each country coantaing number of car's")
print(ds['origin'].value_counts())
print()
print()
print("...Question six..."*5)
print("Extract the part of the dataframe which contains cars belonging to 'usa'")
print(snb.displot(ds['origin']))

print("extraction of dataset having car origin \'USA")
print(ds['origin']=='usa')
print(ds.shape)
print(ds.ndim)
