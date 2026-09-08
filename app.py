import streamlit as st
from inference import predict

st.title("🧠 Smart MCQ Solver")
st.markdown("Enter your question and options below to predict the correct answer.")

# Question input
question = st.text_area("Question", placeholder="e.g., What is the capital of France?", height=80)

# Options input
st.markdown("### Options")
col1, col2 = st.columns(2)
with col1:
    option_a = st.text_input("Option A", placeholder="e.g., Berlin")
    option_b = st.text_input("Option B", placeholder="e.g., Madrid")
    option_c = st.text_input("Option C", placeholder="e.g., Paris")
with col2:
    option_d = st.text_input("Option D", placeholder="e.g., Rome")
    option_e = st.text_input("Option E", placeholder="e.g., (optional)")

# Predict button
if st.button("🔮 Predict Answer", type="primary"):
    if not question.strip():
        st.error("Please enter a question.")
    elif not any([option_a, option_b, option_c, option_d, option_e]):
        st.error("Please enter at least one option.")
    else:
        # Combine question and options in the expected format
        parts = [question.strip()]
        if option_a.strip():
            parts.append(f"A. {option_a.strip()}")
        if option_b.strip():
            parts.append(f"B. {option_b.strip()}")
        if option_c.strip():
            parts.append(f"C. {option_c.strip()}")
        if option_d.strip():
            parts.append(f"D. {option_d.strip()}")
        if option_e.strip():
            parts.append(f"E. {option_e.strip()}")
        
        combined_text = " ".join(parts)
        
        # Show loading state
        with st.spinner("Analyzing..."):
            try:
                result = predict(combined_text)
                st.success(f"### ✅ Predicted Answer: {result}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Instructions
st.markdown("---")
st.markdown("""
**How it works:**
1. Enter your MCQ question
2. Provide the options (at least one, up to five)
3. Click "Predict Answer" to see which option the model thinks is correct

**Note:** This uses a BiLSTM model trained on MCQ data. Results are predictions and may not always be accurate.
""")
