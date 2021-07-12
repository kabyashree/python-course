#var = 5
#var1 = "hello"
'''
print(var)
print(var1)
type(var) #get the data type
print(str(var) + var1)
'''

#var = input("enter a number")
#print(var)

### File handling
import pandas as pd

df = pd.read_csv('dataset/car data.csv')

df.head(10)   #return the first 10 rows
df.tail(5)  #return the last 5 rows
df.columns   #get all the columns of the csv file
df.shape # prints (number of rows and columns)
num_rows =  df.shape[0]
num_cols = df.shape[1]

df.iloc[0]  #get all the values of row 0
df.iloc[1] #get all the values of row 1
df[df.columns[0]]  #get all the values of column 0
df[df.columns[1]]  #get all the values of column 1

#Find missing values
pd.isnull(df)  #Find missing values one by one
pd.isnull(df).sum()  #find missing values for each column
pd.isnull(df).sum().sum()  #Find total sum of all missing values in entire dataset

if pd.isnull(df).sum().sum() ==0:
    print("Dataset has no missing values")
else:
    print("missing values found")
    df = df.dropna() #remove rows with missing values

df = df.dropna(subset=['Car_Name','Year'])  #remove rows with missing values in only these two columns

df.Car_Name.count()

abc = []
abc.append(23)
abc.append(45)


x1 = pd.DataFrame(df)
'''
abc
[23, 45]
abc[0]
23
abc[1]
45
len(abc)
2
abc.append(66)
abc
[23, 45, 66]
abc.append([44])
abc
[23, 45, 66, [44]]
abc.append([33,44,33])
abc
[23, 45, 66, [44], [33, 44, 33]]
len(abc)
5
abc[4]
[33, 44, 33]
abc[0]
23
abc[1]
45
abc[2]
66
abc[3]
[44]
abc[5]
'''


