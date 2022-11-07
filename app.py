from re import X
from turtle import color, fillcolor, title, width
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
df = pd.read_csv("/Users/joasyepidan/Documents/Fall2022/VisualAnalytics-5122/5122_sl/resources/US Police shootings in from 2015-22.csv")
#Death by race
death_by_race = df.groupby("race", as_index=False)["name"].count()
#header
st.header("United States Police Report 🚨")

def header(url):
     st.markdown(f'<p style="color:#f44336;font-size:35px;border-radius:2%;">{url}</p>', 
     unsafe_allow_html=True)

#Navigation
st.sidebar.title('Navigation')

def stats(dataframe):
    st.header("Data Statistics")
    st.write(dataframe.describe())

def data_header(dataframe):
    header('Data Header')
    st.write(df.head())

def plot(dataframe):
    bar = alt.Chart(dataframe).mark_bar(color='red',
    opacity=0.4).encode(
    x=alt.X('race', title='Race'),
    y=alt.Y('name', title='Death'),
    color=alt.Color('race', legend=alt.Legend(title='Race'))
    ).properties(
    title='Death by Race', 
    width=300,
    height=600
    )
    st.altair_chart(bar, use_container_width=True) 

def interactive_plot():
    st.write('## This is an interactive plot where you pick 2 variables and check for correlation!')
    x_axis_val = st.selectbox('Select X-axis value', options=df.columns)
    y_axis_val = st.selectbox('Select Y-axis value', options=df.columns)

    st.write('you selection: ', x_axis_val)
    
    scatter = alt.Chart(df).mark_point().encode(
                x=x_axis_val,
                y=y_axis_val, 
                color=alt.value('red'),
                opacity=alt.value(0.5))

    st.altair_chart(scatter, use_container_width=True)


options = st.sidebar.radio('Pages',
options=['Home',
'Data Statistics',
'Data Header', 
'Plot',
'Interactive Plot'])

#Navigation Control
if options == 'Home':
    st.markdown('Below are lists of people killed by law enforcement in the United States, both on duty and off duty. Although Congress instructed the Attorney General in 1994 to compile and publish annual statistics on police use of excessive force, this was never carried out, and the Federal Bureau of Investigation does not collect these data. Deaths by age group in 2015, according to The Counted')
    st.write('https://en.wikipedia.org/wiki/Lists_of_killings_by_law_enforcement_officers_in_the_United_States')
if options == 'Data Statistics':
   stats(df)
elif options == 'Data Header':
    data_header(df)
elif options == 'Plot':
    plot(death_by_race)
elif options == 'Interactive Plot':
    interactive_plot()

