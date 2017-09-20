import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot
from flask import Flask, render_template

app = Flask('flask app')
@app.route('/')
def main():
    N = 500
    random_x = np.linspace(0, 1, N)
    random_y = np.random.randn(N)

    # Create a trace
    trace = go.Scatter(
    x = random_x,
    y = random_y
    )

    random_x = np.linspace(0, 1, N)
    random_y = np.random.randn(N)

    trace1 = go.Scatter(
    x = random_x,
    y = random_y
    )

    random_x = np.linspace(0, 1, N)
    random_y = np.random.randn(N)

    trace2 = go.Scatter(
    x = random_x,
    y = random_y
    )

    data = [trace]
    plotly_div = plot(data, show_link=False, output_type="div") 
    plotly2_div = plot([trace1,trace2], show_link=False, output_type="div")
    return render_template('main.html',
                           plotly_div=plotly_div,
                           plotly2_div=plotly2_div)

if __name__ == '__main__':
    app.run(debug=True)

