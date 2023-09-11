import streamlit as st
import pickle 
import numpy as np
import pandas as pd
from utils import mapping_dict, smoker_map, columns

model = pickle.load(open('predictor.pkl', 'rb'))

st.title("Predict the insurance Charges")

age = st.slider("Choose Age",0,100)
bmi = st.slider("Choose BMI",15,55)
children = st.slider("Choose Children",0,5)
smoker = st.select_slider("Choose Smoker", ['Smokes', 'Not Smokes'])
region = st.selectbox("Choose Region", ['southwest', 'southeast', 'northwest', 'northeast'])

def predict():
    row  = np.array([age, bmi, children, smoker_map[smoker], mapping_dict[region]])
    X = pd.DataFrame([row], columns=columns)
    prediction = model.predict(X)
    return prediction[0]
    

trigger = st.button("Predict", on_click=predict)

if trigger:
    prediction = predict()
    st.write(f"Predicted Insurance Charges: {prediction:.2f}")