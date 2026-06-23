import pandas as pd 
import numpy as np
from datetime import datetime, timedelta
import random 
import os

np.random.seed(42)
random.seed(42)

num_products = 500
categories = ['Food', 'Medicine', 'Cosmetics', 'Beverages']
warehouses = ['Warehouse A', 'Warehouse B', 'Warehouse C', 'Warehouse D']

def generate_product_name(category):
    names={
        'Food': ['rice', 'wheat', 'sugar', 'salt', 'oil', 'biscuits', 'noodles'],
        'Medicine': ['paracetamol', 'vitamin c', 'antibiotics', 'cough syrup', 'bandage'],
        'Cosmetics': ['shampoo', 'moisturizer', 'sunscreen', 'lip balm', 'facewash'],
        'Beverages': ['water', 'juice', 'soda', 'tea', 'coffee', 'energy drink'],
        'Electronics': ['battery', 'charger', 'earphones', 'usb cable', 'adapter']


    }
    return random.choice(names[category]) + f"_{random.randint(100, 999)}"

# generate dates --

today = datetime.today()
data = []
for i in range(num_products):
    category = random.choice(categories)
    mfg_date = today - timedelta(days=random.randint(30, 365))
    exp_date = mfg_date + timedelta(days=random.randint(60,730))

    data.append({
        'product_id': f'prd_{1000 + i}',
        'product_name': generate_product_name(category),
        'category': category,
        'warehouse': random.choice(warehouses),
        'manufacturing_date': mfg_date.strftime('%Y-%m-%d'),
        'expiry_date': exp_date.strftime('%Y-%m-%d'),
        'stock_quantity': random.randint(10, 1000),
        'units_sold_per_month': random.randint(5,300),
        'price_per_unit': round(random.uniform(10, 5000), 2)
    })

    # create dataframe 

df = pd.DataFrame(data)

#save to csv
os.makedirs('data', exist_ok=True)
df.to_csv('data/product_data.csv', index=False)
print(f"Dataset created succesfully! shape: {df.shape}")
print(df.head())