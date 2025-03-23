import json
from collections import OrderedDict
import csv
import pandas as pd
import ast

# Function to preprocess and convert string to OrderedDict
def preprocess_and_parse(meta_str):
    # Replace OrderedDict with dict
    meta_str = meta_str.replace("OrderedDict", "dict")
    # Replace single quotes with double quotes
    meta_str = meta_str.replace("'", '"')
    # Replace boolean literals
    meta_str = meta_str.replace("True", "true").replace("False", "false")
    try:
        # Safely evaluate the string as a dictionary
        parsed_dict = eval(meta_str, {"dict": dict, "true": True, "false": False})
        if isinstance(parsed_dict, dict):
            return OrderedDict(parsed_dict)  # Ensure it's an OrderedDict
        else:
            return {}
    except (ValueError, SyntaxError, NameError) as e:
        print(f"Error parsing meta: {e}")
        return {}

file_path = r"./web_page.txt"
with open(file_path, "r") as file:
    content = file.read()
try:
    json_data = json.loads(content,object_pairs_hook=OrderedDict)
    print("json_data sucessfully loaded")
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)

# Remove the first object in the "data" list
json_data["data"].pop(0)

# Define CSV file path
csv_file_path1 = r"./output.csv"

# Extract the keys from the first data object to use as CSV header
csv_header = json_data["data"][0].keys()

# Write the data to a CSV file
with open(csv_file_path1, "w", newline="") as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=csv_header)
    csvwriter.writeheader()
    csvwriter.writerows(json_data["data"])

print("CSV file has been created.")

def dataframe_maker(csv_file_path):
    df = pd.read_csv(csv_file_path, header=0)
    return df

df=dataframe_maker(csv_file_path1)
m=['chart30dPath','chartTodayPath','chart365dPath']
df.drop(columns=m,inplace=True)

# Apply conversion
df['meta'] = df['meta'].apply(preprocess_and_parse)
# Extract companyName and industry into separate columns
df['companyName'] = df['meta'].apply(lambda x: x.get('companyName', 'zero') if isinstance(x, OrderedDict) else 'zero')
df['industry'] = df['meta'].apply(lambda x: x.get('industry', 'zero') if isinstance(x, OrderedDict) else 'zero')
# Drop the original 'meta' column
df = df.drop(columns=['meta'])

df['spring'] = (df['yearHigh'] - df['lastPrice'])/(df['lastPrice']) # yearly rise max possible
df['range'] = (df['dayHigh'] - df['dayLow']) # day trend
df['daytrend'] = (df['open'] - df['lastPrice']) #till now how stock moves

for col in df.columns:
    print(col)
df=df.sort_values(by='spring',ascending=False)#to get stocks that are badass even loss making
df.to_csv(csv_file_path1, index=False)