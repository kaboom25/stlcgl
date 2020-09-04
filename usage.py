import stlcgl
import json
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

app = dash.Dash(__name__)

with open('./mult_view.json') as data:
    dataString = data.read()

app.layout = html.Div([
    html.Div(id='output'),
    stlcgl.Cgl(
        id='input',
        network=''
    ),
])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)

@app.callback(Output('input', 'network'), [Input('output', 'children')])
def change_network(kdjslf):
    return dataString

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
