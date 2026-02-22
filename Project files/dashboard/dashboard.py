import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Empowering India: Union Budget Analysis")

data = pd.read_csv("../data/union_budget.csv")

sector = st.selectbox("Select Sector", data["Sector"].unique())
filtered = data[data["Sector"] == sector]

plt.figure()
plt.plot(filtered["Year"], filtered["Allocation_in_Crores"])
plt.xlabel("Year")
plt.ylabel("Allocation (₹ Crores)")
plt.title(f"{sector} Budget Trend")

st.pyplot(plt)
