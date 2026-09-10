#!/usr/bin/env python3


import pandas as pd
import numpy as np
# import seaborn as sns
# df = sns.load_dataset("titanic")

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
# ____________________________ part 1 ____________________________

# 1

# print(df.head(5))

# 2

rows, columns = df.shape
# print(f"Rows : {rows} Columns : {columns}")

# 3

# print(df.dtypes)

# 4

# print(df.describe(include=object))

# 5

c = df.isnull().sum()

c.sort_values(ascending=False)
# print(c)

# 6



# ____________________________ part 2 ____________________________

# 7

subset_columns = df[['Name', 'Sex', 'Age', 'Survived']]
# print(subset_columns)

# 8

# print(df.loc[df['Pclass'] == 1])

# 9

# print(df[['Name', 'Sex', 'Age', 'Survived']].loc[df['Age'] > 60])


# 10


# print(df[['Name', 'Sex', 'Age', 'Survived', 'Pclass']].loc[(df['Pclass'] == 3) & (df['Sex'] == "female")])


# 11

# print(df[['Name', 'Age']].loc[df['Age'].isnull()])

# 12

# print(df.iloc[10:20, 0:3])


# ____________________________ part 3 ____________________________


# 14

median_age = df['Age'].median()

df['Age'] = df['Age'].fillna(median_age)

# print(df['Age'].head(20))


# 15

# print(df.columns)
j = df['Embarked'].mode()

df['Embarked'] = df['Embarked'].fillna(j[0])


# print(df['Embarked'].iloc[50:70])


# 16

df['Has_Cabin'] = df['Cabin'].notnull()

# print(df[['Cabin', 'Has_Cabin']].iloc[800:890])