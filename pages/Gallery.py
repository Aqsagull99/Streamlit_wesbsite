import streamlit as st

# ---- Page Configurations ----
st.set_page_config(page_title="My Gallery", page_icon="🖼", layout="wide")

# ---- Custom CSS for Better UI ----
st.markdown("""
    <style>
        /* Fullscreen Background Styling */
        body {
            background-color: #000000 !important;
            color: #ffffff !important;
            font-family: 'Arial', sans-serif;
        }

        /* Gallery Container */
        .gallery-container {
            background: #000000;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin: auto;
            width: 90%;
        }

        /* Title Styling */
        .title {
            font-size: 50px !important;
            font-weight: bold;
            color: #000000;
            margin-bottom:20px;
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.2);
        }

        /* Heading at the Top */
        .gallery-heading {
            font-size: 300px;
            font-weight: bold;
            color: #000000;
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 3px 3px 6px rgba(255, 255, 255, 0.3);
        }

        /* Image Grid */
        .image-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px; /* Increased gap for vertical spacing */
            justify-content: center;
            padding: 20px;
        }

        /* Image Styling */
        .gallery-img {
            width: 100%;
            height: 300px;
            object-fit: cover;
            border-radius: 10px;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            filter: grayscale(100%);
            margin-top: 100px;
            
        }

        .gallery-img:hover {
            transform: scale(1.05);
            box-shadow: 0px 10px 20px rgba(255, 255, 255, 0.3);
            filter: grayscale(0%);
        }
    </style>
""", unsafe_allow_html=True)

# ---- Gallery Section ----
# st.markdown("<p class='gallery-heading'> Welcome to My Gallery </p>", unsafe_allow_html=True)
# st.markdown("<div class='gallery-container'>", unsafe_allow_html=True)
st.markdown("<p class='title'>🖼 My Gallery</p>", unsafe_allow_html=True)

# ---- Updated Image List (High-Quality Pexels Images) ----
image_urls = [
    "https://images.pexels.com/photos/3225517/pexels-photo-3225517.jpeg",  # Black and white cityscape
    "https://images.pexels.com/photos/325185/pexels-photo-325185.jpeg",    # Black and white mountain
    "https://images.pexels.com/photos/417074/pexels-photo-417074.jpeg",   # Black and white forest
    "https://images.pexels.com/photos/2387873/pexels-photo-2387873.jpeg", # Black and white portrait
    "https://images.pexels.com/photos/1323550/pexels-photo-1323550.jpeg", # Black and white architecture
    "https://images.pexels.com/photos/3408744/pexels-photo-3408744.jpeg", # Black and white winter
    "https://images.pexels.com/photos/3617500/pexels-photo-3617500.jpeg",  # Black and white street
    "https://images.pexels.com/photos/417192/pexels-photo-417192.jpeg",   # Black and white ocean
]

# ---- Display Images in Grid ----
st.markdown("<div class='image-grid'>", unsafe_allow_html=True)
for img_url in image_urls:
    st.markdown(f"<img class='gallery-img' src='{img_url}' alt='Gallery Image'>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)







