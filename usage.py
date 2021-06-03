import stlcgl
import json
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

app = dash.Dash(__name__)

with open('./mult_view.json') as data:
    dataString = data.read()

app.layout = html.Div([
    html.Div(id='output_rows'),
    html.Div(id='output_cols'),
    stlcgl.Cgl(
        id='input',
        divId='id_',
        network=dataString,
    ),
])


@app.callback(Output('output_rows', 'children'), [Input('input', 'value_rows')])
def display_output(value):
    return 'You have entered {}'.format(value)

@app.callback(Output('output_cols', 'children'), [Input('input', 'value_cols')])
def display_output(value):
    return 'You have entered {}'.format(value)

# @app.callback(Output('input', 'network'), [Input('output', 'children')])
# def change_network(kdjslf):
#     return dataString

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
