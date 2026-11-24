
# Cognifyz Internship
# Level 3 - Task 2
# Data Visualization Tool

import pandas as pd
import plotly.express as px
from pathlib import Path

# Read dataset
file_path = Path(__file__).with_name("sales_data.csv")
data = pd.read_csv(file_path)

# Display dataset
print("===== SALES DATA =====")
print(data)

# Create bar chart
fig = px.bar(
    data,
    x="Month",
    y="Sales",
    title="Monthly Sales Report",
    labels={
        "Month": "Month",
        "Sales": "Sales Amount"
    }
)

# Display interactive chart
fig.show()
