import pandas as pd
import numpy as np
import statsmodels.api as sm
import requests

# Load the Livingston Survey data
df = pd.read_excel("D://sysbackup//Desktop//full_stack_project//my_replication_project/medians.xlsx")

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Filter dataset for the required period (June 1992 - December 2022)
df_filtered = df[(df["Date"] >= "1992-06-01") & (df["Date"] <= "2022-12-01")].copy()

# Compute the 6-month spot rate (log annualized return)
df_filtered["spot_rate"] = (1/6) * np.log(df_filtered["RGDPX_6M"] / df_filtered["RGDPX_BP"])

# Compute the 6-month, 6-month forward rate
df_filtered["forward_rate"] = (1/6) * np.log(df_filtered["RGDPX_12M"] / df_filtered["RGDPX_6M"])

# Compute forecast errors using the next survey's realized spot rate
df_filtered["realized_spot_rate"] = df_filtered["spot_rate"].shift(-1)
df_filtered["forecast_error"] = df_filtered["realized_spot_rate"] - df_filtered["forward_rate"]

# Drop rows with missing forecast errors
df_filtered = df_filtered.dropna(subset=["forecast_error"])

# Step 1: Download Shiller's CAPE Data
cape_url = "https://www.econ.yale.edu/~shiller/data/ie_data.xls"
cape_file = "/mnt/data/shiller_cape.xls"

# Download the file
response = requests.get(cape_url)
with open(cape_file, "wb") as f:
    f.write(response.content)

# Load the Shiller CAPE dataset
cape_df = pd.read_excel(cape_file, sheet_name="Data", skiprows=7)
# Clean and rename columns
cape_df = cape_df.iloc[:, [0, 10]]  # Select Date and CAPE Ratio
cape_df.columns = ["Date", "CAPE"]
cape_df = cape_df.dropna()  # Remove missing values

# Convert "Date" to datetime (use mid-month dates for consistency)
cape_df["Date"] = pd.to_datetime(cape_df["Date"].astype(str) + "-15", format="%Y-%m-%d")

# Compute Inverse CAPE (Earnings Yield)
cape_df["inv_CAPE"] = 1 / cape_df["CAPE"]

# Merge with Livingston Survey Data
df_merged = pd.merge(df_filtered, cape_df, on="Date", how="left")

# Define regression function
def run_regression(y, X):
    X = sm.add_constant(X)  # Add intercept
    model = sm.OLS(y, X).fit()
    return model.params, model.rsquared

# Panel A: Predictability in Spot Rates
params_A, r2_A = run_regression(df_merged["spot_rate"], df_merged["forward_rate"])

# Panel B: Predictability in Forecast Errors
params_B, r2_B = run_regression(df_merged["forecast_error"], df_merged["forward_rate"])

# Panel C: Cyclicality using inverse CAPE (actual data)
rho_f_CAPE = df_merged["forward_rate"].corr(df_merged["inv_CAPE"])
rho_err_CAPE = df_merged["forecast_error"].corr(df_merged["inv_CAPE"])

# Create the Updated Table 1
table1_updated = pd.DataFrame({
    "Panel": ["Panel A: Predictability in Spot Rates", "Panel B: Predictability in Forecast Errors", "Panel C: Cyclicality"],
    "β₁ (Livingston Survey)": [params_A[1], params_B[1], rho_f_CAPE],
    "R² (Livingston Survey)": [r2_A, r2_B, rho_err_CAPE]
})
# Display the Updated Table 1
import ace_tools as tools
tools.display_dataframe_to_user(name="Updated Table 1 - Livingston Survey with CAPE", dataframe=table1_updated)
