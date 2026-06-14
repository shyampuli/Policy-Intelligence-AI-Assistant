import streamlit as st
from utils.pdf_reader import extract_text

st.title("Policy Comparison Assistant")

old_pdf = st.file_uploader(
    "Upload Old Policy PDF",
    type=["pdf"]
)

new_pdf = st.file_uploader(
    "Upload New Policy PDF",
    type=["pdf"]
)

if old_pdf:
    st.success("Old Policy Uploaded")

if new_pdf:
    st.success("New Policy Uploaded")

if old_pdf:

    with open("old_policy.pdf","wb") as f:
        f.write(old_pdf.read())

    st.success("Old Policy Saved")
if old_pdf:

    text = extract_text("old_policy.pdf")

    st.subheader("Extracted Text")

    st.text(text[:3000])