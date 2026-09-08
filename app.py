import streamlit as st
from inference import predict

st.title("🧠 Smart MCQ Solver")
st.markdown("Enter your MCQ question with options below.")

st.markdown("**Format:** Question A. Option1 B. Option2 C. Option3 D. Option4")

text = st.text_area("Question with Options", height=150)

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
