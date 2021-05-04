
# C:\Users\youss\PycharmProjects\mscovid\Supplementary_materials_-_dataset.csv

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

file = r'C:\Users\youss\Downloads\Supplementary_materials_-_dataset.csv'
df = pd.read_csv(file)


df = df[df['age'] != 'trust_gov']

print(df['age'])

fig = go.Figure()
fig = px.bar(df, x='education', y='trust_gov')
fig.add_trace(go.Bar(name="1 = Primary School", x=["education", "trust_gov"], y=[1,2]))
fig.add_trace(go.Bar(name="2 = High School", x=["education", "trust_gov"], y=[2,1]))
fig.add_trace(go.Bar(name="3 = BA Degree", x=["education", "trust_gov"], y=[1,2]))
fig.add_trace(go.Bar(name="4 = MA Degree", x=["education", "trust_gov"], y=[2,1]))
fig.add_trace(go.Bar(name="5 = Specialist Degree", x=["education", "trust_gov"], y=[1,2]))
fig.add_trace(go.Bar(name="6 = PhD Degree", x=["education", "trust_gov"], y=[2,1]))
fig.show()



# Youssof Amer