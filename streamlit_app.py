import streamlit as st
from utils import extract_text
from generator import generate_content

st.set_page_config(page_title="AI Trainer Assistant")

st.title("📚 AI Trainer Assistant")

st.write("Upload course material to generate MCQs, assignments, and case studies.")

uploaded_file = st.file_uploader(
    "Upload file",
    type=["pdf","docx","txt"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    st.success("Material uploaded successfully!")

    if st.button("Generate MCQs"):
        result = generate_content(text,"10 multiple choice questions with answers")
        st.write(result)

    if st.button("Generate Assignment"):
        result = generate_content(text,"5 assignment questions")
        st.write(result)

    if st.button("Generate Case Study"):
        result = generate_content(text,"2 case studies with questions")
        st.write(result)