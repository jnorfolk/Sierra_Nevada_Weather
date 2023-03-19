# Sierra_Nevada_Weather
Practicum Sprint 4 Project - Build App

My primary goal for this project was to build an app using streamlit with some interactive plots.

I took a dataset from Kaggle regarding weather in the Sierra Nevada from 1970 to 2019. It contains daily data on temperature, precipitation, snowfall, snow depth, etc. The dataset was not ready for plotting, so I spent a while processing it and getting the measurements into float format, and filling in some missing data based on remarks. Analysis of the data was not my focus, so I made some plots that I intended to carry over into my app. I looked at a scatter matrix first to get an idea of which relationships may be most interesting to look at.

In this app, you can look at the snowfall for every day in any year between 1970 and 2019, you can compare the histograms between the mimimum and maximum air temperatures for any particular month, and you can examine the relationship between total snowfall, snow depth, and the conversion between snow depth and water level.

If you wish to view my app on render.com, click on this link:
https://sierra-nevada-weather.onrender.com/

If you wish to run this app on your local machine, you will need to:
    1. Make sure streamlit, pandas, and plotly.express are installed.
    2. Clone this repository to your machine. One option is to use git commands in the terminal.
    3. Make sure the file 'app.py' is contained within your active directory in the terminal.
    4. Use the command "streamlit run app.py".
    5. Click on the URL that is provided after the program successfully runs.
    6. If the webpage is not found, a likely fix will be to navigate to .streamlit\config.toml and set serverAddress = "127.0.0.1", and then retry steps 3-5.