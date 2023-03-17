import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('processed_donner_pass.csv')
print(df.head())

st.header("Weather in the Sierra Nevada")

st.write("In this application, we can examine weather in the Sierra Nevada from 1970 to 2019.")


# Block that creates a scatter plot of new snow vs date, showing one year at a time, with user input deciding which year to show

st.write("Our first interactive plot lets you input a year from 1970 to 2019, and displays the daily snowfall (cm) for every day of that year.")

year_input = st.number_input('Pick a year between 1970 and 2019:', 1970, 2019)
fig = px.scatter(df.query('year==@year_input'), x='date',
                 y='new_snow_cm', labels={'new_snow_cm': 'new snow (cm)'})
st.plotly_chart(fig)

###


# Block that creates histograms of air temperature data per month; user input decides month and max/min/both temp data

st.write("In this next plot, we can look at histograms for daily air temperature data (in degrees F). You can choose to look at \
         distributions for any month of the year, for either minimum temp, maximum temp, or both. Data from all years between 1970 \
         and 2019 are plotted.")

month_input = st.selectbox(
    'Pick one month of the year to view its temperature data ("1" is January, and so on):', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

fig = px.histogram(df.query('month==@month_input'),
                   x=['air_temp_max_f', 'air_temp_min_f'], labels={'value': 'degrees Fahrenheit'})
st.plotly_chart(fig)

###


# Block that creates line graphs of various snow data over each year; user input decides which snow data

st.write('Next we have a plot that charts the cumulative amount of snow (in cm) over each year.')

checkbox = st.checkbox(
    'Show snowpack depth, season snow total, and snow/water height equivalent at the same time.')

if checkbox:
    pivot_by_year = df.pivot_table(index='year', aggfunc='max',
                                   values=['snowpack_depth_cm', 'season_total_snow_cm', 'snow_water_equivalent_cm'])
else:
    precip_input = st.selectbox('Choose from snow data:', [
                                'snowpack_depth_cm', 'season_total_snow_cm', 'snow_water_equivalent_cm'])
    pivot_by_year = df.pivot_table(
        index='year', aggfunc='max', values=precip_input)

fig = px.line(pivot_by_year, labels={'value': 'amount of snow/water (cm)'})
st.plotly_chart(fig)
