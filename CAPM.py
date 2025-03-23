import yfinance as yf
# Monetary Policy Rates automate from RBI
monetary_policy_rates = {
    "Policy Repo Rate": 6.25,
    "Standing Deposit Facility Rate": 6.00,
    "Marginal Standing Facility Rate": 6.50,
    "Bank Rate": 6.50,
    "Fixed Reverse Repo Rate": 3.35,
    "CRR": 4.00,
    "SLR": 18.00
}

# Forex Exchange Rates
forex_rates = {
    "INR / 1 USD": 87.4006,
    "INR / 1 GBP": 109.9762,
    "INR / 1 EUR": 90.7807,
    "INR / 100 JPY": 58.3000
}

# Banking Rates
banking_rates = {
    "Base Rate": "9.10% - 10.40%",
    "MCLR (Overnight)": "8.15% - 8.45%",
    "Savings Deposit Rate": "2.70% - 3.00%",
    "Term Deposit Rate > 1 Year": None,  # No value provided
    "Call Rates": "5.15% - 6.40% "
}

# Market Data
market_data = {
    "Government Securities": {
        "7.38% GS 2027": 6.5686,
        "7.04% GS 2029": 6.6276,
        "6.79% GS 2034": 6.7092,
        "6.92% GS 2039": 6.8802,
        "7.09% GS 2054": 7.1133
    },
    "T-bills": {
        "91 day": 6.4490,
        "182 day": 6.5989,
        "364 day": 6.5409
    },
    "Stock Market": {
        "S&P BSE Sensex": 74612.43,
        "Nifty 50": 22545.05
    },
    "Date": "February 27, 2025"
}

GetFacebookInformation = yf.Ticker("META")
beta = GetFacebookInformation.info["beta"]
print(beta)

#yfinance blocked me?

Ri= int(monetary_policy_rates["Bank Rate"])+ int(beta) * (10.6-int(monetary_policy_rates["Bank Rate"]))
print(Ri)