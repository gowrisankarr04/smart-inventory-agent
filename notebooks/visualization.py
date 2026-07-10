import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import datetime

df = pd.read_csv('data/product_data.csv')

df['manufacturing_date'] = pd.to_datetime(df['manufacturing_date'])
df['expiry_date'] = pd.to_datetime(df['expiry_date'])

today = pd.Timestamp(datetime.date.today())
df['days_until_expiry'] = (df['expiry_date'] - today).dt.days

sns.set(style='darkgrid')

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='category', hue = 'category',palette='viridis', legend=False)
plt.title('Number of Products per Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('data/category.png')
plt.close()
print("chart 1 saved")

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='warehouse', y='stock_quantity', hue='warehouse', palette='coolwarm', legend=False)
plt.title('Average Stock Quantity Per Warehouse')
plt.xlabel('warehouse')
plt.ylabel('average stock quantity')
plt.tight_layout()
plt.savefig('data/charts/warehouse_stock.png')
plt.close()
print("chart 2 saved")


# Chart 3 - Expiry Risk
expiry_data = {
    'Status': ['Already Expired', 'Expiring in 30 days', 'Expiring in 90 days', 'Safe'],
    'Count': [
        (df['days_until_expiry'] < 0).sum(),
        (df['days_until_expiry'].between(0, 30)).sum(),
        (df['days_until_expiry'].between(31, 90)).sum(),
        (df['days_until_expiry'] > 90).sum()
    ]
}
expiry_df = pd.DataFrame(expiry_data)
plt.figure(figsize=(8, 5))
sns.barplot(data=expiry_df, x='Status', y='Count',
            hue='Status', palette='RdYlGn', legend=False)
plt.title('Product Expiry Risk Analysis')
plt.xlabel('Expiry Status')
plt.ylabel('Number of Products')
plt.tight_layout()
plt.savefig('data/charts/expiry_risk.png')
plt.close()
print("Chart 3 saved!")