import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


# Pure dash application
app = dash.Dash()

# load data once - consider reading data in the callback if you
# have constantly changing data and need it refreshed
df = pd.read_csv('data/gapminder.csv').dropna()

# Matching Hans Rosling's 2006 TEDx talk, 1964 to 2003
df = df[(df.year > 1963) & (df.year < 2004)]


app.layout = html.Div([
    html.H1('Gapminder revisited'),
    dcc.Graph(id='gapminder-graphic'),

    dcc.Slider(
        id='year--slider',
        min=df.year.min(),
        max=df.year.max(),
        value=df.year.min(),  # start at the beginning
        step=None,
        updatemode='drag',
        marks={str(year): str(year) for year in df.year.unique()}
    )
])


def bubble_chart(df, region):
    return go.Scatter(
            x=df.fertility[df.region == region],
            y=df.life_exp[df.region == region],
            text=df.Country[df.region == region] + ':' + df['pop'][df.region == region].astype(str),
            mode='markers',
            name=region,
            marker={
                'size': df['pop'][df.region == region] / 100000,
                'sizemode': 'area',
                'sizeref': 1,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )


@app.callback(
    dash.dependencies.Output('gapminder-graphic', 'figure'),
    [dash.dependencies.Input('year--slider', 'value')])
def update_graph(year_value):
    # subset dataframe by specific year
    df_year = df[df.year == year_value]

    return {
        'data': [bubble_chart(df_year, region) for region in df_year['region'].unique()],
        'layout': go.Layout(
            xaxis={
                'title': 'Children per woman (fertility rate)',
            },
            yaxis={
                'title': 'Life expectancy at birth (years)',
            },
            #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server()
