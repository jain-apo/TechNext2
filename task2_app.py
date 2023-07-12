import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, callback, Output, Input

# Retrieve data from the REST endpoint
url = "https://testtechnext1-pearl118.b4a.run/search/api/phases/"
response = requests.get(url)
data = response.json()

# Extract relevant information from the data
labels = []
entries = []

for item in data:
    phase = item["phase"]
    entry = item["entries"]
    
    if phase is None:
        phase = "Unknown"
    
    labels.append(phase)
    entries.append(entry)

# Create bar plot using Plotly Express
fig = px.bar(x = labels, y = entries, color = labels)
fig.update_layout(
    xaxis_title = "Phase",
    yaxis_title = "Number of Entries",
    title = "Plot: Phases and Entries",
    xaxis = dict(tickangle = 0),
)

# Create line trace
line_trace = go.Scatter(
    x=labels,
    y=entries,
    mode="lines+markers",
    name="Line Chart",
    line=dict(color="red"),
    marker=dict(symbol="circle", size=8),
)

# Add line trace to the figure
fig.add_trace(line_trace)

# Display the figure
fig.show()

app = Dash(__name__)

# Define the layout
app.layout = html.Div(
    children=[
        dcc.Graph(figure=fig),
    ]
)

if __name__ == '__main__':
    app.run(debug=True)