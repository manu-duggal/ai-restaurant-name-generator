import streamlit as st
import langchain_helper

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AI Restaurant Creator 🍽️",
    page_icon="🍴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM DARK THEME STYLING ---
st.markdown("""
    <style>
        .stApp {
            background: #1e1e1e !important;
            color: #fafafa !important;
            font-family: 'Poppins', sans-serif;
        }

        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 700;
            background: linear-gradient(90deg, #FF8E53, #FF6B6B);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }

        .subtitle {
            text-align: center;
            color: #d0d0d0;
            font-size: 1.1rem;
            margin-bottom: 2.5rem;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #121212, #2a2a2a);
            color: #fafafa;
        }

        .sidebar-header {
            text-align: center;
            font-size: 1.3rem;
            font-weight: 600;
            margin-top: 1rem;
            color: #FF8E53;
        }

        .menu-card {
            background-color: #2b2b2b !important;
            padding: 1.4rem 1.7rem;
            border-radius: 16px;
            box-shadow: 0 6px 18px rgba(255, 142, 83, 0.15);
            margin-bottom: 1rem;
            transition: all 0.25s ease-in-out;
            border-left: 6px solid #FF8E53;
        }

        .menu-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 22px rgba(255, 142, 83, 0.25);
        }

        .menu-item {
            font-size: 1.1rem;
            font-weight: 500;
            color: #f0f0f0;
        }

        .section-title {
            font-weight: 600;
            color: #f5f5f5;
            font-size: 1.6rem;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }

        .footer {
            text-align: center;
            margin-top: 3rem;
            font-size: 0.9rem;
            color: #999;
        }

        /* 🔥 FIXED BUTTON STYLING */
        div.stButton > button {
            background: linear-gradient(90deg, #FF8E53, #FF6B6B) !important;
            color: white !important;
            border: none !important;
            padding: 0.6rem 1.2rem !important;
            border-radius: 10px !important;
            font-size: 1rem !important;
            font-weight: 600 !important;
            width: 100% !important;
            transition: 0.2s ease-in-out !important;
            margin-top: 10px !important;
        }

        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 14px rgba(255, 110, 86, 0.4) !important;
        }

    </style>
""", unsafe_allow_html=True)


# --- SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1046/1046784.png", width=90)
st.sidebar.markdown("<div class='sidebar-header'>🍴 AI Menu Creator</div>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown("### 🌍 Choose Cuisine Type")
cuisine = st.sidebar.selectbox(
    "",
    ("American", "Italian", "Indian", "Chinese", "Japanese", "French",
     "Mexican", "Thai", "Spanish", "Greek", "Turkish", "Korean",
     "Vietnamese", "Lebanese", "Mediterranean", "Brazilian", "Moroccan", "British")
)

# --- BEAUTIFUL VISIBLE GENERATE BUTTON ---
generate = st.sidebar.button("Generate Menu")

st.sidebar.markdown("---")
st.sidebar.caption("Built with ❤️ By MD using Streamlit + LangChain")


# --- MAIN CONTENT ---
st.markdown("<h1 class='main-title'>AI Restaurant Name & Menu Generator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Generate creative restaurant names and curated menus powered by AI 🍲</p>", unsafe_allow_html=True)
st.markdown("---")


# --- RUN LLM ONLY WHEN BUTTON IS CLICKED ---
if generate:
    with st.spinner(f"🍳 Cooking up ideas for {cuisine} cuisine..."):
        response = langchain_helper.generate_restaurant_name_and_menu(cuisine)
        st.session_state["response"] = response


# --- DISPLAY SAVED RESULT IF EXISTS ---
if "response" in st.session_state:
    response = st.session_state["response"]

    restaurant_name = response.get('restaurant_name', 'Unnamed Restaurant')
    menu_items = response.get('menu_items', '').split(',')

    # --- Restaurant Section ---
    st.markdown(f"<h2 class='section-title'>🏠 {restaurant_name}</h2>", unsafe_allow_html=True)
    st.caption(f"A sophisticated {cuisine} dining experience, crafted with AI creativity.")

    st.markdown("<h3 class='section-title'>Today's Signature Menu</h3>", unsafe_allow_html=True)

    cols = st.columns(3)
    for i, item in enumerate(menu_items):
        with cols[i % 3]:
            st.markdown(f"""
            <div class='menu-card'>
                <p class='menu-item'>🍽️ {item.strip()}</p>
            </div>
            """, unsafe_allow_html=True)

else:
    st.info("👈 Select a cuisine and click **Generate Menu** to create your AI-powered restaurant.")


# --- FOOTER ---
st.markdown("<div class='footer'>© 2025 AI Restaurant Creator | Crafted with Streamlit 💡</div>", unsafe_allow_html=True)
