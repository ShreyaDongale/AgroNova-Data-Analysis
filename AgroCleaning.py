import pandas as pd

# Read Excel
fact_sales = pd.read_excel("AgroNovA.xlsx", sheet_name="Fact_Sales")
calendar = pd.read_excel("AgroNovA.xlsx", sheet_name="Dim_Calendar")
country = pd.read_excel("AgroNovA.xlsx", sheet_name="Dim_Country")
customer = pd.read_excel("AgroNovA.xlsx", sheet_name="Dim_Customer")
product = pd.read_excel("AgroNovA.xlsx", sheet_name="Dim_Product")
salesperson = pd.read_excel("AgroNovA.xlsx", sheet_name="Dim_Salesperson")


# Missing Values
print("Fact Sales Missing Values:")
print(fact_sales.isnull().sum())

print("Calendar Missing Values:")
print(calendar.isnull().sum())

print("Country Missing Values:")
print(country.isnull().sum())

print("Customer Missing Values:")
print(customer.isnull().sum())

print("Product Missing Values:")
print(product.isnull().sum())

print("Salesperson Missing Values:")
print(salesperson.isnull().sum())


# Duplicates
print("Fact Sales Duplicates:", fact_sales.duplicated().sum())
print("Calendar Duplicates:", calendar.duplicated().sum())
print("Country Duplicates:", country.duplicated().sum())
print("Customer Duplicates:", customer.duplicated().sum())
print("Product Duplicates:", product.duplicated().sum())
print("Salesperson Duplicates:", salesperson.duplicated().sum())


# Gross Sales
fact_sales["GrossSales_USD"] = fact_sales["Quantity"] * fact_sales["UnitPrice_USD"]


# Create CSV files
fact_sales.to_csv("Fact_Sales_Clean.csv", index=False)
calendar.to_csv("Dim_Calendar_Clean.csv", index=False)
country.to_csv("Dim_Country_Clean.csv", index=False)
customer.to_csv("Dim_Customer_Clean.csv", index=False)
product.to_csv("Dim_Product_Clean.csv", index=False)
salesperson.to_csv("Dim_Salesperson_Clean.csv", index=False)

print("CSV files created successfully!")