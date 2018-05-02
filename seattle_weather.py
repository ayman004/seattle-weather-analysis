import dash_core_components as dcc
import plotly.graph_objs as go
import dash
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output,Input
df = pd.read_csv('st.csv')
app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(children=[
	html.Div(
	dcc.Graph(id='my-graph'),style={'width': '98%'}),
	html.Div(children = [
	html.Label('Select a year',style={ 'color': 'green'
	}),
	dcc.Dropdown(
                id='year-slider',
                options=[{'label': i, 'value': i}  for i in df.year.unique()],
                value = df.year.min()
				
            ),
	html.Label('Y-axis column',style={ 'color': 'green'
	}),
	dcc.Dropdown(
                id='x-axis',
                options=[{'label': i, 'value': i} for i in ['PRCP', 'TMAX','TMIN']],
                value = 'PRCP'
            )],style={'width': '49%', 'display': 'inline-block'})
])
@app.callback(
	Output('my-graph', 'figure'),
	[Input('year-slider', 'value'),
	Input('x-axis', 'value')]
)
def update_figure(selected_year,xaxis_column_name):
	re_year =  df.ix[df['year'] == selected_year]
	print(re_year)
	return{
		'data':[{
			'x':re_year.DATE,
			'y' : re_year[xaxis_column_name]
			}
		],
		'layout': go.Layout({'font':{'color': 'green'},'title':'Seattle '+xaxis_column_name+' In '+str(selected_year), 'yaxis': {'title':xaxis_column_name},'plot_bgcolor':colors['background']}
        )
	}
if __name__ == '__main__':
	ADDRESS = '192.168.0.112'
	app.run_server()