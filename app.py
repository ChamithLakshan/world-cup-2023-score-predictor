import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Australia', 'Pakistan', 'Afghanistan', 'Scotland', 'Zimbabwe',
       'New Zealand', 'Bangladesh', 'South Africa', 'India', 'England',
       'Sri Lanka', 'West Indies',
       'Ireland',  'Netherlands']

cities = ['Mirpur',
          'Harare',
          'London',
          'Colombo',
          'Bulawayo',
          'Abu Dhabi',
          'Sydney',
          'Rangiri',
          'Melbourne',
          'Sharjah',
          'Dubai',
          'Centurion',
          'Adelaide',
          'Dublin',
          'Perth',
          'Birmingham',
          'Johannesburg',
          'Brisbane',
          'Auckland',
          'Southampton',
          'Pallekele',
          'Wellington',
          'Hamilton',
          'Guyana',
          'Cardiff',
          'Durban',
          'Belfast',
          'Port Elizabeth',
          'Manchester',
          'Jamaica',
          'Nottingham',
          'Antigua',
          'Chandigarh',
          'Cape Town',
          'Christchurch',
          'St Kitts',
          'Trinidad',
          'Karachi',
          'Hambantota',
          'Leeds',
          'Napier',
          'St Lucia',
          'Hobart',
          'Barbados',
          'Chittagong',
          'Lahore',
          'Mumbai',
          'Chester-le-Street',
          'Ahmedabad',
          'Grenada',
          'Dhaka',
          'Delhi',
          'Nagpur',
          'Dunedin',
          'Jaipur',
          'Chennai',
          'Nelson',
          'Mount Maunganui',
          'Visakhapatnam',
          'Kolkata',
          'Bristol',
          'Canberra',
          'Bloemfontein',
          'Fatullah',
          'St Vincent',
          'Benoni',
          'Rajkot',
          'Edinburgh',
          'Bangalore',
          'Hyderabad',
          'Kanpur',
          'Potchefstroom',
          'Cuttack',
          'Kuala Lumpur',
          'Indore',
          'Greater Noida',
          'Pune',
          'Rawalpindi',
          'Paarl',
          'Multan',
          'Dehra Dun']

st.title('ODI Cricket match score predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select batting team', sorted(teams))

with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select Ground(city)',sorted(cities))

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score')
with col4:
    overs = st.number_input('Overs done(Should be over>5)')
with col5:
    wickets = st.number_input('Wickets gone')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict'):
    balls_left = 300 - (overs * 6)
    wickets_left = 10 - wickets
    crr = current_score/overs
    input_df = pd.DataFrame(
    {'batting_team':[batting_team],'bowling_team':[bowling_team],'city': [city], 'current_score':[current_score], 'balls_left':[balls_left], 'wickets_left':[wickets_left], 'crr':[crr], 'last_five':[last_five]}
    )
    result = pipe.predict(input_df)
    st.text(int(result[0]))
