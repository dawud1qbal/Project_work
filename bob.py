import pandas as pd
df = pd.read_csv("C:/Users/S1109967/Downloads/new_titanic.csv")
""" print(df)
print("Shape of DataFrame:", df.shape)
print("/nFirst few rows:")
print(df.head())
print("/nSummary Information:")
print(df.info())
print("/nDescriptive Statisitcs:")
print(df.describe())


print("Missing Values Count:")
print(df.isnull().sum())

df = df.dropna()
df = df.drop_duplicates()

df['Age'] = df['Age'].astype(int)

print("/nCleaned DataFrame:")

print("First five rows of 'Name' and 'Age' columns:")
print(df.loc[0:4, ['Name', 'Age']])

df = df[df['Age'] > 30]

df['FamilySize'] = df['SibSp'] + df['Parch']

df = df.groupby('Pclass').agg({'Age': 'mean'}) """

print("First five rows of 'Name' and 'Age' columns:")
print(df.loc[0:4, ['Name', 'Age']])