import pandas as pd
import sys
packages_path = '/Users/harryvincent/Desktop/python/Stock market/packages'  # Adjust this if your folder is located elsewhere
sys.path.append(packages_path)
import yfinance as yf

# df = pd.read_csv(r'./output.csv', header=0)

# # Define a function to fetch EPS data
# def get_eps(ticker):
#     try:
#         ticker_ns = f"{ticker}.NS"
#         print (ticker_ns)
#         stock = yf.Ticker(ticker_ns)
#         # Fetch EPS (trailing twelve months)
#         eps = stock.info.get('trailingEps', 'N/A')  # Default to 'N/A' if EPS is not available
#         return eps
#     except Exception as e:
#         print(f"Error fetching data for {ticker}: {e}")
#         return 'Error'


# results = []
# for ticker in  df["symbol"]:
#      eps = get_eps(ticker)
#      results.append({'symbol': ticker, 'eps': eps})

# # Convert results to a DataFrame
# df_eps = pd.DataFrame(results)
# # Step 3: Save the DataFrame to a CSV file
# df_eps.to_csv(r"./EPS.csv", index=False)
# print("EPS data has been saved to eps.csv")

#Segment for appending dataframes
file1=r"./EPS.csv"
file2=r"./BSE_Industrydata.csv"
# Function to read CSV with error handling
def read_csv_with_error_handling(file_path):
    try:
        # Attempt to read the CSV file
        df = pd.read_csv(file_path,header=0)
        return df
    except pd.errors.ParserError as e:
        print(f"Error reading {file_path}: {e}")
        return None
    
# Load the CSV files into DataFrames with error handling
df1 = read_csv_with_error_handling(file1)
df2 = read_csv_with_error_handling(file2)

# Proceed only if both DataFrames are loaded successfully
if df1 is not None and df2 is not None:
    # Merge the DataFrames on the 'symbol' column
    updated_df = pd.merge(df1, df2[['symbol', 'Igroup Name']], on='symbol', how='left')

    # Save the updated DataFrame back to the original file1.csv
    updated_df.to_csv(file1, index=False)

    print("file1.csv has been updated with data from file2.csv.")
else:
    print("One or both CSV files could not be read.")