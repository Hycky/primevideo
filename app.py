import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Carregar os dados
df = pd.read_csv('data/data.csv')

# Inicializar a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1('Dashboard Amazon Prime'),
    html.Div([
        # Componentes interativos
        dcc.Dropdown(id='content-type', options=[...], value='all'),
        dcc.RangeSlider(id='year-range', min=df['releaseYear'].min(), max=df['releaseYear'].max(), value=[...]),
        dcc.Checklist(id='genres', options=[...], value=[...])
    ]),
    html.Div([
        # Visualizações
        dcc.Graph(id='content-distribution'),
        dcc.Graph(id='genre-popularity'),
        dcc.Graph(id='release-trends'),
        dcc.Graph(id='country-heatmap'),
        dcc.Graph(id='rating-by-genre')
    ])
])

# Callbacks para atualizar os gráficos
@app.callback(
    [Output('content-distribution', 'figure'),
     Output('genre-popularity', 'figure'),
     Output('release-trends', 'figure'),
     Output('country-heatmap', 'figure'),
     Output('rating-by-genre', 'figure')],
    [Input('content-type', 'value'),
     Input('year-range', 'value'),
     Input('genres', 'value')]
)
def update_graphs(content_type, year_range, genres):
    # Lógica para filtrar os dados e criar os gráficos
    # ...
    return fig1, fig2, fig3, fig4, fig5

if __name__ == '__main__':
    app.run_server(debug=True)