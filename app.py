import pandas as pd
from dash import Output, Input, Dash, dcc
import dash_mantine_components as dmc
import plotly.express as px


df = pd.read_csv("data/processed_sales.csv")

app = Dash(__name__)

app.layout = dmc.MantineProvider(
    children = dmc.Container(
        [
            dmc.Title("Pink Morsel Sales Trend: Before & After Price Increase (Jan 15, 2021)", order = 2, ta = "center", my = 20),

            dmc.Space(30),

            dcc.Graph(id = "sales-graph"),
            dmc.Text(id = "dummy", children = "load", style = {"display": "none"})
        ],
        fluid = True
    )
)

@app.callback(
    Output("sales-graph", "figure"),
    Input("dummy", "children")
)

def create_graph(_):
    df["date"] = pd.to_datetime(df["date"])
    daily_sales = df.groupby("date")["sales"].sum().reset_index()

    fig = px.line(
        daily_sales,
        x = "date",
        y = "sales",
        title = "Daily Sales of Pink Morsel",
        markers = True
    )

    return fig


if __name__ == "__main__":
    app.run(debug = True)