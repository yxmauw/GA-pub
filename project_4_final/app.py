## Instructions
# 1. Install the following packages
# plotly - https://plotly.com/python/getting-started/
# dash - https://dash.plotly.com/installation
# 2. Change data path file for the files

# To run this app:
# 1. Nagivate to the directory containing this file via terminal/anacoda prompt
# 2. Run `python app.py`
# 3. View the app at http://127.0.0.1:8050/ in your browser
# 4. Press Ctrl+C in your terminal/anaconda prompt to stop the server - this is the only way to stop the server, if you do not do this, the server will continue to run in the background

# Imports
from dash import Dash, html, dcc, dash_table

from flask import request
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

color_pal = sns.color_palette("muted")

"""
Do not edit the below map token
"""
# MAPBOX_TOKEN = open(".mapbox_token.txt").read().strip()
MAPBOX_TOKEN = "pk.eyJ1IjoieHNpbHZlcnIiLCJhIjoiY2w3dmhybTM3MGJ3dDN2bHBxdWlub2EwZSJ9.hiSrBJzfZAvozFLyZY-0mA"
px.set_mapbox_access_token(MAPBOX_TOKEN)

app = Dash(__name__)

"""
Change the below file path to your own file path
"""
# Reading of the data
df_train = pd.read_csv("../data/train.csv")
df_spray = pd.read_csv("../data/spray.csv")
df_weather = pd.read_csv("../data/weather.csv")

# Change date column to be datetime dtype
def date_add(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index("Date").sort_index()
    df["Year"] = df.index.year
    df["Month"] = df.index.month
    df["Day"] = df.index.day
    return df


df_train = date_add(df_train)
df_spray = date_add(df_spray)
df_weather = date_add(df_weather)


## Plot - Overall years
# Copy of dataframe
df1 = df_train.copy().drop(
    columns=["Block", "AddressAccuracy", "Address", "Street", "AddressNumberAndStreet"]
)
# Group by the day and sum the other values
df_train_year = df1.resample("M").sum().reset_index()

# Setting up the figure
overall_years = make_subplots(
    rows=3,
    cols=1,
    shared_xaxes=True,
    vertical_spacing=0.1,
    subplot_titles=(
        "Number of Mosquitoes vs Number of Wnv Mosquitoes per year",
        "Number of Mosquitoes vs Number of Traps per year",
        "Number of Mosquitoes vs Number of Sprays per year",
    ),
    specs=[[{"secondary_y": True}], [{"secondary_y": True}], [{"secondary_y": True}]],
)

# Plot 1 - Overall mos vs Wnv mos
overall_years.add_trace(
    go.Bar(
        x=df_train_year["Date"],
        y=df_train_year["NumMosquitos"],
        name="NumMosquitos",
        marker_color="#636EFA",
    ),
    row=1,
    col=1,
    secondary_y=False,
)

overall_years.add_trace(
    go.Scatter(
        x=df_train_year["Date"],
        y=df_train_year["WnvPresent"],
        name="WnvPresent",
    ),
    row=1,
    col=1,
    secondary_y=True,
)

# Plot 2 - Overall mos vs no. of traps
df_train_trap = df1.resample("M").count().reset_index()

overall_years.add_trace(
    go.Bar(
        x=df_train_year["Date"],
        y=df_train_year["NumMosquitos"],
        name="NumMosquitos",
        marker_color="#636EFA",
    ),
    row=2,
    col=1,
    secondary_y=False,
)

overall_years.add_trace(
    go.Scatter(
        x=df_train_trap["Date"],
        y=df_train_trap["Trap"],
        name="Trap",
    ),
    row=2,
    col=1,
    secondary_y=True,
)

# Plot 3 - Overall mos vs no. of sprays
df_spray_year = df_spray.resample("M").count().reset_index()

overall_years.add_trace(
    go.Bar(
        x=df_train_year["Date"],
        y=df_train_year["NumMosquitos"],
        name="NumMosquitos",
        marker_color="#636EFA",
    ),
    row=3,
    col=1,
    secondary_y=False,
)

overall_years.add_trace(
    go.Scatter(
        x=df_spray_year["Date"],
        y=df_spray_year["Latitude"],
        name="Spray",
    ),
    row=3,
    col=1,
    secondary_y=True,
)

overall_years.update_layout(
    hovermode="x unified",
    barmode="group",
    title_text="Number of mosquitos per year",
    height=1000,
    width=1200,
    showlegend=True,
)
overall_years.update_xaxes(title_text="Date")
overall_years.update_yaxes(title_text="Number of Mosquitos", row=1, col=1)
overall_years.update_yaxes(
    title_text="Number of Wnv Mosquitos", row=1, col=1, secondary_y=True
)
overall_years.update_yaxes(title_text="Number of Mosquitos", row=2, col=1)
overall_years.update_yaxes(title_text="Number of Traps", row=2, col=1, secondary_y=True)
overall_years.update_yaxes(title_text="Number of Mosquitos", row=3, col=1)
overall_years.update_yaxes(
    title_text="Number of Sprays", row=3, col=1, secondary_y=True
)

## Plot - Overall months
# Creating the dataframe
df_train_year = (
    df_train.copy()
    .drop(
        columns=[
            "Block",
            "AddressAccuracy",
            "Address",
            "Street",
            "AddressNumberAndStreet",
        ]
    )
    .groupby(["Year", "Month"], as_index=False)
    .sum()
)

# Plot 1 - Number of mosquitos per month
mos_month = px.histogram(
    x=df_train_year["Month"],
    y=df_train_year["NumMosquitos"],
    color=df_train_year["Year"],
    barmode="group",
)


mos_month.update_layout(
    barmode="group",
    title_text="Number of mosquitos per month over the years",
    yaxis_title="Number of mosquitos",
    xaxis_title="Month",
    height=500,
    width=1000,
)

# Plot 2 - Number of Wnv mosquitos per month
wnv_month = px.histogram(
    x=df_train_year["Month"],
    y=df_train_year["WnvPresent"],
    color=df_train_year["Year"],
    barmode="group",
)
wnv_month.update_layout(
    barmode="group",
    title_text="Number of mosquitos with WnvPresent per month over the years",
    yaxis_title="Number of WNV mosquitos",
    xaxis_title="Month",
    height=500,
    width=1000,
)

# # Plot 3 - Number of traps per month
# df_train_trap = df1.groupby(["Year", "Month"], as_index=False).count()
# trap_month = px.histogram(
#     x=df_train_trap["Month"],
#     y=df_train_trap["Trap"],
#     color=df_train_trap["Year"],
#     barmode="group",
# )

# trap_month.update_layout(
#     barmode="group",
#     title_text="Number of Traps placed per month over the years",
#     yaxis_title="Number of Traps",
#     xaxis_title="Month",
#     height=500,
#     width=1000,
# )

# # Plot 4 - Number of sprays per month
# df_spray_year = df_spray.groupby(["Year", "Month"], as_index=False).count()
# spray_month = px.histogram(
#     x=df_spray_year["Month"],
#     y=df_spray_year["Latitude"],
#     color=df_spray_year["Year"],
#     barmode="group",
#     color_discrete_sequence=["#00CC96", "#AB63FA"],
# )

# spray_month.update_layout(
#     barmode="group",
#     title_text="Number of sprays per month over the years",
#     yaxis_title="Number of sprays",
#     xaxis_title="Month",
#     height=500,
#     width=1000,
# )

## Plot - Species
# Bar chart of count of different species
overall_species = px.histogram(
    df_train,
    x="Species",
    # y="NumMosquitos",
    color="WnvPresent",
    text_auto=True,
    barmode="group",
    height=500,
    width=1000,
)

overall_species.update_layout(hovermode="x")

overall_species.update_layout(
    height=500,
    title_text="Number of mosquitos per species",
    yaxis_title="Number of mosquitos",
    xaxis_title="Species",
)

# # Bar chart of count of different species per month
# # Plot of species vs mos
# # Creating the dataframe
# df_train_species = df_train.groupby(["Year", "Month", "Species"], as_index=False)[
#     "NumMosquitos"
# ].sum()
# # Plot 1
# species_mos = px.histogram(
#     x=df_train_species["Month"],
#     y=df_train_species["NumMosquitos"],
#     color=df_train_species["Species"],
#     barmode="group",
#     height=500,
#     width=1000,
# )

# species_mos.update_layout(
#     barmode="group",
#     title_text="Number of mosquitos of different species per month",
#     yaxis_title="Number of mosquitos",
#     xaxis_title="Month",
# )

# # Creating the dataframe
# df_train_species = df_train.groupby(["Year", "Month", "Species"], as_index=False)[
#     "WnvPresent"
# ].sum()
# # Plot 3
# species_wnv = px.histogram(
#     x=df_train_species["Month"],
#     y=df_train_species["WnvPresent"],
#     color=df_train_species["Species"],
#     barmode="group",
#     height=500,
#     width=1000,
# )

# species_wnv.update_layout(
#     barmode="group",
#     title_text="Number of wnv mosquitos of different species per month",
#     yaxis_title="Number of mosquitos",
#     xaxis_title="Month",
# )


## Mapping
# Overall mapping
# Create a copy of the dataframe to work with
df1 = df_train.copy().reset_index()
df1 = date_add(df1)

# Aggregate the data
overall_date = (
    df1.groupby([pd.Grouper(freq="Y"), "Address"])
    .agg(
        {
            "NumMosquitos": "sum",
            "WnvPresent": "sum",
            "Latitude": "median",
            "Longitude": "median",
        }
    )
    .reset_index()
)

overall_date["Date"] = overall_date["Date"].dt.date

overall_years_ani = px.scatter_mapbox(
    overall_date,
    lat="Latitude",
    lon="Longitude",
    color="WnvPresent",
    size="NumMosquitos",
    # color_continuous_scale=px.colors.sequential.Bluered,
    hover_data=["NumMosquitos", "WnvPresent"],
    animation_frame="Date",
    zoom=9,
    width=1000,
    height=900,
)

overall_years_ani.update_layout(
    title="Total Mosquitoes and Wnv over the years",
    # mapbox_style="open-street-map"
)

# To see the effectiveness of overall spraying
# Create a copy of the dataframe to work with
df1 = df_train.copy().reset_index()
df1 = date_add(df1)

# Aggregate the data
overall_add = (
    df1.groupby(["Address"])
    .agg(
        {
            "NumMosquitos": "sum",
            "WnvPresent": "sum",
            "Latitude": "median",
            "Longitude": "median",
        }
    )
    .reset_index()
)

df_spray_copy = df_spray.reset_index().copy()
df_spray_copy["Date"] = df_spray_copy["Date"].dt.date

spray_loc = px.scatter_mapbox(
    df_spray_copy,
    lat="Latitude",
    lon="Longitude",
    size_max=15,
    zoom=9,
    color_discrete_sequence=["darkgreen"],
    opacity=0.5,
    # animation_frame="Date",
    width=1000,
    height=900,
)

spray_loc_2 = px.scatter_mapbox(
    overall_add,
    lat="Latitude",
    lon="Longitude",
    size="NumMosquitos",
    color="WnvPresent",
    # color_continuous_scale=px.colors.sequential.Bluered,
    zoom=9,
)

spray_loc.add_trace(spray_loc_2.data[0])

spray_loc.update_layout(title="Spray Locations", mapbox_style="open-street-map")

# Map of spray on years 2011 and 2013
overall_add = (
    df1.groupby(["Year", "Address"])
    .agg(
        {
            "NumMosquitos": "sum",
            "WnvPresent": "sum",
            "Latitude": "median",
            "Longitude": "median",
        }
    )
    .reset_index()
)

spray_loc_2011 = px.scatter_mapbox(
    df_spray_copy.query("Year == 2011"),
    lat="Latitude",
    lon="Longitude",
    size_max=15,
    zoom=9,
    color_discrete_sequence=["darkgreen"],
    opacity=0.5,
    # animation_frame="Date",
    width=1000,
    height=900,
)

spray_loc_2011_2 = px.scatter_mapbox(
    overall_add.query("Year == 2011"),
    lat="Latitude",
    lon="Longitude",
    size="NumMosquitos",
    color="WnvPresent",
    # color_continuous_scale=px.colors.sequential.Bluered,
    zoom=9,
)

spray_loc_2011.add_trace(spray_loc_2011_2.data[0])

spray_loc_2011.update_layout(
    title="Spray Locations - 2011", mapbox_style="open-street-map"
)

spray_loc_2013 = px.scatter_mapbox(
    df_spray_copy.query("Year == 2013"),
    lat="Latitude",
    lon="Longitude",
    size_max=15,
    zoom=9,
    color_discrete_sequence=["darkgreen"],
    opacity=0.5,
    width=1000,
    height=900,
)

spray_loc_2013_2 = px.scatter_mapbox(
    overall_add.query("Year == 2013"),
    lat="Latitude",
    lon="Longitude",
    size="NumMosquitos",
    color="WnvPresent",
    # color_continuous_scale=px.colors.sequential.Bluered,
    zoom=9,
)

spray_loc_2013.add_trace(spray_loc_2013_2.data[0])

spray_loc_2013.update_layout(
    title="Spray Locations - 2013", mapbox_style="open-street-map"
)

## Weather plots

# Creating the dataframe
# Removing whitespace in the values
# Replacing the values with np.nan
# Filling the nan values with forward fill
# Changing the type to float

df_weather_edit = (
    df_weather.drop(columns=["Depth", "Water1", "SnowFall", "CodeSum"])
    .apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    .replace(["M", "T", "-"], np.nan)
    .fillna(method="ffill")
    .astype(float, errors="ignore")
)

df_weather_agg = df_weather_edit.resample("M").agg(
    {
        "Tmax": "mean",
        "Tmin": "mean",
        "Tavg": "mean",
        "Depart": "mean",
        "DewPoint": "mean",
        "WetBulb": "mean",
        "Heat": "mean",
        "Cool": "mean",
        "Sunrise": "mean",
        "Sunset": "mean",
        "StnPressure": "mean",
        "SeaLevel": "mean",
        "ResultSpeed": "mean",
        "ResultDir": "mean",
        "AvgSpeed": "mean",
    }
)

# Merge the num of mos and the wnvpresent to the weather data to see the relationship betwewen the 2 datasets
df_train_mos_wnv_sum = df_train.resample("M")["NumMosquitos", "WnvPresent"].sum()

# new df created with the train + weather data, and merged on the dates
df_weather_agg_train = pd.merge(
    left=df_weather_agg,
    right=df_train_mos_wnv_sum,
    how="left",
    left_index=True,
    right_index=True,
)

df_weather_agg_train.dropna().head()
df_weather_agg_train = date_add(df_weather_agg_train.dropna().reset_index())

# Input of correlation data table
# Create dataframe
df_corr = (
    df_weather_agg_train.dropna()
    .corr()["NumMosquitos"]
    .sort_values(ascending=False)
    .reset_index()
    .query("NumMosquitos > 0")
    .round(2)
)

# Plot 1 - temperature vs mosquito count
temp_mos = make_subplots(specs=[[{"secondary_y": True}]])

temp_mos.add_trace(
    go.Bar(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["NumMosquitos"],
        name="NumMosquitos",
        opacity=0.5,
    ),
    secondary_y=True,
)

temp_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["Tmax"],
        name="Tmax",
    ),
    secondary_y=False,
)


temp_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["Tmin"],
        name="Tmin",
    ),
    secondary_y=False,
)

temp_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["Tavg"],
        name="Tavg",
    ),
    secondary_y=False,
)


temp_mos.update_layout(
    hovermode="x unified",
    title="Temperature vs Mosquito Count",
    height=500,
    width=1000,
)
temp_mos.update_xaxes(title_text="Date")
temp_mos.update_yaxes(title_text="NumMosquitos", secondary_y=True)
temp_mos.update_yaxes(title_text="Temperature", secondary_y=False)

# Plot 2 - sunrise/sunset vs the num of mos
sun_mos = make_subplots(specs=[[{"secondary_y": True}]])

sun_mos.add_trace(
    go.Bar(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["NumMosquitos"],
        name="NumMosquitos",
        opacity=0.5,
    ),
    secondary_y=True,
)

sun_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["Sunrise"],
        name="Sunrise",
    ),
    secondary_y=False,
)


sun_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["Sunset"],
        name="Sunset",
    ),
    secondary_y=False,
)

sun_mos.update_layout(
    hovermode="x unified",
    height=600,
    width=1000,
    title="Sunrise/Sunset vs Mosquito Count",
)
sun_mos.update_xaxes(title_text="Date")
sun_mos.update_yaxes(title_text="NumMosquitos", secondary_y=True)
sun_mos.update_yaxes(title_text="Sunrise/Sunset", secondary_y=False)

# Plot 3 - dewpoint and depart vs the num of mos
dew_depart_mos = make_subplots(specs=[[{"secondary_y": True}]])

dew_depart_mos.add_trace(
    go.Bar(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["NumMosquitos"],
        name="NumMosquitos",
        opacity=0.5,
    ),
    secondary_y=True,
)

dew_depart_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["Depart"],
        name="Depart",
    )
)

dew_depart_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["DewPoint"],
        name="DewPoint",
    ),
    secondary_y=False,
)

dew_depart_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index, y=df_weather_agg_train["WetBulb"], name="WetBulb"
    ),
    secondary_y=False,
)

dew_depart_mos.update_layout(
    hovermode="x unified",
    height=600,
    width=1000,
    title="Depart/Dewpoint vs Mosquito Count",
)

dew_depart_mos.update_xaxes(title_text="Date")
dew_depart_mos.update_yaxes(title_text="NumMosquitos", secondary_y=True)
dew_depart_mos.update_yaxes(title_text="DewPoint/Depart", secondary_y=False)

# Plot 4 - stnpressure and sealevel vs num of mos
stnpres_sea_mos = make_subplots(specs=[[{"secondary_y": True}]])

stnpres_sea_mos.add_trace(
    go.Bar(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["NumMosquitos"],
        name="NumMosquitos",
        opacity=0.5,
    ),
    secondary_y=True,
)

stnpres_sea_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["StnPressure"],
        name="StnPressure",
    )
)

stnpres_sea_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["SeaLevel"],
        name="SeaLevel",
    ),
    secondary_y=False,
)

stnpres_sea_mos.update_layout(
    hovermode="x unified",
    height=600,
    width=1000,
    title="StnPressure/SeaLevel vs Mosquito Count",
)

stnpres_sea_mos.update_xaxes(title_text="Date")
stnpres_sea_mos.update_yaxes(title_text="NumMosquitos", secondary_y=True)
stnpres_sea_mos.update_yaxes(title_text="StnPressure/SeaLevel", secondary_y=False)

# Plot 5 - resultspeed, resultdir and avgspeed vs num of mos
res_speed_mos = make_subplots(specs=[[{"secondary_y": True}]])

res_speed_mos.add_trace(
    go.Bar(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["NumMosquitos"],
        name="NumMosquitos",
        opacity=0.5,
    ),
    secondary_y=True,
)

res_speed_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["ResultSpeed"],
        name="ResultSpeed",
    )
)

res_speed_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["ResultDir"],
        name="ResultDir",
    ),
    secondary_y=False,
)

res_speed_mos.add_trace(
    go.Scatter(
        x=df_weather_agg_train.index,
        y=df_weather_agg_train["AvgSpeed"],
        name="AvgSpeed",
    ),
    secondary_y=False,
)

res_speed_mos.update_layout(
    hovermode="x unified",
    height=600,
    width=1000,
    title="ResultSpeed/ResultDir/AvgSpeed vs Mosquito Count",
)

res_speed_mos.update_xaxes(title_text="Date")
res_speed_mos.update_yaxes(title_text="NumMosquitos", secondary_y=True)
res_speed_mos.update_yaxes(
    title_text="ResultSpeed/ResultDir/AvgSpeed", secondary_y=False
)

## Dash layout
app.layout = html.Div(
    children=[
        # All elements from the top of the page
        # 1st element
        html.Div(
            [
                html.H1(
                    children="Total Mosquitos, WnvPresent and Traps over the years"
                ),
                html.Div(
                    children="""
          
        """
                ),
                dcc.Graph(id="num_mos_year", figure=overall_years),
            ]
        ),
        # 2nd element
        html.Div(
            [
                html.H1(
                    children="Overall map of total Mosquitos, WnvPresent, Traps and Sprays over the months"
                ),
                html.Div(
                    children="""
            
        """
                ),
                dcc.Graph(id="mos_month", figure=mos_month),
                dcc.Graph(id="wnv_month", figure=wnv_month),
                # dcc.Graph(id="trap_month", figure=trap_month),
                # dcc.Graph(id="spray_month", figure=spray_month),
            ]
        ),
        # 3rd element
        html.Div(
            [
                html.H1(children="Species"),
                html.Div(
                    children="""
                    
                    """
                ),
                dcc.Graph(id="overall_species", figure=overall_species),
                # dcc.Graph(id="species_mos", figure=species_mos),
                # dcc.Graph(id="species_wnv", figure=species_wnv),
            ]
        ),
        # New Div for all elements in the new 'row' of the page
        # dash_table.DataTable(df_train.to_dict("records")),
        # map element 1
        html.Div(
            [
                html.H1(
                    children="Overall map of total Mosquitos, WnvPresent and Traps over the years"
                ),
                html.Div(
                    children="""
            
        """
                ),
                dcc.Graph(id="overall_years_ani", figure=overall_years_ani),
            ]
        ),
        # Map element 2
        html.Div(
            [
                html.H1(children="Spray Locations"),
                html.Div(
                    children="""
            
        """
                ),
                dcc.Graph(id="spray_loc", figure=spray_loc),
                dcc.Graph(id="spray_loc_2011", figure=spray_loc_2011),
                dcc.Graph(id="spray_loc_2013", figure=spray_loc_2013),
            ]
        ),
        html.Div(
            [
                html.H1(children="Weather"),
                html.Div(
                    children="""
            Correlation Table of Weather Data Against Mosquito Count
        """
                ),
                dash_table.DataTable(
                    data=df_corr.to_dict("records"), style_table={"width": 500}
                ),
                dcc.Graph(id="temp_mos", figure=temp_mos),
                dcc.Graph(id="sun_mos", figure=sun_mos),
                dcc.Graph(id="dew_depart_mos", figure=dew_depart_mos),
                dcc.Graph(id="stnpres_sea_mos", figure=stnpres_sea_mos),
                dcc.Graph(id="res_speed_mos", figure=res_speed_mos),
            ]
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
