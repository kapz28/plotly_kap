# -*- coding: utf-8 -*-

import sys
import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly
from plotly.offline import plot
import random


number_of_words=int(30)
top_words=[]
with open('dict_filteredv2.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
#     mydict = dict(reader) 
#     OrderedDict(zip(headers, row))
    index=0
    for row in reader:
        #print(row[0])
        single_word=row[0]
        if index <=30:
            top_words.append(single_word) 
            index = index+1; 

print(top_words)
#quit()


colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(number_of_words)]
weights = [random.randint(15, 35) for i in range(number_of_words)]



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                x=[random.random() for i in range(30)],
                y=[random.random() for i in range(30)],
                mode='text',
                text=top_words,
                marker={'opacity': 0.3},
                textfont={'size': weights,
                          'color': colors}
                ) #for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False},
                yaxis={'showgrid': False, 'showticklabels': False, 'zeroline': False}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
    
##################REFERENCE WORDCLOUD##############################
# words = dir(go)[:30]
# colors = [plotly.colors.DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(30)]
# weights = [random.randint(15, 35) for i in range(30)]
# 
# 
# import plotly
# import plotly.graph_objs as go
# from plotly.offline import plot
# import random
# data = go.Scatter(x=[random.random() for i in range(30)],
#                  y=[random.random() for i in range(30)],
#                  mode='text',
#                  text=words,
#                  marker={'opacity': 0.3},
#                  textfont={'size': weights,
#                            'color': colors})
# layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
#                     'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}})
# fig = go.Figure(data=[data], layout=layout)
# 
# plot(fig)


##############################FILTER START#########################
#following is code that was used to filtered the data
#played around with it for a bit 

# parsed_data = []
# csv.field_size_limit(sys.maxsize)

#played around with this to filter data from this link 
#https://github.com/mkearney/trumptweets

# with open('parsedtrumptweetsv6.csv', 'rU') as csvfile , open('parsedtrumptweetsv7.csv', 'wb') as csvfile2:
#     tweet_reader = csv.reader(csvfile, delimiter=' ', quotechar='|', dialect=csv.excel)
#     parsed_writer = csv.writer(csvfile2, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
#     for row in tweet_reader:
#         k = []
#         for i in row:
#             j = i.replace(' ','')
#             k.append(j)
#         parsed_writer.writerow([k])        

# store_words=[]
# with open('parsedtrumptweetsfinal.csv', 'rb') as csvfile:
#     tweet_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in tweet_reader:
#         row = row[0].strip('\"')
#         sentence = row.split(',')
#         for word in sentence:
#             word=word.lower()
#             store_words.append(word)
# 
# result_dict = dict( [ (i, store_words.count(i)) for i in set(store_words) ] )    

# with open('dict_filtered.csv', 'wb') as csv_file,open('dict_sorted.csv', 'rb') as csvfile:
#     reader = csv.reader(csvfile)
#     mydict = dict(reader)
#     writer = csv.writer(csv_file)  
#     for key, value in mydict.items():
#         if len(key) >=5:
#             writer.writerow([key, value])   
 
  




