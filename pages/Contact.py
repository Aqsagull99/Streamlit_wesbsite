import streamlit as st

# ---- Page Configurations ----
st.set_page_config(page_title="Contact Us", page_icon="📩", layout="wide")

# ---- Custom CSS for Styling ----
st.markdown("""
    <style>
        /* Background Gradient */
        .stApp {
            # background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%) !important;
        }

        /* Container Styling */
        .container {
            background: rgba(255, 255, 255, 0.9);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
            text-align: center;
            margin: 20px auto;
            max-width: 800px;
        }

        /* Title Styling */
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #1e3c72;
            margin-bottom: 10px;
        }

        /* Subtitle Styling */
        .subtitle {
            font-size: 20px;
            font-weight: bold;
            color: #2a5298;
            margin-bottom: 20px;
        }

        /* Text Styling */
        .text {
            font-size: 16px;
            line-height: 1.8;
            color: #ff9800;
            margin-bottom: 20px;
        }

        /* Contact Info Styling */
        .contact-info {
            font-size: 18px;
            color:#3a3a3a;
            margin-bottom: 10px;
        }

        /* Social Icons Styling */
        .social-icons {
            font-size: 24px;
            color: #2a5298;
            margin-top: 20px;
        }

        /* Form Input Styling */
        .stTextInput input, .stTextArea textarea {
            background-color: #ffffff !important;
            color: #333333 !important;
            border: 1px solid #cccccc !important;
            border-radius: 5px !important;
            padding: 10px !important;
            width: 100% !important;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #1e3c72 !important;
            color: white !important;
            border-radius: 5px !important;
            padding: 10px 20px !important;
            font-weight: bold !important;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #2a5298 !important;
        }

        /* Link Styling */
        a {
            color: #ff9800 !important;
            text-decoration: none;
            font-weight: bold;
        }

        a:hover {
            color: #2a5298 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Contact Form Section ----
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<p class='title'>📩 Contact Us</p>", unsafe_allow_html=True)
st.markdown("<p class='text'>Have questions or want to collaborate? Fill out the form below, and we’ll get back to you soon!</p>", unsafe_allow_html=True)

# ---- Form Inputs ----
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
message = st.text_area("Your Message")

if st.button("Submit"):
    st.success("✅ Thank you! We will get back to you soon.")

st.markdown("</div>", unsafe_allow_html=True)

# ---- Contact Information ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>📞 Contact Info</p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>📧 Email: contact@yourwebsite.com</p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>🔗 LinkedIn: <a href='https://linkedin.com/in/yourprofile'>Your LinkedIn Profile</a></p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>🌍 Website: <a href='https://yourwebsite.com'>yourwebsite.com</a></p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)




