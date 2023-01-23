import streamlit as st
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import style
from PIL import Image

import plotly
import plotly.express as px
import plotly.graph_objects as go

import cufflinks as cf
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot

pyo.init_notebook_mode(connected=True)
cf.go_offline()

import folder1,folder2
df=pd.read_csv('athlete_events.csv')
region=pd.read_csv('noc_regions (1).csv')


image = Image.open('olympic image.jpeg')

st.sidebar.image('olympic image.jpeg')




st.sidebar.title("Olympic Analysis")
df=folder1.sort_df()







user=st.sidebar.radio(
    "select an option",
    ('Overall','seleted_detail','Athlete_wise','Medals','Top5_country','Top10 Award winning sports','Male vs Female')

)

if user=='Medals':
    st.title('Medals Analysis')
    medals_tally=folder2.medals(df)
    st.dataframe(medals_tally)



if user=='Overall':
    st.title('Overall_view')
    df = folder1.sort_df()
    df=df.dropna()
    st.dataframe(df)

if user=='seleted_detail':
    st.title('Medals_Achieved')
    year,country=folder2.country_year(df)
    selected_year=st.sidebar.selectbox('select year',country)
    selected_country=st.sidebar.selectbox('select country',year)
    detail = folder2.medals(df)
    detail=folder2.detail(df,selected_country,selected_year)


    st.dataframe(detail)

if user=='Top5_country':
    st.title('Top_5 Medal winning country')
    top5 = df['region'].value_counts().reset_index().head()
    top5.rename(columns={'index': 'country', 'region': 'count'}, inplace=True)
    fig = px.bar(top5, x='country', y='count')
    st.plotly_chart(fig)

if user=='Top10 Award winning sports':
    sport = df['Sport'].value_counts().reset_index().head(10)
    sport.rename(columns={'index': 'Sports', 'Sport': 'counts'}, inplace=True)
    fig = px.bar(sport, y='counts', x='Sports', text_auto='.2s',
                 title="Top10 Award winning sports")
    st.plotly_chart(fig)

if user=='Male vs Female':
    x = df['Sex'].value_counts().reset_index()
    x=x.rename(columns={'index':'sex','Sex':'counts'})
    fig = px.bar(x, x="sex", y="counts", color="sex", title="male vs female")
    st.plotly_chart(fig)

if user=='Athlete_wise':
    st.title('Athlete_Details')
    athlete=folder2.name(df)
    selected_athlete=st.sidebar.selectbox('select athletes',athlete)



    athlete=folder2.athlete(df,selected_athlete)


    st.dataframe(athlete)



    

















