import numpy as np 
import pandas as pd 

df = pd.read_csv('data/product_data.csv')
print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df['category'].value_counts())
print(df['warehouse'].value_counts())

# convert date columns to datetime format
df['manufacturing_date'] = pd.to_datetime(df['manufacturing_date'])
df['expiry_date'] = pd.to_datetime(df['expiry_date'])

# calculate days untill expiry
import datetime
today = pd.Timestamp(datetime.date.today())
df['days_untill_expiry'] = (df['expiry_date'] - today).dt.days

print(f"Already expired products: {(df['days_untill_expiry'] < 0).sum()}")
print(f"Products expiring within 30 days: {(df['days_untill_expiry'] <= 30).sum()}")
print(f"Products expiring within 90 days: {(df['days_untill_expiry'] <= 90).sum()}")