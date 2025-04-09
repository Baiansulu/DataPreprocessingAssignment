# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load and combine all yearly datasets
years = ['2020', '2021', '2022', '2023', '2024']
dfs = []
for year in years:
    df = pd.read_csv(f"{year}.csv")
    df.columns = df.columns.str.strip().str.replace('\t', '', regex=True)
    df["Year"] = int(year)
    dfs.append(df)

df = pd.concat(dfs, ignore_index=True)

# Step 1: Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Step 2: Data Integration - already done above

# Step 3: Data Reduction
df = df[[
    'Country name', 'Year', 'Happiness score',
    'Economy (GDP per Capita)', 'Social support',
    'Healthy life expectancy', 'Freedom to make life choices',
    'Generosity', 'Perceptions of corruption'
]]

# Step 4: Data Transformation - Normalize numeric features
features = [
    'Economy (GDP per Capita)', 'Social support', 'Healthy life expectancy',
    'Freedom to make life choices', 'Generosity', 'Perceptions of corruption'
]

scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

# Step 5: Data Discretization - Convert Happiness Score to categories
df['Happiness Level'] = pd.cut(df['Happiness score'],
                               bins=[0, 4.5, 6.5, 10],
                               labels=['Low', 'Medium', 'High'])

# Bonus: Model to predict Happiness Score
X = df[features]
y = df['Happiness score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

# Visualization
plt.figure(figsize=(10, 6))
sns.histplot(df['Happiness score'], bins=20, kde=True)
plt.title("Happiness Score Distribution (2020–2024)")
plt.xlabel("Happiness Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("happiness_histogram.png")
plt.show()