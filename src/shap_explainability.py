import pandas as pd
import shap
import matplotlib.pyplot as plt 
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import datetime

df = pd.read_csv('data/product_data.csv')

df['expiry_date'] = pd.to_datetime(df['expiry_date'])
df['manufacturing_date'] = pd.to_datetime(df['manufacturing_date'])

today = pd.Timestamp(datetime.date.today())
df['days_until_expiry'] = (df['expiry_date'] - today).dt.days
df['months_of_stock'] =(df['stock_quantity'] / df['units_sold_per_month'])

df['expiry_risk'] = (
    (df['days_until_expiry'] < 0) |
    (df['months_of_stock'] > df['days_until_expiry'] / 30)
).astype(int)

features = ['days_until_expiry', 'months_of_stock', 'stock_quantity', 'units_sold_per_month', 'price_per_unit']

x = df[features]
y = df['expiry_risk']

# load save model
with open("models/expiry_model.pkl", "rb") as f:
    model = pickle.load(f)

print("model loaded successfully!")

# Create SHAP explainer
explainer = shap.TreeExplainer(model)
shap_values =explainer.shap_values(x)

print("shap values calculated successfully!")

shap.summary_plot(shap_values[:,:,1], x, show = False)
plt.tight_layout()
plt.savefig('data/charts/shap_summmary.png')
plt.close()

print("shap summary plot saved successfully!")