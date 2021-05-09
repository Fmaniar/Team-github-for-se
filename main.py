import dash
import dash_html_components as html
import dash_core_components as dcc
import covidgraphs as cgraphs
import salesgraph as sgraphs
import base64
import pandas as pd
import datetime
import io
import plotly.express as px
import dash_table
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df1 = pd.read_csv("train.csv")
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#Get location of Images (In this case headshots)-Junaid Maniar
image_filename = 'test1.png' 
joe_headshot = "joeimg1.png"
amer_headshot = "Amerimg2.PNG"
faisal_headshot = "faisalimg1.png"
cols = [{"label": "1", "value":"Ship Mode"},{"label": "2", "value": "City"},{"label": "3", "value": "Sales"}]
#Encode them to be decoded later-Junaid Maniar
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
joe_image = base64.b64encode(open(joe_headshot, 'rb').read())
amer_image = base64.b64encode(open(amer_headshot, 'rb').read())
faisal_image = base64.b64encode(open(faisal_headshot, 'rb').read())
app.layout = html.Div([
    #Create tabs that will be used to show off information and divide our program- Junaid Maniar
    dcc.Tabs([
        #This is the main introduction tab that will serve as, well and intro and description of what we're doing- Junaid Maniar
        dcc.Tab(label='Introduction', children=[
            html.Br(),
            html.Div([
                html.H1(
                "ITCS 3155 Final Project",
                style={
                    "textAlign": "center",
                    "color": "#000000",
                },
            ),
            #In the Introduction make a section stating the authors of this lab.
            html.H2(
                "The Visualization Station is a hub for your trending and personalized analytical needs!", style={
                    "textAlign":"center",
                    "color": "#000000",
                }),
            html.H2(
                "Meet the Creators!",
                style={
                    "font-size":"30px",
                },
            ),
            html.H3(
                "Junaid Maniar-Interface & Input your own Data Graph Creation",
                style={
                    "font-size":"20px",
                },
                
            ),
            html.Div([
                html.Img(src = 'data:image/png;base64,{}'.format(encoded_image.decode()))
            ]),
            html.H4(
                "Faisal Maniar-Sales Tab",
                style={
                    "font-size":"20px",
                },
            ),
            html.Div([
                html.Img(src = 'data:image/png;base64,{}'.format(faisal_image.decode()))
            ]),
            html.H5(
                "Youssof Amer-Covid Tab",
                style={
                    "font-size":"20px",
                },
            ),
            html.Div([
                html.Img(src = 'data:image/png;base64,{}'.format(amer_image.decode()))
            ]),
            html.H6(
                "Joe Mulaparthi-Data Upload & Sales Tab",
                style={
                    "font-size":"20px",
                },
            ),
            html.Div([
                html.Img(src = 'data:image/png;base64,{}'.format(joe_image.decode()))
            ]),
            #style={"background-image":"url(/assets/testbackground.png)"} <--- mess around with images gonna use colors for now
            ],style={
                    "height":"1500px"},
            ),
            
        ]
        ),
        dcc.Tab(label='Covid Data', children=[
            dcc.Graph(
                figure=cgraphs.eduBarChar()
            ),
            dcc.Markdown(''' **my graphs provides relation between age/education and trust in the govt, from what I see people with lower education and are older don't trust the govt while the educated and young trust the govt** - Youssof
            '''),
            
            dcc.Graph(
                figure=cgraphs.eduComp()
            ),
            dcc.Markdown('''
            **My graph provides an insight into the levels of compliance amongst the survey population, utilizing the subject's highest level of education achieved as a categorical organizer.  This is to test the hypothesis that those who have pursued higher levels of education are more likely to research the effects and causes of the virus, and are therefore more likely to adhere to the government's recommended protocols in order to cmbat the spread of the pandemic. As the box plot shows, while the results were not fully conclusive, it seems that there is, at the very least, a correlation: those who have studied at higher institutions of learning seem to display a higher level of compliance as well** -Joe
             '''),
        ]),
        dcc.Tab(label='Sales Data', children=[
            dcc.Graph(
                figure=sgraphs.shipHeatMap(),
                style= {'height':"1000px",
                        'width':"80%"},
            ),
            dcc.Markdown(''' **the bar graph shows the percentage break down of all sales for the 4 shipping modes provided by the data and from the graph we can see that the most popular shipping mode is standard class followed by second class then first class 
and same day delivery,we can most likely attribute this trend to the prices of the shipping mode but same day delivery's low representation could be because it is not availble for all transactions** - Faisal'''),
            dcc.Graph(
                figure=sgraphs.shipBarChar(),
                style={"height":"800px",
                        "weight":"80%"}
            ),
            dcc.Markdown(''' **the heat map compares the type of customer to the shipping mode they choose to use and the sales of each shipping mode determines the color of the square . What can be seen from the heat map is how popular the the combination of shipping mode and customer segment are based on the sales amount, with standard shipping
and Consumer customers being the most popular combination.** - Faisal'''),
            dcc.Graph(
                figure=sgraphs.shipbarg(),
                style={"height":"800px",
                        "weight":"80%"}
            ),
            dcc.Markdown(''' **From the boxplots we can the distributions of the data and all 4 plots have a right skew to them, but what is interesting is that there is a surprising number of outliers that the standard class shipping mode has and this can 
most likely be attributed to the amount of data points that the standard class contains compared to the rest of the shipping modes.** - Faisal''')
        ]),
        dcc.Tab(label='Input Your Own', children=[
            html.Div([dcc.Markdown('''**CURRENTLY THIS ONLY ACCEPTS CSV FILES**'''), ],
            style={"font-size":"40px"}),
            dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
    html.Div([dcc.Dropdown(id = 'gpick',
        options= [{"label": "bar", 'value':'1'},
                   {"label":"scatter", 'value':'2'},
                   {"label":'heatmap', 'value': '3'}], value= "2")
                   ]),
    html.Div([dcc.Dropdown(id = 'dd1',
            options=cols,
            multi = True
            ),], style = {"display": "block !important",
                          "margin-bottom":"3rem!important"}),
    html.Div(id = "dd1-output"),

            dcc.Graph(id="Mygraph"),
]),
            
        ]),
    ])

#This is the thing that lets me yoink the data from the uploaded csv
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    abc = []
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            global df1
            df1 = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            for col in df1.columns:
                abc.append({"Label" : col, "value": col})
                cols = abc
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df1 = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df1.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df1.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

#Call back to upload the data visually-Junaid
@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
#Callback that lets me upadte the value chosen section-Junaid
@app.callback(Output('dd1-output', 'children'),
    Input('dd1', 'value'))
def update_output(value):
    return 'You have selected "{}"'.format(value)
@app.callback(
    Output('dd1', 'options'),
    Input('gpick','value'))
#Callback that updates the options-Junaid
def set_dd_value(value):
    options = [{'label': idx, "value":idx} for idx in df1.columns]
    return options
#callback that lets me update the graph at the bottom of the final tab-Junaid
@app.callback(Output('Mygraph', 'figure'), [
Input('dd1', 'value'),
State("gpick", "value")
])
def update_graph(value,type):
    x = [1,2,3]
    y = [1,2,3]
    #value checking for the start of program run
    if not value:
        x = [1,2,3]
        y = [1,2,3]
    elif len(value) >= 2:
        x=df1[value[0]]
        y=df1[value[1]]
    if type == "1":
        fig = px.bar(x=x, y=y, title="Bar Graph of Selected Input")
    elif type == "2":
        fig = px.scatter(x=x, y=y)
    else:
         fig = px.imshow(df1[value])
    
    return fig
    
if __name__ == '__main__':
    app.run_server(debug=True)