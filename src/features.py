import pandas as pd

def engineer_features(df):
    """Transform cleaned data into ML-ready features"""
    df = df.copy()

    df = encode_categories(df)
    df = create_new_features(df)
    df = normalize_numeric(df)

    return df

def encode_categories(df):
    """Convert categorical columns to numbers — models need numbers, not text"""
    # Sex: male=0, female=1
    df['Sex'] = df['Sex'].map({'male': 0, 'female':1}).astype(int)

    # Embarked: S=0, C=1, Q=2
    df['Embarked'] = df['Embarked'].map({'S':0, 'C':1, 'Q':2}).astype(int)

    print(df[['Sex', 'Embarked']].dtypes)

    # Pclass is already numeric, just convert from category
    df['Pclass'] = df['Pclass'].astype(int)

    print("Encoded: Sex, Embarked, Pclass")
    return df

def create_new_features(df):
    """Create new columns that might help a model"""
    # Family size — alone vs with family might affect survival
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    #passanger alone
    df['IsAlone'] = (df['FamilySize']==1).astype(int)

    # Age group
    df['AgeGroup'] = pd.cut(
        df['Age'],
        bins = [0,12,18,35,60,100],
        labels = [0,1,2,3,4]
    ).astype(int)

    print("Created: FamilySize, IsAlone, AgeGroup")
    return df

def normalize_numeric(df):
    for col in ['Age','Fare','FamilySize']:
        min_val = df[col].min()
        max_val = df[col].max()
        df[col] = (df[col] - min_val) / (max_val - min_val)

    print("Normalized: Age, Fare, FamilySize")
    return df
