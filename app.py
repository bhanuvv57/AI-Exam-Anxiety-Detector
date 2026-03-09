import streamlit as st
from anxiety_model import predict_anxiety
from tips import get_tips

st.title("🧠 AI Exam Anxiety Detector")

st.write("Enter your thoughts before the exam.")

user_input = st.text_area("How are you feeling about your exam?")

if st.button("Analyze Anxiety"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:

        level = predict_anxiety(user_input)
        tips = get_tips(level)

        if level == "High Anxiety":
            st.error(f"Anxiety Level: {level} 😟")

        elif level == "Moderate Anxiety":
            st.warning(f"Anxiety Level: {level} 😐")

        else:
            st.success(f"Anxiety Level: {level} 😊")

        st.subheader("Tips")
        st.write(tips)