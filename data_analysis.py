import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulating Dataset (Tourism Data)
data = {
    'Year':,
    'Country': ['India', 'India', 'India', 'India', 'India'],
    'Tourists_Count':,
    'Avg_Spend_JPY':,
    'Primary_Purpose': ['Business', 'Business', 'Leisure', 'Leisure', 'Leisure']
}

df = pd.DataFrame(data)

# 2. Data Transformation (Calculating Total Revenue in JPY)
df['Total_Revenue_JPY'] = df['Tourists_Count'] * df['Avg_Spend_JPY']

# Saving the cleaned data to CSV for SQL analysis
df.to_csv('cleaned_japan_tourism.csv', index=False)
print("Data cleaned and saved successfully!")

# 3. Data Visualization
plt.figure(figsize=(10, 5))
plt.bar(df['Year'].astype(str), df['Tourists_Count'], color='dodgerblue', edgecolor='black')
plt.title('Growth of Indian Tourists in Japan (2021-2025)')
plt.xlabel('Year')
plt.ylabel('Number of Tourists')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Saving the chart image for GitHub README
plt.savefig('tourist_growth_chart.png')
print("Visualization saved successfully!")
