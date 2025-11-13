import streamlit as st
import langchain_helper

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AI Restaurant Creator 🍽️",
    page_icon="🍴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================================================
#      🌅 SUNSET GOLD MICHELIN UI — FINAL CLEAN BUILD
# ===========================================================

st.markdown("""
<style>

    /* ---------------- GLOBAL BACKGROUND ---------------- */
    .stApp {
        background: radial-gradient(
            circle at 20% 20%,
            #3b1e0d 0%,
            #1b1918 45%,
            #121111 85%
        ) !important;
        font-family: 'Poppins', sans-serif;
        color: #f5f5f5;
    }

    .stApp:before {
        content: "";
        position: fixed;
        inset: 0;
        background: linear-gradient(
            130deg,
            rgba(255,138,55,0.10),
            rgba(180,55,28,0.06),
            rgba(255,180,120,0.07)
        );
        pointer-events: none;
        z-index: -1;
    }

    /* ======================================================= */
    /*      SIDEBAR GOLD-GLASS PANEL                           */
    /* ======================================================= */
    [data-testid="stSidebar"] > div:first-child {
        margin: 14px;
        padding: 26px;
        border-radius: 22px;
        background: linear-gradient(
            145deg,
            rgba(255,225,185,0.13),
            rgba(255,175,105,0.10),
            rgba(255,145,70,0.08)
        );
        border: 1px solid rgba(255,190,125,0.28);
        box-shadow:
            0 8px 28px rgba(0,0,0,0.50),
            inset 0 0 25px rgba(255,140,65,0.08);
        backdrop-filter: blur(22px);
    }

    /* ======================================================= */
    /*        SIDEBAR TITLE SHIMMER                            */
    /* ======================================================= */

    .sidebar-header {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.2rem;
        font-weight: 700;
        letter-spacing: 1.4px;
        text-align: center;

        background: linear-gradient(
            90deg,
            #fff3e2 0%,
            #ffd9a6 35%,
            #ffb870 65%,
            #ffcc96 100%
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        text-shadow:
            0 0 10px rgba(255,215,160,0.55),
            0 0 16px rgba(255,170,90,0.35),
            0 0 32px rgba(255,150,70,0.25);

        animation: shimmer 4.5s ease-in-out infinite alternate;
    }

    @keyframes shimmer {
        0% { filter: drop-shadow(0 0 2px rgba(255,180,120,0.25)); }
        100% { filter: drop-shadow(0 0 8px rgba(255,200,140,0.55)); }
    }

    .sidebar-divider {
        width: 80%;
        height: 2px;
        margin: 12px auto 26px auto;
        background: linear-gradient(90deg, #ffe6c0, #ffc185, #ff9445);
        border-radius: 3px;
    }

    /* ======================================================= */
    /*       SELECT BOX                                        */
    /* ======================================================= */

    .stSelectbox > div > div {
        background: rgba(255,245,230,0.07) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255,195,125,0.32) !important;
        transition: 0.25s ease;
        box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    }

    .stSelectbox > div > div:hover {
        border-color: #ff9d4d !important;
        box-shadow: 0 0 18px rgba(255,150,80,0.55);
    }

    label[data-testid="stWidgetLabel"] {
        font-family: 'Cormorant Garamond', serif !important;
        font-size: 1.15rem !important;
        color: #ffe7c7 !important;
    }

    /* ======================================================= */
    /*       GENERATE BUTTON (ROUNDED + HOVER)                 */
    /* ======================================================= */

    [data-testid="stSidebar"] div.stButton > button {
        width: 100% !important;
        background: linear-gradient(90deg, #ffc47a, #ff8e48, #d95d25) !important;
        border: none !important;
        border-radius: 18px !important;
        color: white !important;
        font-size: 1.07rem !important;
        font-weight: 700 !important;
        padding: 0.72rem 1.2rem !important;
        box-shadow: 0 6px 18px rgba(255,125,45,0.48);
        transition: 0.25s ease-in-out !important;
    }

    [data-testid="stSidebar"] div.stButton > button:hover {
        transform: translateY(-4px);
        box-shadow:
            0 10px 26px rgba(255,150,75,0.55),
            0 0 12px rgba(255,180,120,0.45);
        filter: brightness(1.15);
    }

    [data-testid="stSidebar"] div.stButton > button:active {
        transform: translateY(2px) scale(0.96);
    }

    /* ======================================================= */
    /*       MAIN CONTENT TITLES                               */
    /* ======================================================= */

    .main-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ffd7a6, #ff9a57, #d95725);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        color: #e6cbb9;
        font-size: 1.18rem;
        margin-bottom: 2.7rem;
    }

    .chef-caption {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.30rem;
        font-style: italic;
        background: linear-gradient(90deg, #ffe8c9, #ffc488, #ff9b48);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 12px;
    }

    .caption-divider {
        width: 135px;
        height: 2px;
        background: linear-gradient(90deg, #ffe2bb, #ff9944);
        border-radius: 2px;
        margin-bottom: 28px;
    }

    .restaurant-name {
        font-family: 'Cormorant Garamond', serif;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #ffe5c4, #ffb974, #ff9342);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .restaurant-underline {
        width: 220px;
        height: 3px;
        background: linear-gradient(90deg, #ffe5b8, #ff9d4b);
        border-radius: 3px;
        margin-bottom: 32px;
    }

    .signature-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: 2.2rem;
        font-weight: 600;
        background: linear-gradient(90deg, #ffe7c8, #ffc489, #ff9d4a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .signature-underline {
        width: 180px;
        height: 2px;
        background: linear-gradient(90deg, #ffe9c9, #ffb476, #ff8a37);
        margin-bottom: 28px;
    }

    /* ======================================================= */
    /*    RESTORED MENU CARD HOVER EFFECT (UNCHANGED)          */
    /* ======================================================= */

    .menu-card {
        background: rgba(255,255,255,0.06) !important;
        border-radius: 16px;
        padding: 1.35rem;
        margin-bottom: 1.6rem;
        border: 1px solid rgba(255,150,70,0.22);
        box-shadow: 0 10px 30px rgba(0,0,0,0.38);
        backdrop-filter: blur(14px);
        transition: all 0.28s ease;
    }

    .menu-card:hover {
        transform: translateY(-6px) scale(1.015);
        box-shadow:
            0 16px 42px rgba(255,160,90,0.38),
            0 0 16px rgba(255,150,80,0.25);
    }

    .menu-item {
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.18rem;
        letter-spacing: 0.2px;
        line-height: 1.25;
        background: linear-gradient(90deg, #ffead0, #ffc994, #ff9b47);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .footer {
        margin-top: 3rem;
        font-size: 0.9rem;
        text-align: center;
        color: #cda88e;
    }

</style>
""", unsafe_allow_html=True)



# ===========================================================
#                          SIDEBAR
# ===========================================================

st.sidebar.markdown("<div class='sidebar-header'>AI Menu Creator</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

cuisine = st.sidebar.selectbox(
    "",
    ("American","Italian","Indian","Chinese","Japanese","French","Mexican",
     "Thai","Spanish","Greek","Turkish","Korean","Vietnamese","Lebanese",
     "Mediterranean","Brazilian","Moroccan","British")
)

generate = st.sidebar.button("Generate Menu")


st.sidebar.markdown(
    "<p style='text-align:center; margin-top:2rem; color:#e67300; font-size:0.95rem;'>"
    "Built with ❤️ By MD using Streamlit + LangChain"
    "</p>",
    unsafe_allow_html=True
)



# ===========================================================
#                       MAIN CONTENT
# ===========================================================

st.markdown("<h1 class='main-title'>AI Restaurant Name & Menu Generator</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Crafting warm, elegant restaurant concepts with Michelin-grade finesse.</p>", unsafe_allow_html=True)

if generate:
    with st.spinner(f"🍳 Creating {cuisine} inspirations..."):
        st.session_state.response = langchain_helper.generate_restaurant_name_and_menu(cuisine)


if "response" in st.session_state:

    restaurant_name = st.session_state.response["restaurant_name"]
    menu_items = [item.strip() for item in st.session_state.response["menu_items"].split(",")]

    st.markdown(f"<div class='restaurant-name'>{restaurant_name}</div>", unsafe_allow_html=True)
    st.markdown("<div class='restaurant-underline'></div>", unsafe_allow_html=True)

    st.markdown(
        f"<p class='chef-caption'>A signature {cuisine} culinary identity, shaped with AI artistry.</p>",
        unsafe_allow_html=True
    )
    st.markdown("<div class='caption-divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='signature-title'>Signature Menu</div>", unsafe_allow_html=True)
    st.markdown("<div class='signature-underline'></div>", unsafe_allow_html=True)

    cols = st.columns(3)

    for i, item in enumerate(menu_items):
        with cols[i % 3]:
            st.markdown(
                f"<div class='menu-card'><p class='menu-item'>{item}</p></div>",
                unsafe_allow_html=True
            )

else:
    st.info("👈 Select a cuisine and click **Generate Menu** to begin.")


st.markdown("<div class='footer'>© 2025 AI Restaurant Creator | Michelin Edition 🌅</div>", unsafe_allow_html=True)
