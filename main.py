import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forcast for next days")

place = st.text_input("Place: ")


days = st.slider("Forecast days", min_value=1, max_value=5, help="""
    The number of forecasted days 
""")

option = st.selectbox("Select data to view", options=["Temperature", "Sky"])

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_content = get_data(place, days)



    if option == "Temperature":
        temp = [i["main"]["temp"] / 10 for i in filtered_content]

        dates = [i["dt_txt"] for i in filtered_content]

        figure = px.line(x=dates, y=temp, labels={"x": "Dates",
                                                  "y": "Temperature (C)"})

        st.plotly_chart(figure)

    elif option == "Sky":
        skies = [i["weather"][0]["main"] for i in filtered_content]

        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        dates = [i["dt_txt"] for i in filtered_content]

        images_path = [images[condition] for condition in skies]

        st.image(images_path, width=115)
