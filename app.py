import streamlit as st
import requests
import time
import datetime
from datetime import datetime, date, time
import geocoder




'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
st.header("Date and Time of Pickup")
datestart = st.date_input("Date of Pickup")
datetime = st.time_input("what time?")
datetimeclean = str(datetime)[0:8]
# and used in order to select the displayed lines
key = str(datestart) +" " + datetimeclean + " UTC"
key

pickup_datetime = key
### pickup longitude

st.header("Pickup Spot")
pickup = st.text_input("Place of Pickup","Brooklyn")
g = geocoder.osm(pickup)
pickup_longitude = g.latlng[0]
pickup_latitude = g.latlng[1]
g


st.header("Dropoff Spot")
dropoff = st.text_input("Place of Dropoff","Harlem")
d = geocoder.osm(dropoff)
dropoff_longitude = d.latlng[0]
dropoff_latitude = d.latlng[1]
d

st.header("Passenger Count")
passenger_count = st.number_input("Number of Passengers",min_value=1,max_value=5)


x = dict(
    key=key,
    pickup_datetime=pickup_datetime,
    pickup_longitude=str(pickup_longitude),
    pickup_latitude=str(pickup_latitude),
    dropoff_longitude=str(dropoff_longitude),
    dropoff_latitude=str(dropoff_latitude),

    passenger_count=passenger_count
)
url = f"https://wagon-taxi-5n66xcem5q-ew.a.run.app/predict_fare/?key={x['key']}&pickup_datetime={x['pickup_datetime']}&pickup_longitude={x['pickup_longitude']}&pickup_latitude={x['pickup_latitude']}&dropoff_longitude={x['dropoff_longitude']}&dropoff_latitude={x['dropoff_latitude']}&passenger_count={x['passenger_count']}"

if url == 'https://wagon-taxi-5n66xcem5q-ew.a.run.app/predict_fare/':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

response = requests.get(url).json()

st.header("Prediction")
response["prediction"]

