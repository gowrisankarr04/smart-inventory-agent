import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split    
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import datetime

# Load data
df = pd.read_csv('data/product_data.csv')

# Convert dates
df['expiry_date'] = pd.to_datetime(df['expiry_date'])
df['manufacturing_date'] = pd.to_datetime(df['manufacturing_date'])

# Calculate days until expiry
today = pd.Timestamp(datetime.date.today())
df['days_until_expiry'] = (df['expiry_date'] - today).dt.days

# Calculate months of stock remaining
df['months_of_stock'] = df['stock_quantity'] / df['units_sold_per_month']

print(df[['product_name', 'days_until_expiry', 'months_of_stock']].head())

# Create target label - 1 = at risk, 0 = safe
df['expiry_risk'] = (
(df['days_until_expiry'] <0) |
(df['months_of_stock'] > df['days_until_expiry'] / 30)
).astype(int)

print("/n=== Risk Distribution ===")
print(df['expiry_risk'].value_counts())



features = ['days_until_expiry', 'months_of_stock', 'stock_quantity', 'units_sold_per_month', 'price_per_unit']

x = df[features]
y = df['expiry_risk']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(f"/nTraning samples: {len(x_train)}")
print(f"Testing samples: {len(x_test)}")

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))


#save the model 
import pickle
with open("models/expiry_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model saved successfully!")

