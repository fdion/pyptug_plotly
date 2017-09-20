import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask, render_template

server = Flask('flask app')


# A typical Flask setup
@server.route('/')
def main():
    return render_template('main.html',
                           title='Home')


# below is a dash app, reusing the above Flask server.
app = dash.Dash(name='dash_app', server=server, url_base_pathname='/dash')

# the rest is the same as dash_01.py
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
    # note the Flask server.run, instead of the Dash app.run_server!
    server.run(debug=True)
