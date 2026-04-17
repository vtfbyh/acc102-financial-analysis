import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Global font configuration for consistent chart display
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

# Page Setup & Introduction
st.set_page_config(page_title="ACC102 Financial Analysis Tool", layout="wide")
st.title("ACC102 Financial Analysis Tool")
st.markdown("Financial Performance Analysis for Home Appliance Companies (2020-2024)")
st.markdown("This tool analyzes ROE and Profit Margin for Midea, Gree, and Haier.")

# Load Raw Data (Consistent with Notebook)
data = {
    "Company": ["Midea", "Gree", "Haier"] * 5,
    "Year": [2020, 2020, 2020,
             2021, 2021, 2021,
             2022, 2022, 2022,
             2023, 2023, 2023,
             2024, 2024, 2024],
    "ROE": [22, 23, 18, 21, 22, 17, 20, 22, 16, 21, 23, 17, 22, 24, 18],
    "ProfitMargin": [8, 15, 5, 7, 14, 5, 8, 16, 6, 9, 17, 6, 10, 18, 6]
}
df = pd.DataFrame(data)

# Data Preview & Cleaning Check
st.subheader("Data Preview & Cleaning")
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Data Preview (First 5 Rows):**")
    st.dataframe(df.head())
with col2:
    st.markdown("**Missing Value Check:**")
    st.write(df.isna().sum())

# Calculate Average ROE by Company
st.subheader("Average ROE by Company (2020-2024)")
avg_roe = df.groupby('Company')['ROE'].mean().round(2)
st.dataframe(avg_roe)

# Plot ROE Trend Comparison Chart
st.subheader("ROE Trend Comparison (2020-2024)")
df_pivot = df.pivot(index='Year', columns='Company', values='ROE')
fig, ax = plt.subplots(figsize=(10,5))
df_pivot.plot(ax=ax, marker='o', linewidth=2)
ax.set_title('ROE Comparison of Home Appliance Companies (2020-2024)', fontsize=14)
ax.set_ylabel('ROE (%)', fontsize=12)
ax.grid(alpha=0.3)
st.pyplot(fig)

# Business Insights & Conclusion
st.subheader("Key Business Insights & Conclusion")
insights = """
**1. Profitability Performance:**
- Gree Electric maintains the highest average ROE (22.8%) with strong stability, demonstrating the strongest profitability among the three companies.
- Midea Group shows steady growth and consistent performance, with an average ROE of 21.2%.
- Haier has a relatively lower average ROE (17.2%) but remains stable, indicating solid operational fundamentals.

**2. Trend Analysis (from the chart):**
- Gree's ROE saw a slight dip in 2021-2022 but rebounded strongly to 24% in 2024, showing strong resilience and recovery capability.
- Midea's ROE remained stable throughout the period, with a steady upward trend after 2022.
- Haier's ROE hit a low in 2022 but has been recovering consistently since then.

**3. Investment Recommendation:**
- For investors prioritizing stable high returns, Gree is the preferred choice.
- For those seeking balanced growth and risk, Midea offers a reliable option.
- Haier is suitable for investors focused on long-term recovery potential.
"""
st.markdown(insights)