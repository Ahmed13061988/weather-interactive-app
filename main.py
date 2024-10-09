import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forcast for next days")

place = st.text_input("Place: ")

days = st.slider("Forecast days", min_value=1, max_value=5, help="""
    The number of forecasted days 
""")

data = st.selectbox("Select data to view", options=["Temperature", "Sky"])

st.subheader(f"{data} for the next {days} days in {place}")

data = get_data(place, days, option)



d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Dates",
                                   "y": "Temperature (C)"})

st.plotly_chart(figure)
