# advanced_dashboard.py
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='live-update-graph', animate=True),
    dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0),
    html.Hr(),
    html.Div("Customizable Dashboard")
])

@app.callback(
    dash.dependencies.Output('live-update-graph', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    x = list(range(10))
    y = [i * 2 for i in x]
    return go.Figure(data=[go.Scatter(x=x, y=y)])

if __name__ == '__main__':
    app.run_server(debug=True)
