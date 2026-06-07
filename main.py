from src.loader import load_data, audit_data
from src.cleaner import clean_data
from src.analyzer import analyze_data
from src.features import engineer_features


df = load_data('data/titanic.csv')
audit_data(df)

df_clean = clean_data(df)

analyze_data(df_clean)

df_features = engineer_features(df_clean)

print("\n--- Final ML-Ready Dataset ---")
print(df_features.head())
print(f"\nShape: {df_features.shape}")
print(f"\nDtypes:\n{df_features.dtypes}")

df_features.to_csv('output/clean_data.csv', index=False)
print("\nSaved to output/clean_data.csv")