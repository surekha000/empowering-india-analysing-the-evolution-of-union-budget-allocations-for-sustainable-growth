import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/union_budget.csv")

plt.figure()
for sector in data['Sector'].unique():
    sector_data = data[data['Sector'] == sector]
    plt.plot(sector_data['Year'], sector_data['Allocation_in_Crores'], label=sector)

plt.xlabel("Year")
plt.ylabel("Allocation (₹ Crores)")
plt.title("Union Budget Allocation Trends")
plt.legend()
plt.show()
