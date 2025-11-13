import pandas as pd
from dash import Output, Input, Dash, dcc
import dash_mantine_components as dmc
import plotly.express as px


df = pd.read_csv("data/processed_sales.csv")
regions = ["All"] + df["region"].unique().tolist()

app = Dash(__name__)

app.layout = dmc.MantineProvider(
    children = dmc.Container(
        [

            dmc.Title("Pink Morsel Sales Trend: Before & After Price Increase (Jan 15, 2021)", order = 2, ta = "center", my = 20, className="header-title"),

            dmc.Grid([

                dmc.GridCol(dmc.RadioGroup(
                    id="region-selector",
                    children = dmc.Group([dmc.Radio(i, value = i) for i in regions], my = 10),
                    value="All",
                    label="Choose Regions",
                    size="sm",
                    mt=10,
                ))
            ]),

            dmc.Space(h=30),
            dcc.Graph(id = "sales-graph"),
        ],
        fluid = True
    )
)

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-selector", "value")
)

def create_graph(region):

    df_filtered = df.copy()

    if region != "All":
        df_filtered = df_filtered[df_filtered["region"] == region]
    
    df_filtered["date"] = pd.to_datetime(df_filtered["date"])
    daily_sales = df_filtered.groupby("date")["sales"].sum().reset_index()

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