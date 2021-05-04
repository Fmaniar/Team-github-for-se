import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/train.csv')
data = [go.Heatmap(x=df["Ship Mode"],
                   y = df["Segment"],
                   z = df["Sales"],
                   colorscale = "Jet")]
layout = go.Layout(title='ship mode to segment to sales price', xaxis_title="ship mode",
                   yaxis_title="segment")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmap.html')