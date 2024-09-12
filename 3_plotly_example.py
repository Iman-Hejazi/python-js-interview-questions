'''
1) read 'plolty_example.csv' to a dataframe
2) using plotly plot a line chart with "inc" as y axis vs "bit_depth" as x axis
3) set the x axis label to "Bit Depth" and y axis label to "Inclination"
4) set the y axis range to zero to 90
'''

import pandas as pd
import plotly.graph_objects as go


FIlE_NAME = 'plotly_example.csv'


# 1. read 'plolty_example.csv' to a dataframe
df = pd.read_csv(FIlE_NAME)

fig = go.Figure()
fig.add_trace(go.Line(x=df['bit_depth'], y=df['inc']))
# fig.show()

# 2. using plotly plot a line chart with "inc" as y axis vs "bit_depth" as x axis
# 3. set the x axis label to "Bit Depth" and y axis label to "Inclination"
# 4. set the y axis range to zero to 90
fig.update_layout(
    title='interview',
    xaxis_title='Bit Depth',
    yaxis_title='Inclination',
    yaxis=dict(
        range=[0, 90]
    )
)

fig.show()
