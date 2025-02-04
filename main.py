import pandas as pd
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the full path for saving
save_path = os.path.join(script_dir, "sample_data.xlsx")

# Read the Stata file in chunks
reader = pd.read_stata("./serrano_2024_Stata/serrano_2024_Stata/serrano.dta", iterator=True)

# Read the first 100 rows
df = reader.read(100)

# Export to Excel in the same directory as the script
df.to_excel(save_path, index=False)

print(f"Saved to {save_path}")
print(df.head())
