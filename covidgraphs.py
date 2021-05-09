import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

file = 'Supplementary_materials_-_dataset.csv'
df = pd.read_csv(file)


df = df[df['age'] != 'trust_gov']

def eduBarChar():
    file = 'Supplementary_materials_-_dataset.csv'
    df = pd.read_csv(file)
    df = df[df['age'] != 'trust_gov'] 
    fig = go.Figure()
    fig = px.bar(df, x='education', y='trust_gov')
    fig.add_trace(go.Bar(name="1 = Primary School", x=["education", "trust_gov"], y=[1,2]))
    fig.add_trace(go.Bar(name="2 = High School", x=["education", "trust_gov"], y=[2,1]))
    fig.add_trace(go.Bar(name="3 = BA Degree", x=["education", "trust_gov"], y=[1,2]))
    fig.add_trace(go.Bar(name="4 = MA Degree", x=["education", "trust_gov"], y=[2,1]))
    fig.add_trace(go.Bar(name="5 = Specialist Degree", x=["education", "trust_gov"], y=[1,2]))
    fig.add_trace(go.Bar(name="6 = PhD Degree", x=["education", "trust_gov"], y=[2,1]))
    return fig
def eduComp():
    file = 'Supplementary_materials_-_dataset.csv'
    df = pd.read_csv(file)
    fig = px.box(df,
             x="education",
             y="compliance",
             points="all",
             color="education",
             notched=True,
             labels=dict(education="Education Level",
                         compliance="Compliance Level"),
             title="Education Level vs Level of Compliance in Survey Responders"
             )


    fig = legend(fig=fig,
             swap={'1': 'Primary School', '2': 'High School', '3': 'BA', '4': 'MA', '5': 'Specialist', '6': 'PhD'}
             )
    return fig

def legend(fig, swap):
    for i, data in enumerate(fig.data):
        for element in data:
            if element == 'name':
                fig.data[i].name = swap[fig.data[i].name]
    return fig