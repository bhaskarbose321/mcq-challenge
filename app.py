import streamlit as st
from inference import predict

st.title("🧠 Smart MCQ Solver")

col1, col2 = st.columns([4, 1])
with col1:
    text = st.text_area("Enter your MCQ question", height=150)
with col2:
    st.write("")  # Spacer
    button_clicked = st.button("predict answer", type="primary")

if button_clicked:
    if text.strip():
        with st.spinner("Analyzing..."):
            try:
                result = predict(text)
                st.success(f"### ✅ Predicted Answer: {result}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.error("Please enter a question with options.")
