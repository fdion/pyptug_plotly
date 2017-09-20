""" dash_04.py

The only way right now to include raw html in the layout is to use the Iframe component.
What needs to happen is for somebody to write a RawHtml plugin (https://plot.ly/dash/plugins)
"""
import dash
import dash_core_components as dcc
import dash_html_components as html

raw_html = """
<H1>Dash: A web application framework for Python</H1>
<p>And this could be coming from a jinja2 template.
"""
app = dash.Dash()

app.layout = html.Div([
    html.Iframe(srcDoc=raw_html,
                seamless="seamless",
                style={'border': '0', 'width': "100%", 'height': "250"}),

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

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Iframe(srcDoc=raw_html,
                seamless="seamless",
                style={'border': '0', 'width': "100%", 'height': "250"}),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
