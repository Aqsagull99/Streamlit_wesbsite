import streamlit as st

# ---- Page Configurations ----
st.set_page_config(page_title="Our Services", page_icon="💼", layout="wide")

# ---- Custom CSS for Styling ----
st.markdown("""
    <style>
        /* Background Styling */
        .stApp {
            background: url('https://images.unsplash.com/photo-1522252234503-e356532cafd5') no-repeat center center fixed;
            background-size: cover;
        }

        /* Main Container */
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
            text-align: center;
        }

        /* Title Styling */
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #FFD700;
            margin-bottom: 10px;
        }

        /* Subtitle */
        .subtitle {
            font-size: 22px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 20px;
        }

        /* Service List */
        .service-item {
            font-size: 20px;
            color: white;
            background: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
            font-weight: bold;
            text-align: left;
        }

        /* Hover Effect */
        .service-item:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        /* Description */
        .text {
            font-size: 16px;
            line-height: 1.8;
            color: #cccccc;
            margin-top: 20px;
        }

    </style>
""", unsafe_allow_html=True)

# ---- Services Section ----
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<p class='title'>💼 Our Services</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>We offer top-notch digital solutions tailored to your needs.</p>", unsafe_allow_html=True)

# ---- Service List ----
services = [
    "🌐 Web Development - Build modern, responsive, and dynamic websites.",
    "🤖 AI & Machine Learning - Smart AI solutions for business automation.",
    "🎨 UI/UX Design - Intuitive and user-friendly design experiences.",
    "📊 Data Analytics - Gain insights with powerful data-driven strategies."
]

for service in services:
    st.markdown(f"<div class='service-item'>{service}</div>", unsafe_allow_html=True)

st.markdown("<p class='text'>Let’s turn your vision into reality with our expertise.</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
