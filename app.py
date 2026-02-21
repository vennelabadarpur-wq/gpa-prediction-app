import streamlit as st
import pickle
import numpy as np
import gdown


url = "https://drive.google.com/uc?id=1dKk_2tuSU7qTK02mJoFZmXqgIRwbuWoA"
gdown.download(url, "teja.pkl", quiet=False)

model = pickle.load(open("teja.pkl", "rb"))


st.title("Student GPA Prediction")

st.write("Enter student details below:")

sleep = st.number_input("Sleep Hours")
social = st.number_input("Social Media Hours")
study = st.number_input("Study Hours")
attendance = st.number_input("Attendance %")

if st.button("Predict GPA"):
    data = np.array([[sleep, social, study, attendance]])
    result = model.predict(data)
    st.success(f"GPA = {round(result[0],2)}")



