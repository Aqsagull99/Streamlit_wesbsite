import streamlit as st

# ---- Page Configurations ----
st.set_page_config(page_title="Contact Us", page_icon="📩", layout="wide")

# ---- Custom CSS for Styling ----
st.markdown("""
    <style>
        /* Background Image */
        .stApp {
            background: url('https://i.pinimg.com/736x/fe/59/bb/fe59bbf15c4bbfbef93f238661a0f536.jpg') 
            no-repeat center center fixed;
            background-size: cover;
            background color:white;
        }

        /* Container Styling */
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
            text-align: center;
        }

        .title {
            font-size: 36px;
            font-weight: bold;
            color: #FFD700;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 20px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 20px;
        }

        .text {
            font-size: 16px;
            line-height: 1.8;
            # color: #cccccc;
            color: #000000 !important;  /* Pure Black */
            font-weight: bold;
        }

        .contact-info {
            font-size: 18px;
            color: #FFD700;
        }

        .social-icons {
            font-size: 24px;
            color: white;
        }

        /* Form Styling */
        .stTextInput input,.stTextArea textarea {
             background-color: #222222 !important;
              color: white !important;
            border-radius: 5px !important;
            padding: 10px !important;
        }

        .stButton>button {
            background-color: #FFD700 !important;
            color: black !important;
            border-radius: 5px !important;
            padding: 10px 20px !important;
            font-weight: bold !important;
            cursor: pointer;
        }
        
        .stButton>button:hover {
            background-color: #ffcc00 !important;
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
st.markdown("<p class='contact-info'>🔗 LinkedIn: <a href='https://linkedin.com/in/yourprofile' style='color:#FFD700;'>Your LinkedIn Profile</a></p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>🌍 Website: <a href='https://yourwebsite.com' style='color:#FFD700;'>yourwebsite.com</a></p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

