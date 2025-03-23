import json
from collections import OrderedDict
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from io import BytesIO

file_path = r"./financial_results.txt"
with open(file_path, "r") as file:
    content = file.read()
try:
    json_data = json.loads(content,object_pairs_hook=OrderedDict)
    print("json_data sucessfully loaded")
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)

# Step 2: Convert the JSON data into a Pandas DataFrame
df = pd.DataFrame(json_data)
print(df)
# Step 3: Query the data by symbol
# Example query: Get all records for symbol "UDS"
symbol_query = "UDS"
result = df[df["symbol"] == symbol_query]

# Display the result
home_url=result["xbrl"].iloc[0]
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0.1 Safari/605.1.15a",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Content-Type":"text/html; charset=utf-8"

}

response=requests.get(home_url,headers=headers)

if response.status_code == 200:
    print("Response Received:")
    print(response.text)  # Print the response content
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

   # Example if response is coming from an API
bytes_response = BytesIO(response.content)
parsed_xml = ET.parse(bytes_response)
print(type(parsed_xml))

root = parsed_xml.getroot()
columns = ["name", "description", "id", "context_ref", "unit_ref", "decimals","value"]
    
# Create an empty DataFrame
df_statement = pd.DataFrame(columns=columns)
data = []
for child in root:
        row = {
            "name": child.tag,
            "description": child.attrib.get("description", ""),
            "id": child.attrib.get("id", ""),
            "context_ref": child.attrib.get("contextRef", ""),
            "unit_ref": child.attrib.get("unitRef", ""),
            "decimals": child.attrib.get("decimals", ""),
            "value": child.text
            }
        data.append(row)
    
# Convert the list to a DataFrame
df_statement = pd.DataFrame(data, columns=columns)
# for loop for text editing, removing unwanted text
for index, row in df_statement.iterrows():
    id_value = row['id']
    
    if id_value =="":
        # Remove 56 characters from the 'name' column for this row
        df_statement.at[index, 'name'] = row['name'][56:]


df_statement_fs = df_statement[(df_statement['context_ref'] == "OneD") & (df_statement['unit_ref'] == "INR")]
df_statement_fs.to_clipboard(index=False)


