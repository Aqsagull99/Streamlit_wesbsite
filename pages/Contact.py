import streamlit as st

st.title("📩 Contact Us")
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
message = st.text_area("Your Message")

if st.button("Submit"):
    st.success("Thank you! We will get back to you soon.")




