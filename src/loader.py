import pandas as pd

def load_data(filepath):
    """Load CSV and return DataFrame"""
    df = pd.read_csv(filepath)
    return df

def audit_data(df):
    """Print basic audit of the dataset"""
    print("="*40)
    print("DATASET AUDIT")
    print("="*40)
    print(f"Shape : {df.shape}")
    print(f"\nMissing Values :\n {df.isnull().sum()}")
    print(f"\nData Types:\n {df.dtypes}")
    print(f"\nFirst 5 rows:\n{df.head()}")
    print("="*40)