import pandas as pd

df = pd.read_stata("./stata_202408/bokslut_hhs_avi202408.dta")

print(df.head())
