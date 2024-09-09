# dashboard_settings.py
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Customizable Dashboard"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': 'OPT1'},
            {'label': 'Option 2', 'value': 'OPT2'}
        ],
        value='OPT1'
    ),
    dcc.Graph(id='custom-graph')
])

@app.callback(
    dash.dependencies.Output('custom-graph', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def update_graph(selected_option):
    if selected_option == 'OPT1':
        y = [1, 3, 2, 4]
    else:
        y = [4, 2, 3, 1]
    return {
        'data': [go.Bar(x=['A', 'B', 'C', 'D'], y=y)],
        'layout': go.Layout(title='Custom Graph')
    }

if __name__ == '__main__':
    app.run_server(debug=True)
