import streamlit as st
from inference import predict

st.title("Smart MCQ Solver - BiLSTM")

text = st.text_area("Enter question")

if st.button("Predict"):
    if text.strip():
        result = predict(text)
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please enter a question.")  st.write("Prediction:", result)

