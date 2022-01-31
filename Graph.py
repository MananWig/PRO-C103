import pandas as pd
import plotly.express as px

dataframe = pd.read_csv("data.csv")
graph = px.scatter(dataframe, x="date", y="cases",
                   color="country",
                   size_max=60)
graph.show()
