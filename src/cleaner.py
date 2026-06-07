import pandas as pd

def clean_data(df):
    df = df.copy()

    # 1. Drop columns too broken to use
    df = drop_useless_columns(df)

    # 2. Fix missing values
    df = fix_missing_values(df)

    # 3. Fix data types
    df = fix_dtypes(df)

    return df

def drop_useless_columns(df):
    """Drop columns with too much missing data or no ML value"""
    # Cabin is 77% missing — not recoverable
    # Name and Ticket have no predictive value as raw text
    df = df.drop(columns=['Cabin','Name','Ticket','PassengerId'])
    print("Dropped: Cabin, Name, Ticket, PassengerId")
    return df

def fix_missing_values(df):
    """Fill missing values with appropriate strategy"""
    # Age: fill with median (more robust than mean for skewed data)
    df['Age'] = df['Age'].fillna(df['Age'].median())

    # Embarked: only 2 missing, fill with mode (most common value)
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    print("Fixed missing values: Age, Embarked")
    return df

def fix_dtypes(df):
    df['Sex'] = df['Sex'].astype('category')
    df['Embarked'] = df['Embarked'].astype('category')
    df['Pclass'] = df['Pclass'].astype('category')

    print("Fixed dtypes: Sex, Embarked, Pclass")
    return df