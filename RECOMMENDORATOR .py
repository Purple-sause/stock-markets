# made an excl file with the data from nse website and sorted it 52wk high vs current price
import pandas as pd

# Load the Excel file as DataFrame
df1 = pd.read_csv(r"./output.csv")
df2 = pd.read_csv(r"./EPS.csv")
df1.drop(columns=["priority","identifier","date365dAgo","date30dAgo"],inplace=True)

FINALDF = pd.merge(df1, df2[['symbol','eps', 'Igroup Name']], on='symbol', how='left')
FINALDF["PE Ratio"] = FINALDF["lastPrice"]/FINALDF["eps"]

FINALDF.dropna(subset=['PE Ratio'], inplace=True)
FINALDF = FINALDF[FINALDF['PE Ratio'] >= 0]

industrylist=[]
for i, industry in enumerate(FINALDF['industry'].unique(), 1):
    industrylist.append(industry)
print(industrylist)
Full_stockdata = pd.DataFrame()
emptyline=pd.DataFrame([{}])
for industry in industrylist:
    selected_df = FINALDF[FINALDF['Igroup Name'] == industry]
    # Sort the filtered DataFrame by price in ascending order
    selected_df_sorted = selected_df.sort_values(by='PE Ratio')
    # Select the first three rows with the lowest prices

    lowest_prices = selected_df_sorted.head(5)
    
    Full_stockdata  =pd.concat([Full_stockdata, lowest_prices,emptyline] ,ignore_index=True)
    # Full_stockdata  =pd.concat([Full_stockdata, emptyline],  ignore_index=True)

Full_stockdata.to_clipboard()

