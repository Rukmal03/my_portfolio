import streamlit as st
import os

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Rukmal Manoj | Portfolio",
    page_icon="₄:₂₀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------- GLOBAL STYLING -----------------
st.markdown("""
    <!-- Load FontAwesome Icon Library -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
    /* Global Page Styling */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #d5d1d4 !important;
        color: #111111 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        min-height: 100vh !important;
    }

    /* Main Container Padding */
    [data-testid="stMainBlockContainer"] {
        padding-top: 4.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 1000px !important;
        margin: 0 auto !important;
    }

    /* Text Readability */
    p, span, label, h1, h2, h3, h4, h5, h6, div, a {
        opacity: 1 !important;
        color: #111111 !important;
    }

    /* Hide Sidebar Collapse Button */
    [data-testid="stSidebarCollapseButton"] { display: none !important; }

    /* NAVIGATION BAR CONTAINER */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] {
        display: flex !important;
        justify-content: center !important;
        gap: 12px !important;
        flex-wrap: wrap !important;
        margin-top: 0.5rem !important;
        margin-bottom: 0rem !important;
        padding-bottom: 10px !important;
    }

    /* Remove Default Streamlit Radio Indicators */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label > div:first-child,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label svg,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label input,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] [data-aria-hidden="true"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
    }

    /* COMPLETELY REMOVE STREAMLIT DEFAULT ORANGE HIGHLIGHTS / ACCENTS */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] *,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label *,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] input,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] div {
        outline: none !important;
        box-shadow: none !important;
        -webkit-tap-highlight-color: transparent !important;
        accent-color: #000000 !important;
        border-color: rgba(150, 150, 150, 0.8);
    }

    /* BASE TAB ANIMATED STYLING */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label {
        position: relative !important;
        background-color: rgba(255, 255, 255, 0.75) !important;
        border: 1px solid rgba(150, 150, 150, 0.8) !important;
        border-radius: 12px !important;
        padding: 9px 20px !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05) !important;
        user-select: none !important;
    }

    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label p {
        font-size: 0.9rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
        transition: color 0.3s ease !important;
        color: #111111 !important;
    }

    /* TAB HOVER ANIMATION */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label:hover {
        background-color: #ffffff !important;
        border-color: #333333 !important;
        transform: translateY(-4px) !important;
        box-shadow: 0 8px 18px rgba(0, 0, 0, 0.12) !important;
    }

    /* TAB CLICK / PRESS ANIMATION */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label:active {
        transform: translateY(-1px) scale(0.97) !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08) !important;
        transition: transform 0.1s ease !important;
    }

    /* ACTIVE / SELECTED TAB STATE (BLACK BORDER & WHITE BG, NO ORANGE) */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label[data-checked="true"],
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label[aria-checked="true"],
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label[aria-selected="true"] {
        background-color: #ffffff !important;
        border-color: #000000 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15) !important;
    }

    /* PREVENT FOCUS-VISIBLE ORANGE RINGS IN STREAMLIT */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label:focus,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label:focus-within,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label:focus-visible,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] [data-baseweb="radio"] {
        outline: none !important;
        border-color: #000000 !important;
    }

    .nav-divider {
        width: 100%;
        height: 1px;
        background-color: #888888;
        margin-top: 0.2rem;
        margin-bottom: 1.8rem;
    }

    /* EDITORIAL CONTENT STYLES */
    .editorial-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 800 !important;
        margin-bottom: 1rem;
    }

    .editorial-bio {
        text-align: center;
        font-size: 1rem;
        line-height: 1.6;
        font-weight: 500 !important;
        max-width: 800px;
        margin: 0 auto 1.5rem auto;
    }

    .editorial-divider {
        width: 100px;
        height: 1px;
        background-color: #666666;
        margin: 0 auto 1.5rem auto;
    }

    .name-badge {
        background-color: #ffffff;
        color: #000000 !important;
        padding: 8px 20px;
        font-size: 0.9rem;
        font-weight: 800;
        letter-spacing: 2px;
        border: 1px solid #888888;
        text-transform: uppercase;
        margin-top: -15px;
        z-index: 10;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }

    .social-icons-container {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 18px;
    }

    .social-icon-link {
        color: #333333 !important;
        font-size: 1.2rem;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background-color: rgba(255, 255, 255, 0.6);
        border: 1px solid rgba(150, 150, 150, 0.5);
        transition: all 0.3s ease;
        text-decoration: none !important;
    }

    .social-icon-link:hover {
        color: #ffffff !important;
        background-color: #111111 !important;
        transform: translateY(-2px);
    }

    /* ----------------- HOMIES SYMBOLS ANIMATION ----------------- */
    .homie-symbol {
        display: inline-block;
        font-size: 1.5rem;
        margin: 0 3px;
        animation: homieBounce 1.8s infinite ease-in-out;
        transition: all 0.3s ease;
    }

    .h1 { animation-delay: 0.0s; }
    .h2 { animation-delay: 0.2s; }
    .h3 { animation-delay: 0.4s; }
    .h4 { animation-delay: 0.6s; }

    @keyframes homieBounce {
        0%, 100% {
            transform: translateY(0px) rotate(0deg) scale(1);
        }
        30% {
            transform: translateY(-8px) rotate(-10deg) scale(1.2);
        }
        60% {
            transform: translateY(2px) rotate(10deg) scale(1.05);
        }
    }

    /* ----------------- PLAYSTATION SYMBOLS ANIMATION ----------------- */
    .ps-symbol {
        display: inline-block;
        font-weight: 900;
        font-size: 1.6rem;
        margin: 0 2px;
        animation: psWave 2s infinite ease-in-out;
        transition: all 0.3s ease;
    }

    /* Playstation Iconic Colors */
    .ps-triangle { color: #2ecc71 !important; animation-delay: 0.0s; } /* Green */
    .ps-circle   { color: #e74c3c !important; animation-delay: 0.2s; } /* Red */
    .ps-cross    { color: #3498db !important; animation-delay: 0.4s; } /* Blue */
    .ps-square   { color: #e84393 !important; animation-delay: 0.6s; } /* Pink */

    @keyframes psWave {
        0%, 100% {
            transform: translateY(0px) scale(1);
            filter: drop-shadow(0 0 0px transparent);
        }
        50% {
            transform: translateY(-6px) scale(1.2);
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.25));
        }
    }

    /* Mobile View Adjustments */
    @media (max-width: 600px) {
        [data-testid="stMainBlockContainer"] {
            padding-top: 3.5rem !important;
        }
        [data-testid="stMainBlockContainer"] [role="radiogroup"] > label {
            padding: 6px 12px !important;
        }
        [data-testid="stMainBlockContainer"] [role="radiogroup"] > label p {
            font-size: 0.8rem !important;
        }
        .ps-symbol, .homie-symbol {
            font-size: 1.3rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- TOP NAVIGATION BAR -----------------
page = st.radio(
    "Navigation",
    [" 🏠︎ Home", " 📽 What IF", " ☣︎ Game Plays", " ✉ Contact Details"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)

# ----------------- PAGE ROUTING -----------------
if page.endswith("Home"):
    st.markdown('<div class="editorial-title">About Me</div>',
                unsafe_allow_html=True)

    st.markdown(
        """
        <div class="editorial-bio">
            Hi, I'm Rukmal Manoj.<br>
            Technology and an endless curiosity for the unknown are major parts of my life. 
            As a BIS undergraduate at the University of Sri Jayewardenepura, 
            my academic world revolves around software, data, and management. 
            As an Agnostic who views any idea with an open mind, I love learning new things, 
            finding calm through music, and seeking to understand the true nature of the universe. 
            Ultimately, my hope is to lead a simple and peaceful life, 
            while remaining eager to exchange new ideas and work together with others. &nbsp;&nbsp;✌︎︎ ₄:₂₀
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="editorial-divider"></div>',
                unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        image_path = "rukmal.jpg"
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.info("💡 Place `rukmal.jpg` in your project directory.")

        st.markdown(
            '<div style="display:flex; justify-content:center;"><div class="name-badge">Rukmal Manoj</div></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="social-icons-container">
                <a href="https://instagram.com" target="_blank" class="social-icon-link" title="Instagram"><i class="fab fa-instagram"></i></a>
                <a href="https://www.youtube.com/channel/UCzpd_QGX_KvvpwS0SewgtnA" target="_blank" class="social-icon-link" title="YouTube"><i class="fab fa-youtube"></i></a>
                <a href="https://www.linkedin.com/in/rukmal-manoj-1a47a7376" target="_blank" class="social-icon-link" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                <a href="https://github.com/Rukmal03" target="_blank" class="social-icon-link" title="GitHub"><i class="fab fa-github"></i></a>
            </div>
            """,
            unsafe_allow_html=True
        )

elif page.endswith("What IF"):
    st.title("What IF")

    # Animated Homies Greeting
    st.markdown(
        """
        <div style="font-size: 1.15rem; font-weight: 600; margin-bottom: 1rem; display: flex; align-items: center; gap: 8px;">
            <span>Welcome Homies...</span>
            <span style="display: inline-flex; align-items: center;">
                <span class="homie-symbol h1">𐦂</span>
                <span class="homie-symbol h2">𖨆</span>
                <span class="homie-symbol h3">𐀪</span>
                <span class="homie-symbol h4">𖠋</span>
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Featured Projects ↻ ◁ || ▷ ↺ ⩇⩇:⩇⩇")
    st.info("Portfolio showcase pending.")

elif page.endswith("Game Plays"):
    # Animated Title with Playstation Icons
    st.markdown(
        """
        <h1 style="display: flex; align-items: center; gap: 15px; flex-wrap: wrap;">
            <span>Game Plays</span>
            <span style="display: inline-flex; align-items: center; gap: 4px;">
                <span class="ps-symbol ps-triangle">△</span>
                <span class="ps-symbol ps-circle">○</span>
                <span class="ps-symbol ps-cross">⛌</span>
                <span class="ps-symbol ps-square">□</span>
            </span>
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.write("Game Plays By **@lbedo**.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ghost Of Tsushima")
        st.video("https://youtu.be/xU6p9t3xV2A")
    with col2:
        st.subheader("Call of Duty: WWII")
        st.video("https://youtu.be/88r7el5zshc")

elif page.endswith("Contact Details"):
    st.title("Contact Details")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            "📧 **Email**\n\n[rukmalmanoj651@gmail.com](mailto:rukmalmanoj651@gmail.com)")
    with c2:
        st.markdown(
            "🔗 **LinkedIn**\n\n[Connect](https://www.linkedin.com/in/rukmal-manoj-1a47a7376)")
    with c3:
        st.markdown(
            "🐙 **GitHub**\n\n[Repositories](https://github.com/Rukmal03)")

    st.write("---")
    st.subheader("Send a Message")

    WEB3FORMS_ACCESS_KEY = "af82c152-73aa-42f8-8d53-53e162073c10"

    contact_form_html = f"""
    <div style="width: 100%; box-sizing: border-box;">
        <form action="https://api.web3forms.com/submit" method="POST" style="background-color: rgba(255,255,255,0.7); padding: 15px; border-radius: 8px; border: 1px solid #999999;">
            <input type="hidden" name="access_key" value="{WEB3FORMS_ACCESS_KEY}">
            
            <div style="margin-bottom: 12px;">
                <label style="font-weight: 600; font-size: 0.9rem; font-family: sans-serif; color: #111111;">Name</label><br>
                <input type="text" name="name" required style="width: 100%; padding: 8px; border: 1px solid #777777; background: #ffffff; color: #000000; border-radius: 4px; box-sizing: border-box;">
            </div>
            <div style="margin-bottom: 12px;">
                <label style="font-weight: 600; font-size: 0.9rem; font-family: sans-serif; color: #111111;">Email Address</label><br>
                <input type="email" name="email" required style="width: 100%; padding: 8px; border: 1px solid #777777; background: #ffffff; color: #000000; border-radius: 4px; box-sizing: border-box;">
            </div>
            <div style="margin-bottom: 15px;">
                <label style="font-weight: 600; font-size: 0.9rem; font-family: sans-serif; color: #111111;">Message</label><br>
                <textarea name="message" rows="4" required style="width: 100%; padding: 8px; border: 1px solid #777777; background: #ffffff; color: #000000; border-radius: 4px; resize: vertical; box-sizing: border-box;"></textarea>
            </div>
            
            <button type="submit" style="background-color: #111111; color: white; padding: 10px 20px; border: none; cursor: pointer; font-weight: bold; width: 100%; text-transform: uppercase; letter-spacing: 1px; border-radius: 4px;">
                Send Message
            </button>
        </form>
    </div>
    """
    st.components.v1.html(contact_form_html, height=380, scrolling=False)
