from dash import Dash, html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv("Data/athlete_events.csv")

styles = {  
    "div_main": {
        'backgroundColor': '#FBE9D1',
        'height': '100vh',
        'display': 'flex',
        'flexDirection': 'column',
    },
    "div_head":{
        'flex': '0 0 auto',
        'padding': '20px',
        'backgroundColor': '#FBE9D1'
    },
    "div_title": {
        "text-align": "center",
        "font-size": "40px",
        "font-weight": "bold",
        "color": "#444339",
    }}

app.layout = html.Div( style=styles["div_main"], children=[ 
    html.Div( style=styles["div_head"], children=[ 
        html.Div("Project OS", style=styles["div_title"]),
        html.Hr(),
    ]),
    dbc.Table.from_dataframe(df[df["NOC"] == "HUN"].head(),   bordered=True,
    dark=True,
    hover=True,
    responsive=True,
    striped=True,)
    ])

if __name__ == "__main__":
    app.run(debug=True)