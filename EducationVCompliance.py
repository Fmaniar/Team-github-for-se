import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


file = r'C:\Users\mulap\OneDrive\Documents\Education\College\UNC Charlotte\2021\Spring\ITSC 3155\Projects\Final ' \
       r'Project\Team-github-for-se-main\Supplementary_materials_-_dataset.csv '

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


def legend(fig, swap):
    for i, data in enumerate(fig.data):
        for element in data:
            if element == 'name':
                fig.data[i].name = swap[fig.data[i].name]
    return fig


fig = legend(fig=fig,
             swap={'1': 'Primary School', '2': 'High School', '3': 'BA', '4': 'MA', '5': 'Specialist', '6': 'PhD'}
             )


fig.show()