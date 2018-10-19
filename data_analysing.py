import plotly
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='zeeo_', api_key='uoLHoxIhGZdPQFkqtvQw')
data_file = open("materials/data.txt", 'r')

negative_retweets = list()
negative_likes = list()
positive_likes = list()
positive_retweets = list()
negative_score_base_on_likes = list()
negative_score_base_on_retweets = list()
positive_score_base_on_likes = list()
positive_score_base_on_retweets = list()
senti_base_on_likes = list()
senti_base_on_retweets = list()
times = list()

for i in range(1000000):
    data = data_file.readline()
    if data == "AYE":
        break
    data = data_file.readline()
    negative_likes.append(int(data[data.find("  "):]))
    data = data_file.readline()
    negative_retweets.append(int(data[data.find("  "):]))
    data = data_file.readline()
    data = data_file.readline()
    positive_likes.append(int(data[data.find("  "):]))
    data = data_file.readline()
    positive_retweets.append(int(data[data.find("  "):]))
    data = data_file.readline()
    negative_score_base_on_likes.append(float(data[data.find("  "):]))
    data = data_file.readline()
    negative_score_base_on_retweets.append(float(data[data.find("  "):]))
    data = data_file.readline()
    positive_score_base_on_likes.append(float(data[data.find("  "):]))
    data = data_file.readline()
    positive_score_base_on_retweets.append(float(data[data.find("  "):]))
    data = data_file.readline()
    senti_base_on_likes.append(float(data[data.find("  "):]))
    data = data_file.readline()
    senti_base_on_retweets.append(float(data[data.find("  "):]))
    data = data_file.readline()
    times.append(data[11:16])
    data = data_file.readline()
trace0 = go.Scatter(
    x=times,
    y=negative_likes,
    name='Simple dict: negative words * likes',
    line=dict(
        color=('rgb(205, 12, 24)'),
        width=4,
        dash='dash')
)
trace1 = go.Scatter(
    x=times,
    y=negative_retweets,
    name='Simple dict: negative words * retweets',
    line=dict(
        color=('rgb(205, 12, 24)'),
        width=4)
)
trace2 = go.Scatter(
    x=times,
    y=positive_likes,
    name='Simple dict: positive words * likes',
    line=dict(
        color=('rgb(0, 255, 0)'),
        width=4,
        dash='dash')
)
trace3 = go.Scatter(
    x=times,
    y=positive_retweets,
    name='Simple dict: positive words * retweets',
    line=dict(
        color=('rgb(0, 255, 0)'),
        width=4)
)
traces1 = [trace0, trace2]
traces2 = [trace1, trace3]

# Edit the layout
layout1 = dict(title='Sentiment analyse twits, with words: "bitcoin" OR "btc" OR "BTC" OR "Bitcoin"',
              xaxis=dict(title='Time'),
              yaxis=dict(title='value'),
              )
layout2 = dict(title='Sentiment analyse twits, with words: "bitcoin" OR "btc" OR "BTC" OR "Bitcoin"',
              xaxis=dict(title='Time'),
              yaxis=dict(title='value'),
              )
fig1 = dict(data=traces1, layout=layout1)
fig2 = dict(data=traces2, layout=layout2)
py.iplot(fig1, filename='styled-line1')
py.iplot(fig2, filename='styled-line2')