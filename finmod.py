# -*- coding: utf-8 -*-
"""finmod.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nf3jUscP5UBueUtxOp76Bsi-ApnGUHrN
"""

import streamlit as st

# Streamlit app title
st.title("Financial Model App")

# Input for the income statement
st.header("Income Statement")
revenue = st.number_input("Revenue (Year 1)", min_value=0.0, format="%.2f")
cogs_manufacturing = st.number_input("COGS - Manufacturing (per order)", min_value=0.0, format="%.2f")
cogs_order_fulfillment = st.number_input("COGS - Order Fulfillment (per order)", min_value=0.0, format="%.2f")

# Assumptions
st.header("Assumptions")
num_orders = st.number_input("Number of Orders", min_value=0)
order_growth_rate = st.number_input("Order Growth Rate (%)", min_value=0.0, format="%.2f")
average_order_value = st.number_input("Average Order Value ($)", min_value=0.0, format="%.2f")

# Operating Expenses
st.header("Operating Expenses")
warehouse_rent = st.number_input("Warehouse Rent ($)", min_value=0.0, format="%.2f")
salaries_payroll = st.number_input("Salaries & Payroll ($)", min_value=0.0, format="%.2f")
marketing_expenses = st.number_input("Marketing Expenses ($)", min_value=0.0, format="%.2f")
other_expenses = st.number_input("Other Expenses ($)", min_value=0.0, format="%.2f")

# Corporate tax rate
tax_rate = st.number_input("Corporate Tax Rate (%)", min_value=0.0, max_value=100.0, format="%.2f") / 100

# Calculations
# Calculate Revenue for Year 1
revenue = num_orders * average_order_value
st.write(f"Total Revenue (Year 1): ${revenue:.2f}")

# Calculate COGS
total_cogs = num_orders * (cogs_manufacturing + cogs_order_fulfillment)
st.write(f"Total COGS (Year 1): ${total_cogs:.2f}")

# Calculate Gross Profit
gross_profit = revenue - total_cogs
gross_profit_margin = (gross_profit / revenue) * 100 if revenue > 0 else 0
st.write(f"Gross Profit (Year 1): ${gross_profit:.2f}")
st.write(f"Gross Profit Margin: {gross_profit_margin:.2f}%")

# Operating Expenses
total_operating_expenses = warehouse_rent + salaries_payroll + marketing_expenses + other_expenses
st.write(f"Total Operating Expenses (Year 1): ${total_operating_expenses:.2f}")

# Calculate Operating Profit
operating_profit = gross_profit - total_operating_expenses
operating_profit_margin = (operating_profit / revenue) * 100 if revenue > 0 else 0
st.write(f"Operating Profit (Year 1): ${operating_profit:.2f}")
st.write(f"Operating Profit Margin: {operating_profit_margin:.2f}%")

# Calculate Tax
tax = operating_profit * tax_rate if operating_profit > 0 else 0
st.write(f"Tax (Year 1): ${tax:.2f}")

# Calculate Profit or Loss
profit_loss = operating_profit - tax
st.write(f"Profit / (Loss) (Year 1): ${profit_loss:.2f}")