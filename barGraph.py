import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
print(df.head())

figure=px.bar(df,x="Country",y="InternetUsers",color="Country")
figure.show()