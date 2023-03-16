import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('processed_donner_pass.csv')
print(df.head())

st.header("Weather in the Sierra Nevada")

st.write("In this plot, we can examine weather in the Sierra Nevada from 1970 to 2019.")

st.write("Our first interactive plot lets you input a year from 1970 to 2019, and displays each day's snowfall in cm.")

year_input = st.number_input('Pick a number', 1970, 2019)
fig = px.scatter(df.query('year==@year_input'), x='date', y='new_snow_cm')
st.plotly_chart(fig)

st.write("In this next plot, we can look at histograms for each of the daily precipitation data columns.")

month_input = st.selectbox(
    'Pick one:', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
fig = px.histogram(df.query('month==@month_input & daily_precip_cm!=0 & new_snow_cm!=0'),
                   x=['daily_precip_cm', 'new_snow_cm'])
st.plotly_chart(fig)

st.write("It is not a functional app yet. Under construction.")
