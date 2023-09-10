import streamlit as st
import pickle 

model = pickle.load(open('predictor.pkl', 'rb'))

st.title("Predict the insurance Charges")

age = st.slider("Choose Age",0,100)
bmi = st.slider("Choose BMI",15,55)
children = st.slider("Choose Children",0,5)
smoker = st.select_slider("Choose Smoker", ['Smokes', 'Not Smokes'])
region = st.selectbox("Choose Region", ['southwest', 'southeast', 'northwest', 'northeast'])

