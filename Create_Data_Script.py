import numpy as np 
import pandas as pd

np.random.seed(42)

iter_df = pd.DataFrame({"OrderDate": pd.date_range(start="2025-01-01", end="2025-08-31").tolist()})
df = pd.DataFrame(columns=["OrderNumber", "OrderDate", "Amount", "ShippingCost", "COGS", "Return", "ProductLine"])

for i in range(len(iter_df)):
    orderDate = pd.to_datetime(iter_df.OrderDate.iloc[i])

    join_df = pd.DataFrame()
    cnt_orders = np.random.randint(low=0, high=20)

    returns = [0,0,0,0,0,0,0,0,0,1] # 1 in 10 chance of return
    products = ["Clothing", "Beauty", "Electronics", "Home"]
    
    # for order in range(cnt_orders):
    join_df["OrderNumber"] = np.random.randint(low=10000, high=99999, size=cnt_orders)
    join_df["OrderDate"] = [orderDate for i in range(cnt_orders)]
    join_df["Amount"] = np.round(np.random.uniform(low=5, high=100, size=cnt_orders), 2)
    join_df["ShippingCost"] = np.round(join_df["Amount"] * np.random.uniform(0.01, 0.10, cnt_orders), 2)
    join_df["COGS"] = np.round(join_df["Amount"] * np.random.uniform(0.15, 0.30, cnt_orders), 2)
    join_df["Return"] = np.random.choice(returns, size=cnt_orders)
    join_df["ProductLine"] = np.random.choice(products, size=cnt_orders)

    df = pd.concat([df, join_df])

df = df.reset_index(drop=True)
df.to_excel("SalesData.xlsx")