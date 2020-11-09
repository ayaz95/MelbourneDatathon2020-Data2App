# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#df = pd.read_csv("Vic_Variance decomposition_IRA.csv")


##### Reading data from Victorian State
data = pd.read_csv("finalversion_vic.csv")

colors = ['blue', 'red', 'green']
line_size =[1.5,1.5,1.5]


obj = scaler.fit_transform(data[['Mobility_score']])
obj1 = scaler.fit_transform(data[['con_cases']])
obj2 = scaler.fit_transform(data[['demand']])
obj3 = scaler.fit_transform(data[['retail_and_recreation_percent_change_from_baseline']])

data['Mobility_score'] = obj
data['con_cases'] = obj1
data['demand'] = obj2
data['retail_and_recreation_percent_change_from_baseline'] = obj3


#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


##################    Change Graph ####################
fig = go.Figure()
fig3 = go.Figure()
fig4 = go.Figure()

#### Victoria ----> Line Graph Code [Mobility - Covid19 cases - Demand]
fig3.add_trace(go.Scatter(x=data['date'], y=data['Mobility_score'],
                    mode='lines',
                    name='Mobility (Stay at home)',connectgaps=True,line=dict(color='blue', width=line_size[0])))


fig3.add_trace(go.Scatter(x=data['date'], y=data['con_cases'],
                     mode='lines',
                     name='Covid-19 Cases Confirmed',connectgaps=True,line=dict(color=colors[1], width=line_size[1])))

fig3.add_trace(go.Scatter(x=data['date'], y=data['demand'],
                     mode='lines',
                     name='Electricity Demand',connectgaps=True,line=dict(color=colors[2], width=line_size[2]))) 



fig3.update_layout(
    autosize=False,
    width=1500,
    height=800,
    )








###### Victoria ------> Line Graph Code [Mobility - Demand]
fig4.add_trace(go.Scatter(x=data['date'], y=data['retail_and_recreation_percent_change_from_baseline'],
                    mode='lines',
                    name='Retail',connectgaps=True,line=dict(color='blue', width=line_size[0])))

fig4.add_trace(go.Scatter(x=data['date'], y=data['demand'],
                     mode='lines',
                     name='Electricity Demand',connectgaps=True,line=dict(color=colors[2], width=line_size[2]))) 
 

#### Stacked Bar Chart


#### Victoria -------> 
fig_vic = go.Figure()
file = 'Vic_Variance decomposition_IRA.xlsx'
xl = pd.ExcelFile(file)
#print(xl.sheet_names)
df1 = xl.parse('Victoria')

fig_vic.add_trace(go.Bar(x=df1['Period'], y=df1['COVID-19 Confirmed Cases'], name="COVID-19 Confirmed Cases"))
fig_vic.add_trace(go.Bar(x=df1['Period'], y=df1['Mobility Score'],name="Mobility Score"))
fig_vic.add_trace(go.Bar(x=df1['Period'], y=df1['Retail Activity'], name="Retail Activity"))
fig_vic.add_trace(go.Bar(x=df1['Period'], y=df1['Temperature'], name="Temperature"))
fig_vic.update_layout(barmode='relative', title_text='Relative Barmode')
fig.show()





##### Impulse Response Graph Retail
import plotly.express as px
fig_vic_impulse_retail = go.Figure()
fig_vic_impulse_retail  = px.line(df1, x=df1['Period'], y=df1['Retail_Activity IRA'], title='Retail Activity impulse')
fig_vic_impulse_retail.show()

##### Impulse Response Graph Covid-19
import plotly.express as px
fig_vic_impulse_covid = go.Figure()
fig_vic_impulse_covid  = px.line(df1, x=df1['Period'], y=df1['Covid-19 IRA'], title='COVID-19 impulse')
fig_vic_impulse_covid.show()

####################################################################################################################################


##### Reading data from NSW State
data_nsw = pd.read_csv("nsw_score_final.csv")

colors = ['blue', 'red', 'green']
line_size =[1.5,1.5,1.5]


obj = scaler.fit_transform(data_nsw[['score']])
obj1 = scaler.fit_transform(data_nsw[['covid confirmed cases']])
obj2 = scaler.fit_transform(data_nsw[['total demand']])
obj3 = scaler.fit_transform(data_nsw[['Retail and Recreation activity']])



data_nsw['Mobility_score'] = obj
data_nsw['con_cases'] = obj1
data_nsw['demand'] = obj2
data_nsw['Retail and Recreation activity'] = obj3

#fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


##################    Change Graph ####################
fig5 = go.Figure()
fig6 = go.Figure()
# fig4 = go.Figure()

#### NSW ----> Line Graph Code [Mobility - Covid19 cases - Demand]
fig5.add_trace(go.Scatter(x=data_nsw['date'], y=data_nsw['Mobility_score'],
                    mode='lines',
                    name='Mobility (Stay at home)',connectgaps=True,line=dict(color='blue', width=line_size[0])))


fig5.add_trace(go.Scatter(x=data_nsw['date'], y=data_nsw['con_cases'],
                     mode='lines',
                     name='Covid-19 Cases Confirmed',connectgaps=True,line=dict(color=colors[1], width=line_size[1])))

fig5.add_trace(go.Scatter(x=data_nsw['date'], y=data_nsw['demand'],
                     mode='lines',
                     name='Electricity Demand',connectgaps=True,line=dict(color=colors[2], width=line_size[2]))) 







###### NSW ------> Line Graph Code [Mobility - Demand]
fig6.add_trace(go.Scatter(x=data_nsw['date'], y=data_nsw['Retail and Recreation activity'],
                    mode='lines',
                    name='Retail',connectgaps=True,line=dict(color='blue', width=line_size[0])))

fig6.add_trace(go.Scatter(x=data_nsw['date'], y=data_nsw['demand'],
                     mode='lines',
                     name='Electricity Demand',connectgaps=True,line=dict(color=colors[2], width=line_size[2]))) 
 
##### NSW
fig_nsw = go.Figure()
file = 'Vic_Variance decomposition_IRA.xlsx'
xl = pd.ExcelFile(file)
print(xl.sheet_names)
df2 = xl.parse('NSW')

fig_nsw.add_trace(go.Bar(x=df2['Period'], y=df2['COVID-19 Confirmed Cases'], name="COVID-19 Confirmed Cases"))
fig_nsw.add_trace(go.Bar(x=df2['Period'], y=df2['Mobility Score'],name="Mobility Score"))
fig_nsw.add_trace(go.Bar(x=df2['Period'], y=df2['Retail Activity'], name="Retail Activity"))
fig_nsw.add_trace(go.Bar(x=df2['Period'], y=df2['Temperature'], name="Temperature"))
fig_nsw.update_layout(barmode='relative', title_text='Relative Barmode')
fig.show()



fig.update_layout(barmode='relative', title_text='Relative Barmode')




##### Impulse Response Graph Retail fo NSW
import plotly.express as px
fig_nsw_impulse_retail = go.Figure()
fig_nsw_impulse_retail  = px.line(df1, x=df2['Period'], y=df2['Impulse_Retail_Activity'], title='Retail Activity impulse')
fig_nsw_impulse_retail.show()

##### Impulse Response Graph Covid-19 for NSW
import plotly.express as px
fig_nsw_impulse_covid = go.Figure()
fig_nsw_impulse_covid  = px.line(df2, x=df2['Period'], y=df2['Covid_Cases_Impulse'], title='COVID-19 impulse')
fig_nsw_impulse_covid.show()
# labels={
#                      "trace0": "Sepal Length (cm)",
#                      "trace1": "Sepal Width (cm)",
#                      "trace2": "Species of Iris"})
#fig.show()


# fig.update_layout(
#     autosize=False,
#     width=1400,
#     height=500,
#     margin=dict(
#         l=50,
#         r=50,
#         b=100,
#         t=100,
#         pad=4,
#         barmode='relative', title_text='Relative Barmode'
#     ),)

### Image
# fig12 = go.Figure()
# fig12.add_layout_image(
#     dict(
#         source="img.jpg",
#         xref="paper", yref="paper",
#         x=1, y=1.05,
#         sizex=0.2, sizey=0.2,
#         xanchor="right", yanchor="bottom"
#     )
# )

# # update layout properties
# fig12.update_layout(
#     autosize=False,
#     height=800,
#     width=700,
#     bargap=0.15,
#     bargroupgap=0.1,
#     barmode="stack",
#     hovermode="x",
#     margin=dict(r=20, l=300, b=75, t=125),
#     title=("Moving Up, Moving Down<br>" +
#            "<i>Percentile change in income between childhood and adulthood</i>"),
# )
# fig12.show()


from skimage import io
img = io.imread('arch.jpg')
fig12 = px.imshow(img)

fig12.update_yaxes(visible=False, showticklabels=False)

fig12.update_xaxes(visible=False, showticklabels=False)

fig12.update_layout(
    autosize=False,
    width=1500,
    height=600,)
    # margin=dict(
    #     l=50,
    #     r=50,
    #     b=100,
    #     t=100,
    #     pad=4
    # ),)


### Victoria Moving Average 

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x = data['moving_average_cases'], y = data['moving_average_mob'],
                    line_shape='spline'))


fig1.add_annotation(text="Stage Four restrictions announced (02-08-2020)",
                  xref="paper", yref="paper",
                  x=0.88, y=0.65, showarrow=True, font={'color':'red'})

# fig1.add_annotation(text="Hot-spot lockdown (30-06-2020)",
#                   xref="paper", yref="paper",
#                   x=.7, y=0.86, showarrow=True, font={'color':'red'})


fig1.add_annotation(text="City lockdown announced (07-07-2020)",
                  xref="paper", yref="paper",
                  x=.7, y=0.97, showarrow=True, font={'color':'red'})


fig1.add_annotation(text="Face covering mandatory (19-07-2020)",
                  xref="paper", yref="paper",
                  x=.34, y=0.9, showarrow=True, font={'color':'red'})



fig1.update_traces(mode='lines+markers')



###### NSW Moving Average
fignsw1 = go.Figure()
fignsw1.add_trace(go.Scatter(x = data_nsw['ma_cases'], y = data_nsw['ma_score'],
                    line_shape='spline'))


# fig1.add_annotation(text="Stage Four restrictions announced (02-08-2020)",
#                   xref="paper", yref="paper",
#                   x=0.88, y=0.65, showarrow=True, font={'color':'red'})

# # fig1.add_annotation(text="Hot-spot lockdown (30-06-2020)",
# #                   xref="paper", yref="paper",
# #                   x=.7, y=0.86, showarrow=True, font={'color':'red'})


# fig1.add_annotation(text="City lockdown announced (07-07-2020)",
#                   xref="paper", yref="paper",
#                   x=.7, y=0.97, showarrow=True, font={'color':'red'})


# fig1.add_annotation(text="Face covering mandatory (19-07-2020)",
#                   xref="paper", yref="paper",
#                   x=.34, y=0.9, showarrow=True, font={'color':'red'})



fignsw1.update_traces(mode='lines+markers')







#### 

fig.update_layout(
     xaxis=dict(
        title="Month",
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        zeroline=True,
        showline=True,
        showticklabels=False,
        title="Change in Percentage"
    ),
    autosize=True,
    margin=dict(
        autoexpand=True,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=True,
    plot_bgcolor='white',
    title="Time varying relationship for factors influencing Electricity demand during Covid-19 Pandemic")

app.layout = html.Div(style={'backgroundColor': 'forestgreen'}, children=[
    html.H1(
        children='Melbourne Datathon',
        style={
            'textAlign': 'center',
            'color': 'white'
        }
    ),

    html.Div(children='CAN ELECTRICITY CONSUMPTION PATTERNS TELL US ANYTHING ABOUT THE PANDEMIC?', style={
        'textAlign': 'center',
        'color': 'white'
    }),




##### Tabs 
html.Div([
       
        dcc.Tabs([
            dcc.Tab(label='HomePage', children=[
            dcc.Graph(figure = fig12),
            #html.Div(html.H1('Heading', style={'backgroundColor':'white'}))
        ]),

            dcc.Tab(label='Victoria', children=[
            dcc.Graph(figure=fig3),
            dcc.Graph(figure=fig4),
            dcc.Graph(figure = fig1),
            dcc.Graph(figure=fig_vic),
            dcc.Graph(figure=fig_vic_impulse_retail),
            dcc.Graph(figure=fig_vic_impulse_covid),
            ]),

            dcc.Tab(label='New South Wales', children=[
                dcc.Graph(figure = fig5),
                dcc.Graph(figure=fig6),
                dcc.Graph(figure=fignsw1),
                dcc.Graph(figure=fig_nsw),
                dcc.Graph(figure=fig_nsw_impulse_retail),
                dcc.Graph(figure=fig_nsw_impulse_covid),
                    #Step change cuts 
                    #dcc.Graph(figure = fig1),
                     #, style={'float': 'right','margin': 'auto'}) 
            ]),
    ])
])
])
#html.Div([
            #  html.Div([
            # dcc.Graph(figure = fig1)],style={'float': 'right','margin': 'auto'}), 
            
            # html.Div([

#             dcc.Tab(label='Tab two', children=[
#                 #Step change cuts 
#                  dcc.Graph(figure = fig)
#                  ]   #, style={'float': 'right','margin': 'auto'}) 
#          ]),

# ])

    
if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')

# html.Div([
#             dcc.Graph(id='g2', figure=fig),
#         ])
     
#     ])
