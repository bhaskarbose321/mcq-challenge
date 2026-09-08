import streamlit as st
from inference import predict

st.title("🧠 Smart MCQ Solver")

text = st.text_area("Enter your MCQ question", height=150)

if st.button("🔮 Predict Answer", type="primary"):
    if text.strip():
        with st.spinner("Analyzing..."):
            try:
                result = predict(text)
                st.success(f"### ✅ Predicted Answer: {result}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.error("Please enter a question with options.")
