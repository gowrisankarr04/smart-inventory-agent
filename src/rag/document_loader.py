import json
import os
import pandas as pd

df = pd.read_csv('data/product_data.csv')


# Convert each product row into a text document
# This is what RAG will search through

document = []

for _, row in df.iterrows():
    doc = f"""
    product name: {row['product_name']}
    product id: {row['product_id']}
    category: {row['category']}
    warehouse: {row['warehouse']}
    stock quantity: {row['stock_quantity']} units
    manufacturing date: {row['manufacturing_date']}
    expiry date: {row['expiry_date']}
    units sold per month: {row['units_sold_per_month']}
    price per unit: {row['price_per_unit']}

    """
    document.append(doc)


print(f"total documents created: {len(document)}")
print("/n=== sample document ===")
print(document[0])


#save documents to json file
os.makedirs('rag', exist_ok=True)
with open('rag/documents.json', 'w') as f:
    json.dump(document, f)

print("/n === documents saved to rag/documents.json ===")