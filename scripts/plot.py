import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/avg_value_weighted_returns.csv')

fig = px.line(df, x = 'Date', y = 'Cnsmr', title='Consumer products monthly fluctuations')
fig.show()
