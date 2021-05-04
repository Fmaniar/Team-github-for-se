import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
df = pd.read_csv('../Datasets/train.csv')

fig = px.box(df, x="Sales", y="Ship Mode")
fig.show()