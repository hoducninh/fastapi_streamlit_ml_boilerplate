import requests
from requests_toolbelt import MultipartEncoder

import streamlit as st

st.title('The test for model UI')

# fastapi endpoint
url = 'http://fastapi:8000'
endpoint = '/predict'

st.write('''ABC testing''')

# input the numbers
median_income_in_block = st.number_input("median_income_in_block?")
median_house_age_in_blockbath = st.number_input("median_house_age_in_blockbath?")
average_rooms = st.number_input("average_rooms?")
average_bedrooms = st.number_input("average_bedrooms?")
population_per_block = st.number_input("population_per_block?")
average_house_occupancy = st.number_input("average_house_occupancy?")
block_latitude = st.number_input("block_latitude?")
block_longitude = st.number_input("block_longitude?")

url = 'http://127.0.0.1:8000/api/model/predict/'
listing_input = {
  "median_income_in_block": median_income_in_block,
  "median_house_age_in_blockbath": median_house_age_in_blockbath,
  "average_rooms": average_rooms,
  "average_bedrooms": average_bedrooms,
  "population_per_block": population_per_block,
  "average_house_occupancy": average_house_occupancy,
  "block_latitude": block_latitude,
  "block_longitude": block_longitude,
}
api_key = "cd1471ff-bf20-4edd-b3a4-33f0a1c1cc7e"

def process(listing_input, server_url: str):
    r = requests.post(
    url,
    data=listing_params,
    headers={"token": str(api_key)},
    )
    return r

if st.button('Get the result'):
    prediction = process(listing_params=listing_input, server_url=server_url)
    