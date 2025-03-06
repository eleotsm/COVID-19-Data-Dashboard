import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px


df=pd.read_csv('/home/eleo/VSC_projects/covid-project/covid-data.csv')
# Check the available columns
print(df.head())
print(df.columns)

# Adjust the DataFrame to use the correct columns
df = df[['Entity', 'Day', 'Total confirmed deaths due to COVID-19 per 100,000 people']]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("COVID-19 Data Dashboard"),
    dcc.Dropdown(
        id='entity-dropdown',
        options=[
            {'label': entity, 'value': entity} for entity in df['Entity'].unique()
        ],
        value=df['Entity'].unique()[0]  # Default value
    ),
    dcc.Graph(id='covid-graph')
])

# Define the callback to update the graph
@app.callback(
    Output('covid-graph', 'figure'),
    [Input('entity-dropdown', 'value')]
)
def update_figure(selected_entity):
    filtered_df = df[df['Entity'] == selected_entity]
    fig = px.line(filtered_df, x='Day', y='Total confirmed deaths due to COVID-19 per 100,000 people', 
                  title=f'Total Confirmed Deaths in {selected_entity}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)