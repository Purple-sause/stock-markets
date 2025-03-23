import os
import requests

url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20TOTAL%20MARKET"
output_file = "web_page.txt"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0.1 Safari/605.1.15a",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Content-Type":"text/html; charset=utf-8"

}

# Create a session object
session = requests.Session()

# Make an initial request to the home page to get any required cookies
home_url = "https://www.nseindia.com/market-data/live-equity-market"
session.get(home_url, headers=headers)

# Now make the request to the API endpoint
response = session.get(url, headers=headers)
status_code = response.status_code
print(status_code)

if status_code == 200:  # Check if the request was successful
    page_source = response.text
    output_path = os.path.join(R"./", output_file)  # Save in the current working directory
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(page_source)
    print(f"Page source saved to {output_file}")
else:
    print("Failed to retrieve the page source.")

file_path = r"./web_page.txt"
with open(file_path, "r") as file:
    content = file.read()
print(content[1:200])