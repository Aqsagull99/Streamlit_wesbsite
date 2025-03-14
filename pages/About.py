import streamlit as st

# ---- Page Configurations ----
st.set_page_config(page_title="About Us", page_icon="ℹ️", layout="wide")

# ---- Custom CSS Styling ----
st.markdown("""
    <style>
        body {
            background-color: #000000 !important;
            color: #ffffff !important;
            font-family: 'Arial', sans-serif;
        }
        
        /* Section Styling */
        .container {
            padding: 40px;
            text-align: center;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
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
            color: #ff9800 !important;
            margin-bottom: 20px;
        }

        .text {
            font-size: 16px;
            line-height: 1.8;
            color: #FFD700 !important;
             font-weight: bold;
        }

        /* Contact Section */
        .contact-box {
            background: #222222;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        .contact-info {
            font-size: 18px;
            color: #FFD700;
        }

        .social-icons {
            font-size: 24px;
            color: white;
        }
        
        div.stButton > button {
            background-color: #FFD700;
            color: black;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
            padding: 10px 20px;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #ff9800;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)




# ---- About Us Section ----
st.image("https://i.pinimg.com/736x/b5/85/4b/b5854bfc500b970ab5b575b930e9f0a3.jpg", use_container_width=True)


st.markdown("<p class='title'>Who We Are</p>", unsafe_allow_html=True)
st.markdown("<p class='text'>We are a team of passionate developers, innovators, and strategists committed to building modern web applications. Our goal is to create engaging, user-friendly, and impactful experiences using **Streamlit and AI-driven technologies**.</p>", unsafe_allow_html=True)

st.markdown("<p class='title'>Our Mission</p>", unsafe_allow_html=True)
st.markdown("""
    <ul class='text'>
        <li>🚀 <b>Innovation</b> – Building dynamic, data-driven web applications.</li>
        <li>📊 <b>Analysis</b> – Using AI & Web 3.0 for data insights.</li>
        <li>⚡ <b>Optimization</b> – Crafting seamless user experiences.</li>
    </ul>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---- Contact Section ----

st.markdown("<p class='subtitle'>📬 Get in Touch</p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>📧 Email: aqsa.gull.dev.ai99@gmail.com</p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>🌐 Website: <a href='#' style='color:#FFD700;'>yourwebsite.com</a></p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>📍 Location: Remote & Global</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---- CTA Button ----
st.markdown("<br>", unsafe_allow_html=True)
st.button("📩 Contact Us")






