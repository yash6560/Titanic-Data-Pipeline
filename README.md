# Titanic Data Pipeline

A beginner-friendly data engineering and data analysis project built using the Titanic dataset. This project demonstrates a complete data pipeline including data loading, cleaning, feature engineering, analysis, and preprocessing for machine learning.

## Project Overview

The pipeline performs the following tasks:

- Load Titanic dataset
- Clean missing values
- Analyze passenger data
- Encode categorical features
- Create new features
- Normalize numeric columns
- Generate processed data for machine learning

## Project Structure

```text
Titanic-Data-Pipeline/
│
├── data/
│   ├── raw/
│   │   └── titanic.csv
│   └── processed/
│
├── output/
│   └── analysis_report.txt
│
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── cleaner.py
│   ├── analyzer.py
│   └── features.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Features

### Data Cleaning

- Fill missing Age values using median
- Fill missing Embarked values using mode
- Remove unnecessary missing data

### Feature Engineering

- FamilySize
- IsAlone
- AgeGroup

### Encoding

- Sex:
  - male = 0
  - female = 1

- Embarked:
  - S = 0
  - C = 1
  - Q = 2

### Normalization

Numeric features are scaled to the range:

```text
0 → 1
```

Using Min-Max Scaling:

```python
(x - min) / (max - min)
```

## Analysis Included

- Survival rate by gender
- Survival rate by passenger class
- Age distribution statistics
- Correlation with survival

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Titanic-Data-Pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the pipeline:

```bash
python main.py
```

## Sample Output

```text
========================================
Titanic Data Pipeline
========================================

Loaded dataset successfully
Cleaned missing values
Created: FamilySize, IsAlone, AgeGroup
Encoded: Sex, Embarked, Pclass
Normalized: Age, Fare, FamilySize

--- Survival Rate by Gender ---
female    74.2
male      18.9

--- Survival Rate by Passenger Class ---
1    63.0
2    47.3
3    24.2
```

## Technologies Used

- Python
- Pandas
- NumPy
- Git

## Learning Goals

This project demonstrates:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Git & GitHub Workflow
- Modular Python Project Structure

## Future Improvements

- Add machine learning models
- Train survival prediction model
- Generate visualizations
- Add automated tests
- Create a web dashboard

## Author

Yash Patel