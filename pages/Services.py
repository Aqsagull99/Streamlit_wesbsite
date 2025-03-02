import streamlit as st

st.title("💼 Our Services")
services = ["Web Development", "AI & Machine Learning", "UI/UX Design", "Data Analytics"]
for service in services:
    st.subheader(f"✅ {service}")
st.markdown("We provide top-notch services tailored to your needs.")
