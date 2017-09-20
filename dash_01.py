import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# Similar to the first app on Dash tutorial
app.layout = html.Div([
    html.H1('Hello Dashworld'),

    html.Div('''
        Dash: This is some plain text. Instead of a div, we can use markdown too.
    '''),

    dcc.Graph(
        id='hellodashworld-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Winston-Salem'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Bar Chart Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
