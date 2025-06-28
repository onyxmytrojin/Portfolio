import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def img_to_base64(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

def timeline_card(logo_img, org, role, date, desc, location=None):
    logo_b64 = img_to_base64(logo_img)
    col1, col2 = st.columns([1, 8])
    with col1:
        st.markdown(
            f'''
            <div style="display: flex; flex-direction: column; align-items: center; height: 100px; min-width: 60px;">
                <div style="width:2px; height:12px; background:#444a;"></div>
                <img src="data:image/png;base64,{logo_b64}" style="width:48px; height:48px; border-radius:50%; border:3px solid #eee; margin: 0.2rem 0; background:#fff;" />
                <div style="width:2px; flex:1; background:#444a;"></div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(f"<div style='display:flex;justify-content:space-between;align-items:center;'><span style='font-weight:700;font-size:1.1rem'>{org}</span><span style='font-style:italic; color:#888; font-size:1rem'>{date}</span></div>", unsafe_allow_html=True)
        st.markdown(f"<span style='font-style:italic; color:#888; font-size:1rem'>{role}</span>" + (f"<span style='float:right; color:#888; font-size:0.95rem'> {location}</span>" if location else ""), unsafe_allow_html=True)
        st.markdown("<ul style='margin-top:0.5rem;margin-bottom:0.5rem;'>" + ''.join([f"<li style='color:#eee;font-size:0.98rem'>{d}</li>" for d in desc]) + "</ul>", unsafe_allow_html=True)
    st.markdown("<hr style='border: none; border-top: 1px solid #333; margin: 1.5rem 0;'>", unsafe_allow_html=True)

# --- Load Images ---
profile_img = Image.open("mypfp.jpeg")
entrupy_logo = Image.open("entrupy_logo.jpeg")
iitpkd_logo = Image.open("iitpkdlogo.jpeg")
tcs_logo = Image.open("tata_consultancy_services_logo.jpeg")
sjis_logo = Image.open("sjislogo.png")
abps_logo = Image.open("ABPSlogo.png")

# --- Page Config ---
st.set_page_config(page_title="Shubhan Mehrotra Portfolio", page_icon=profile_img, layout="centered")

# --- Modern Custom Navbar (pill style, no radio circles, Streamlit-native navigation) ---
PAGES = ["Home", "Projects", "Skills", "Contact"]
PAGE_URLS = {"Home": "Profile", "Projects": "Projects", "Skills": "Skills", "Contact": "Contact"}

if "page" not in st.session_state:
    st.session_state.page = "Home"

# Remove any extra top margin or empty divs above the navbar
st.markdown("""
<style>
.custom-navbar {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2.5rem;
    background: #181a1b;
    padding: 1.2rem 0 1.2rem 0;
    border-bottom: 1px solid #222;
    border-radius: 0 0 22px 22px;
    margin-bottom: 2.5rem;
    box-shadow: 0 2px 16px 0 rgba(0,0,0,0.08);
}
.custom-navbar .stButton > button {
    background: none;
    border: none;
    color: #bbb;
    font-size: 1.15rem;
    font-weight: 500;
    padding: 0.5em 2.2em;
    border-radius: 18px;
    transition: background 0.2s, color 0.2s, font-weight 0.2s;
    cursor: pointer;
    outline: none;
    margin: 0 0.1em;
}
.custom-navbar .stButton > button.selected {
    background: #23272a;
    color: #fff;
    font-weight: 700;
    box-shadow: 0 2px 8px 0 rgba(0,0,0,0.10);
}
.custom-navbar .stButton > button:hover {
    background: #23272a;
    color: #fff;
}
/* Remove Streamlit's default top blank space */
section[data-testid="stHeader"] { height: 0 !important; min-height: 0 !important; }
header { height: 0 !important; min-height: 0 !important; }
</style>
<div class='custom-navbar'>
""", unsafe_allow_html=True)

nav_cols = st.columns(len(PAGES), gap="small")
for i, p in enumerate(PAGES):
    if nav_cols[i].button(f"{p}", key=f"nav_{p}"):
        st.session_state.page = p
    # Highlight the selected button with JS/CSS
    nav_cols[i].markdown(f"""
    <style>
    div[data-testid="column"]:nth-child({i+1}) .stButton > button {{
        {'background: #23272a; color: #fff; font-weight: 700; box-shadow: 0 2px 8px 0 rgba(0,0,0,0.10);' if st.session_state.page == p else ''}
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

page = PAGE_URLS[st.session_state.page]

# --- Profile Section (now with Timeline tabs) ---
if page == "Profile":
    # Ensure profile image is loaded and visible
    try:
        img_b64 = img_to_base64(profile_img)
        st.markdown(f"""
        <div style='display:flex; flex-direction:column; align-items:center; margin-bottom:1.5em;'>
            <img src="data:image/png;base64,{img_b64}" style="width:140px; height:140px; border-radius:50%; border:3px solid #eee; margin-bottom:1em; box-shadow:0 2px 8px rgba(0,0,0,0.08);" />
            <div style='font-size:2.2rem; font-weight:800; margin-bottom:0.2em; text-align:center;'>Shubhan Mehrotra</div>
            <div style='font-size:1.1rem; color:#888; margin-bottom:0.7em; text-align:center;'>B.Tech. Electrical Engineering<br>Indian Institute Of Technology, Palakkad</div>
            <div style='font-size:1.05rem; margin-bottom:0.3em;'><span style='font-size:1.1em;'>📧</span> <a href='mailto:shubhanmehrotra@gmail.com'>shubhanmehrotra@gmail.com</a></div>
            <div style='font-size:1.05rem; margin-bottom:0.3em;'><span style='font-size:1.1em;'>📱</span> +91-9714957474</div>
            <div style='font-size:1.05rem; margin-bottom:0.3em;'><a href='https://github.com/onyxmytrojin'>GitHub</a> | <a href='https://www.linkedin.com/in/shubhanmehrotra/'>LinkedIn</a></div>
        </div>
        <hr style='margin:1.5em 0;' />
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Profile image could not be loaded: {e}")
    st.header("Timeline")
    tab1, tab2 = st.tabs(["Work", "Education"])
    with tab1:
        work = [
            {
                "logo": entrupy_logo,
                "org": "Entrupy",
                "role": "Software Engineer -1",
                "date": "June 2025 - Ongoing",
                "desc": [
                    "Architected and deployed complex, usage-based billing engines for major clients, culminating in a system , processing over 15,000+ high-volume transactions at scale."
                ]
            },
            {
                "logo": entrupy_logo,
                "org": "Entrupy",
                "role": "Python Developer Intern",
                "date": "October 2024 - May 2025",
                "desc": [
                    "Engineered 5 + feature flags and profile-driven ACLs, replacing rigid role checks in 4 microservices and cutting manual access updates",
                    "Built a dual-category auto-assigned user-profile system with admin UI, halving org/user onboarding time.",
                    "Converted product controls (barcode, fingerprint, sneaker-pricing, JP-user) to toggle-based configs."
                ]
            },
            {
                "logo": tcs_logo,
                "org": "TCS Research",
                "role": "Computing Systems Research Intern",
                "date": "June 2024 - July 2024",
                "desc": [
                    "Curated datasets for efficient RAG-based training on combined LLaMA and Mistral architectures.",
                    "Enhanced utilization metrics, hardware specs, and model data, reducing training time by 27.5 %."
                ],
                "location": "Thane"
            }
        ]
        for job in work:
            timeline_card(
                job["logo"],
                job["org"],
                job["role"],
                job["date"],
                job["desc"],
                job.get("location")
            )
    with tab2:
        edu = [
            {
                "logo": iitpkd_logo,
                "date": "2021 - Present",
                "org": "Indian Institute Of Technology Palakkad",
                "role": "B.Tech. Electrical Engineering",
                "desc": ["CGPA: 7.83 (Current)"]
            },
            {
                "logo": sjis_logo,
                "date": "2021",
                "org": "Satyameva Jayate International School",
                "role": "Senior Secondary",
                "desc": ["Percentage: 90.8%"]
            },
            {
                "logo": abps_logo,
                "date": "2019",
                "org": "Aditya Birla Public School Kovaya",
                "role": "Secondary",
                "desc": ["Percentage: 93.8%"]
            }
        ]
        for ed in edu:
            timeline_card(
                ed["logo"],
                ed["org"],
                ed["role"],
                ed["date"],
                ed["desc"]
            )

# --- Projects Section ---
elif page == "Projects":
    st.header("Projects")
    st.markdown("#### Weather App for Scientists (IIT Palakkad, Sept. 2024 - Ongoing)")
    st.write("- Redesigned and deployed a full-stack weather monitoring application using Django REST and React Native, enabling real-time visualization of meteorological and air quality data for IIT Palakkad.")
    st.write("- Integrated RESTful APIs to fetch and preprocess hourly weather metrics from ground-based sensors, supporting dynamic data rendering and user interaction across mobile platforms.")
    st.markdown("---")
    st.markdown("#### Analyzing Kochi Metro's 5-Year Ridership and Travel Demand Data (IIT Palakkad, Jan. 2024 - May. 2024)")
    st.write("- Standardized over 30 million data points using SQL, ensuring data quality and uniformity.")
    st.write("- Extracted commuting patterns, uncovering insights that boosted ridership by up to 15%.")
    st.markdown("---")
    st.markdown("#### Baby Cry Detection for Health Monitoring using 2D CNN and LSTM (IIT Palakkad, Jan. 2024 - May. 2024)")
    st.write("- Designed and trained 2D CNN and LSTM models to classify baby cries into five categories, achieving 94.57% and 91.47% accuracy, respectively.")
    st.write("- Extracted spectrogram features using Short-Time Fourier Transform (STFT) for efficient audio signal classification.")
    st.markdown("---")
    st.markdown("#### RL-Based Lunar Lander Simulation (IIT Palakkad, Aug. 2023 - Dec. 2023)")
    st.write("- Designed an RL agent in OpenAI to autonomously control a lunar lander, achieving an 85% success rate.")
    st.write("- Optimized simulations, reducing failure rates by 25% and maintaining an average score above 200.")
    st.markdown("---")
    st.markdown("#### Rule Based Chatbot (IIT Palakkad, Jan. 2023 - May. 2023)")
    st.write("- Conceived and launched a rule-based chatbot for basic conversations and music recommendations.")
    st.write("- Administered a database of 50,000 songs and 40 user intents.")

# --- Skills Section ---
elif page == "Skills":
    st.header("Skills")
    st.write("**Programming:** Python, C/C++, TypeScript, SQL, Java")
    st.write("**Databases:** MySQL, PostgreSQL, SQL Server")
    st.write("**Web and Mobile Frameworks:** Django, React Native")
    st.write("**Web Technologies:** JavaScript, HTML5, CSS3, JSON")
    st.write("**Other Technologies:** Arduino, MATLAB, LTSpice, KiCAD, Keil uVision")

# --- Contact Section ---
elif page == "Contact":
    st.header("Contact")
    st.write("📧 [shubhanmehrotra@gmail.com](mailto:shubhanmehrotra@gmail.com)")
    st.write("📱 +91-9714957474")
    st.write("[GitHub](https://github.com/onyxmytrojin) | [LinkedIn](https://www.linkedin.com/in/shubhanmehrotra/)") 