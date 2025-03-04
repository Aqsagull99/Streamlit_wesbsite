import streamlit as st

# ---- Page Configurations ----
st.set_page_config(page_title="About Us", page_icon="ℹ️", layout="wide")

# ---- Custom CSS Styling ----
st.markdown("""
    <style>
        /* Background Styling */
        .stApp {
            # background-color: #111111;
            color: white;
        #  background-image: url("https://i.pinimg.com/736x/fe/59/bb/fe59bbf15c4bbfbef93f238661a0f536.jpg");
        # background-size: cover;
        # background-attachment: fixed;
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
            # color: #cccccc;
            color: #000000 !important;  /* Pure Black */
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
        .button{
        background: #222222;
        }
    </style>
""", unsafe_allow_html=True)




# ---- About Us Section ----
st.image("https://i.pinimg.com/736x/b5/85/4b/b5854bfc500b970ab5b575b930e9f0a3.jpg", use_container_width=True)

# st.markdown("<div class='container'>", unsafe_allow_html=True)

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
st.markdown("<p class='contact-info'>📧 Email: contact@yourwebsite.com</p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>🌐 Website: <a href='#' style='color:#FFD700;'>yourwebsite.com</a></p>", unsafe_allow_html=True)
st.markdown("<p class='contact-info'>📍 Location: Remote & Global</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---- CTA Button ----
st.markdown("<br>", unsafe_allow_html=True)
st.button("📩 Contact Us")




