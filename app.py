import streamlit as st

st.title("LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.write("Generate a basic legal document using simple inputs.")

name = st.text_input("Enter your name")
address = st.text_input("Enter your address")

document_type = st.selectbox(
    "Select Document Type",
    [
        "Rental Agreement",
        "Employment Agreement",
        "Leave Agreement",
        "Affidavit"
    ]
)

duration = st.text_input("Enter Duration")

if st.button("Generate Document"):

    if name and address and duration:

        document = f"""
LEGAL DOCUMENT
============================

Document Type: {document_type}

Name: {name}
Address: {address}
Duration: {duration}

This document is generated using
LegalEase AI-Powered Legal Document Generator.

This is a basic document template for
educational and project demonstration purposes.

It is not a substitute for professional legal advice.
"""

        st.success("Document generated successfully!")

        st.text_area(
            "Generated Document",
            document,
            height=350
        )

        with open("generated_document.txt", "w") as file:
            file.write(document)

        st.download_button(
            "Download Document",
            document,
            file_name="generated_document.txt"
        )

    else:
        st.warning("Please fill all the details.")