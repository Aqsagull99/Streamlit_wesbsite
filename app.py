# import streamlit as st
# import random

# # ---- Page Configurations ----
# st.set_page_config(page_title="My Website", page_icon="🌍", layout="wide")

# # ---- Custom CSS for Background Image & Theme ----
# st.markdown("""
#     <style>
#     /* Background Image */
#     .stApp {
#         background-image: url("https://i.pinimg.com/736x/fe/59/bb/fe59bbf15c4bbfbef93f238661a0f536.jpg");
#         background-size: cover;
#         background-attachment: fixed;
#     }
    
#     /* Custom Fonts & Colors */
#     h1, h2, h3, p, .stTextInput label, .stButton, .stMetric {
#         color: #fff !important;
#     }
    
#     /* Search Bar Styling */
#     .search-box {
#         background: rgba(255, 255, 255, 0.2);
#         border-radius: 10px;
#         padding: 10px;
#         text-align: center;
#     }
    
#     .stTextInput input {
#         background-color: rgba(255, 255, 255, 0.7) !important;
#         color: black !important;
#         border-radius: 5px;
#     }
    
#     /* Center Align Elements */
#     .center-text {
#         text-align: center;
#     }
    
#     /* Custom Button */
#     .stButton button {
#         background-color: #ff9800 !important;
#         color: white !important;
#         border-radius: 8px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # ---- Sidebar Navigation ----
# st.sidebar.title("🌟 Navigation")

# pages = {
#     "About Us": "pages/About.py",
#     "Services": "pages/Services.py",
#     "Gallery": "pages/Gallery.py",
#     "Contact Us": "pages/Contact.py"
# }

# for label, page in pages.items():
#     st.sidebar.page_link(page, label=f"🔹 {label}")

# # ---- Search Bar for Navigation ----
# st.sidebar.markdown("<div class='search-box'>🔎 **Search Navigation**</div>", unsafe_allow_html=True)
# search = st.sidebar.text_input("Search pages...")

# if search:
#     matched_pages = [label for label in pages if search.lower() in label.lower()]
#     if matched_pages:
#         st.sidebar.write("🔍 **Results:**")
#         for page in matched_pages:
#             st.sidebar.page_link(pages[page], label=f"🔹 {page}")
#     else:
#         st.sidebar.write("❌ No results found.")

# # ---- Header Section ----
# st.markdown("<h1 class='center-text'>🚀 Welcome to My Website</h1>", unsafe_allow_html=True)
# st.markdown("<h3 class='center-text'>Explore different sections using the sidebar menu.</h3>", unsafe_allow_html=True)
# st.image("https://source.unsplash.com/random/1200x500", use_container_width=True)

# # ---- Embedded YouTube Video ----
# st.video("https://www.youtube.com/watch?v=your_video_id")

# # ---- Live Visitors Count ----
# visitors = random.randint(100, 500)
# st.metric(label="🌍 Live Visitors", value=visitors)

# # ---- Live News or Blog Section ----
# st.write("## 📰 Latest News & Blog Updates")
# blog_col1, blog_col2 = st.columns(2)

# with blog_col1:
#     st.image("https://source.unsplash.com/300x200/?technology", width=300)
#     st.write("🔹 **AI is Revolutionizing the World!**")
#     st.write("AI and Web 3.0 are reshaping the future. [Read more](#)")

# with blog_col2:
#     st.image("https://source.unsplash.com/300x200/?business", width=300)
#     st.write("🔹 **5 Tips to Become a Pro Developer**")
#     st.write("Master coding with these 5 simple steps. [Read more](#)")

# # ---- Newsletter Subscription ----
# st.write("📩 **Subscribe to Our Newsletter:**")
# email = st.text_input("Enter your email for updates:")
# if st.button("Subscribe"):
#     st.success("🎉 Thank you for subscribing!")

# # ---- Team Members Showcase ----
# st.write("## Meet Our Team 👨‍💻👩‍💻")
# col1, col2 = st.columns(2)
# with col1:
#     st.image("https://source.unsplash.com/150x150/?person,developer", width=150)
#     st.write("🚀 **Aqsa Gull** - Founder & Developer")
# with col2:
#     st.image("https://source.unsplash.com/150x150/?person,technology", width=150)
#     st.write("🌟 **John Doe** - AI Expert")

# # ---- Fun Easter Egg - Surprise Balloons ----
# if st.button("Click for a Surprise! 🎁"):
#     st.balloons()






import streamlit as st
import random

# ---- Page Configurations ----
st.set_page_config(page_title="My Website", page_icon="🌍", layout="wide")

# ---- Custom CSS for Background Image & Theme ----
st.markdown("""
    <style>
    /* Background Image */
    .stApp {
        background-image: url("https://i.pinimg.com/736x/fe/59/bb/fe59bbf15c4bbfbef93f238661a0f536.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* Text Colors & Styling */
    h1, h2, h3, p, label, .stMetric {
        color: #000000 !important;  /* Pure Black */
        font-weight: bold;
    }

    /* Search Box Styling */
    .search-box {
        background: rgba(255, 255, 255, 0.9); /* Light background */
        border-radius: 10px;
        padding: 10px;
        text-align: center;
    }
    
    /* Input Fields */
    .stTextInput input {
        background-color: #ffffff !important;
        color: black !important;
        font-weight: bold;
        border-radius: 5px;
    }
    
    /* Buttons */
    .stButton button {
        # background-color: #1a73e8 !important; /* Blue */
        # color: white !important;
        background-color: #ff9800 !important;
        color: white !important;
        border-radius: 8px;
        font-weight: bold;
        border-radius: 8px;
    }
    
    /* Sidebar Styling */
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        color: #000000;
    }
    
    /* Center Align Text */
    .center-text {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Sidebar Navigation ----
st.sidebar.markdown("<p class='sidebar-title'>📌 Navigation</p>", unsafe_allow_html=True)

pages = {
    "📜 About Us": "pages/About.py",
    "💼 Services": "pages/Services.py",
    "🖼 Gallery": "pages/Gallery.py",
    "📩 Contact Us": "pages/Contact.py"
}

for label, page in pages.items():
    st.sidebar.page_link(page, label=label)

# ---- Search Bar for Navigation ----
st.sidebar.markdown("<div class='search-box'><strong>🔍 Search Navigation</strong></div>", unsafe_allow_html=True)
search = st.sidebar.text_input("Search pages...")

if search:
    matched_pages = [label for label in pages if search.lower() in label.lower()]
    if matched_pages:
        st.sidebar.markdown("**🔍 Results:**")
        for page in matched_pages:
            st.sidebar.page_link(pages[page], label=page)
    else:
        st.sidebar.write("❌ No results found.")

# ---- Header Section ----
st.markdown("<h1 class='center-text'>🚀 Welcome to My Website</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='center-text'>Explore different sections using the sidebar menu.</h3>", unsafe_allow_html=True)
st.image("https://source.unsplash.com/random/1200x500", use_container_width=True)

# ---- Embedded YouTube Video ----
st.video("https://www.youtube.com/watch?v=your_video_id")

# ---- Live Visitors Count ----
visitors = random.randint(100, 500)
st.metric(label="🌍 Live Visitors", value=visitors)

# ---- Live News or Blog Section ----
st.write("## 📰 Latest News & Blog Updates")
blog_col1, blog_col2 = st.columns(2)

with blog_col1:
    st.image("https://source.unsplash.com/300x200/?technology", width=300)
    st.write("**📡 AI is Revolutionizing the World!**")
    st.write("AI and Web 3.0 are reshaping the future. [Read more](#)")

with blog_col2:
    st.image("https://source.unsplash.com/300x200/?business", width=300)
    st.write("**💻 5 Tips to Become a Pro Developer**")
    st.write("Master coding with these 5 simple steps. [Read more](#)")

# ---- Newsletter Subscription ----
st.write("📩 **Subscribe to Our Newsletter:**")
email = st.text_input("Enter your email for updates:")
if st.button("Subscribe"):
    st.success("🎉 Thank you for subscribing!")

# ---- Team Members Showcase ----
st.write("## 👨‍💻 Meet Our Team 👩‍💻")
col1, col2 = st.columns(2)
with col1:
    st.image("https://source.unsplash.com/150x150/?person,developer", width=150)
    st.write("**🚀 Aqsa Gull** - Founder & Developer")
with col2:
    st.image("https://source.unsplash.com/150x150/?person,technology", width=150)
    st.write("**🌟 John Doe** - AI Expert")

# ---- Fun Easter Egg - Surprise Balloons ----
if st.button("Click for a Surprise! 🎁"):
    st.balloons()







