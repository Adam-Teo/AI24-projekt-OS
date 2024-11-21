from dash import Dash, html
import dash_bootstrap_components as dbc
import pandas as pd
import style
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv("Data/athlete_events.csv")

styles = style.styles

app.layout = html.Div( style=styles["div_main"], children=[ 
    html.Div( style=styles["div_head"], children=[ 
        html.Div("Project OS", style=styles["div_title"]),
        html.Img( style={ "width":"200px", "height":"123px", "border":"3px solid black", "display":"block"},  src="olympic_flag_2.png" ),
        html.Hr(),
    ]),
    dbc.Table.from_dataframe(df[df["NOC"] == "HUN"].head(),   
        bordered=True,
        dark=True,
        hover=True,
        responsive=True,
        striped=True,)
    ])

if __name__ == "__main__":
    app.run(debug=True)