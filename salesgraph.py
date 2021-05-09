import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px
# Load CSV file from Datasets folder
def shipHeatMap():
    df = pd.read_csv('train.csv')
    data = [go.Heatmap(x=df["Ship Mode"],
                   y = df["Segment"],
                   z = df["Sales"],
                   colorscale = "Jet")]
    layout = go.Layout(title='ship mode to segment to sales price', xaxis_title="ship mode",
                   yaxis_title="segment")
    fig = go.Figure(data=data, layout=layout)
    return fig
def shipBarChar():
    df = pd.read_csv('train.csv')
    new_df = df.groupby(['Ship Mode']).sum().reset_index()
    test = df["Ship Mode"].value_counts(normalize=True)

    data = [go.Bar(x=new_df['Ship Mode'], y=[test["First Class"],test["Same Day"],test["Second Class"],test["Standard Class"]])]

    layout = go.Layout(title='Shipping mode pecentage splits', xaxis_title="Shipping modes",
                   yaxis_title="Percentage split")

    fig = go.Figure(data=data, layout=layout)
    return fig
def shipbarg():
    df = pd.read_csv('train.csv')

    fig = px.box(df, x="Sales", y="Ship Mode")
    return fig