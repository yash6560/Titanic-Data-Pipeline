import pandas as pd

def analyze_data(df):
    """Run full EDA on cleaned dataset"""
    survival_by_gender(df)
    survival_by_class(df)
    age_distribution(df)
    correlation_summary(df)

def survival_by_gender(df):
    print("\n--- Survival Rate by Gender ---")
    result = df.groupby('Sex')['Survived'].mean().round(3)*100
    print(result.to_string())

def survival_by_class(df):
    print("\n--- Survival Rate by Passenger Class ---")
    result = df.groupby('Pclass')['Survived'].mean().round(3)*100
    print(result.to_string())

def age_distribution(df):
    print("\n--- Age Distribution ---")
    print(f"Min Age {df['Age'].min()}")
    print(f"Max Age {df['Age'].max()}")
    print(f"Mean Age {df['Age'].mean().round(2)}")
    print(f"Median  Age {df['Age'].median()}")

def correlation_summary(df):
    print("\n--- Correlation with Survival ---")
    # Only numeric columns
    numeric_df = df.select_dtypes(include='number')
    corr = numeric_df.corr()['Survived'].drop('Survived').round(3)
    print(corr.sort_values(ascending=False).to_string())