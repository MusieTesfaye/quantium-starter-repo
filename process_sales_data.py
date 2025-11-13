import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

combined = pd.concat([pd.read_csv(file) for file in files], ignore_index = True)


combined["product"] = combined["product"].str.strip().str.lower()
pink_morsel = combined[combined["product"] == "pink morsel"].copy()


pink_morsel["price"] = pink_morsel["price"].str.replace("$", "", regex = False).astype(float)


pink_morsel["sales"] = pink_morsel["price"] * pink_morsel["quantity"]


output = pink_morsel[["sales", "date", "region"]]


output.to_csv("data/processed_sales.csv", index=False)