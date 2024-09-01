import streamlit as st

st.title("Weather forcast for next days")

place = st.text_input("Place: ")

days = st.slider("Forecast days", min_value=1, max_value=5, help="""
    The number of forecasted days 
""")


data = st.selectbox("Select data to view", options=["Temperature", "Sky"])


st.subheader(f"{data} for the next {days} days in {place}")
