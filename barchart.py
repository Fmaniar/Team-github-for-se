import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/train.csv')
new_df = df.groupby(['Ship Mode']).sum().reset_index()
test = df["Ship Mode"].value_counts(normalize=True)

data = [go.Bar(x=new_df['Ship Mode'], y=[test["First Class"],test["Same Day"],test["Second Class"],test["Standard Class"]])]

layout = go.Layout(title='Shipping mode pecentage splits', xaxis_title="Shipping modes",
                   yaxis_title="Percentage split")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
