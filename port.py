import streamlit as st
import os

# ----------------- PAGE CONFIG -----------------
st.set_page_config(
    page_title="Rukmal Manoj | Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------- GLOBAL STYLING & NAVIGATION EFFECT -----------------
st.markdown("""
    <!-- Load FontAwesome Icon Library -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
    /* Warm grey/taupe full-bleed background */
    .stApp {
        background-color: #d5d1d4;
        color: #111111 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* =========================================================
       GLOBAL TEXT OPACITY & READABILITY OVERRIDES
       ========================================================= */
    p, span, label, h1, h2, h3, h4, h5, h6, div, a {
        opacity: 1 !important;
        color: #111111 !important;
        text-shadow: none !important;
    }

    /* Hide sidebar expander button completely */
    [data-testid="stSidebarCollapseButton"] {
        display: none !important;
    }

    /* =========================================================
       CUSTOM NAVIGATION BAR WITH UNDERLINE SEPARATOR
       ========================================================= */
    
    /* Center the horizontal radio group container */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] {
        display: flex !important;
        justify-content: center !important;
        gap: 16px !important;
        flex-wrap: wrap !important;
        margin-bottom: 0rem !important;
        padding-bottom: 12px !important;
    }

    /* REMOVE ALL STREAMLIT RADIO DOTS & SVGs */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label > div:first-child,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label svg,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] label input,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] [data-aria-hidden="true"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Navigation Button Base Styling */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label {
        position: relative !important;
        background-color: rgba(255, 255, 255, 0.6) !important;
        border: 1px solid rgba(150, 150, 150, 0.8) !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        overflow: hidden !important;
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05) !important;
        outline: none !important;
    }

    /* Text & Emoji inside navigation buttons */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label p {
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.6px !important;
        color: #111111 !important;
        opacity: 1 !important;
        margin: 0 !important;
        z-index: 2 !important;
        transition: color 0.3s ease !important;
    }

    /* CUSTOM ANIMATED BOTTOM BAR FOR ACTIVE TAB */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label::after {
        content: '' !important;
        position: absolute !important;
        bottom: 0 !important;
        left: 50% !important;
        width: 0% !important;
        height: 3px !important;
        background: #000000 !important;
        border-radius: 3px 3px 0 0 !important;
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
        transform: translateX(-50%) !important;
    }

    /* HOVER STATE */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label:hover {
        background-color: #ffffff !important;
        border-color: #000000 !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12) !important;
    }

    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label:hover::after {
        width: 60% !important;
    }

    /* ACTIVE / SELECTED STATE */
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label[data-checked="true"],
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label:has(input:checked) {
        background-color: #ffffff !important;
        border-color: #000000 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15) !important;
    }

    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label[data-checked="true"]::after,
    [data-testid="stMainBlockContainer"] [role="radiogroup"] > label:has(input:checked)::after {
        width: 100% !important;
        background: #000000 !important;
    }

    /* HORIZONTAL DIVIDER LINE UNDER TABS */
    .nav-divider {
        width: 100%;
        height: 1px;
        background-color: #888888;
        margin-top: 0rem;
        margin-bottom: 2rem;
    }

    /* =========================================================
       EDITORIAL PAGE STYLES & SOCIAL ICONS STYLING
       ========================================================= */
    .editorial-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800 !important;
        color: #000000 !important;
        opacity: 1 !important;
        margin-top: 0.5rem;
        margin-bottom: 1rem;
    }

    .editorial-bio {
        text-align: center;
        font-size: 1.05rem;
        line-height: 1.65;
        color: #111111 !important;
        opacity: 1 !important;
        font-weight: 500 !important;
        max-width: 800px;
        margin: 0 auto 1.5rem auto;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    .editorial-divider {
        width: 120px;
        height: 1px;
        background-color: #666666;
        margin: 0 auto 2rem auto;
    }

    .name-badge {
        background-color: #ffffff;
        color: #000000 !important;
        opacity: 1 !important;
        padding: 8px 24px;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 1rem;
        font-weight: 800;
        letter-spacing: 2px;
        border: 1px solid #888888;
        text-transform: uppercase;
        margin-top: -15px;
        z-index: 10;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }

    /* SOCIAL MEDIA ICONS BAR BELOW NAME BADGE */
    .social-icons-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        margin-top: 20px;
    }

    .social-icon-link {
        color: #333333 !important;
        font-size: 1.3rem;
        text-decoration: none !important;
        transition: all 0.3s ease;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background-color: rgba(255, 255, 255, 0.5);
        border: 1px solid rgba(150, 150, 150, 0.5);
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    }

    .social-icon-link:hover {
        color: #ffffff !important;
        background-color: #222222 !important;
        border-color: #222222 !important;
        transform: translateY(-3px) scale(1.1);
        box-shadow: 0 6px 14px rgba(0,0,0,0.15);
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- TOP MAIN PAGE NAVIGATION BAR -----------------
page = st.radio(
    "Navigation",
    [" Home", " What IF", " Game Plays", " Contact Details"],
    horizontal=True,
    label_visibility="collapsed"
)

# Line drawn directly under control tabs
st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)

# Extract page title without emoji
page_name = page.split(" ", 1)[1] if " " in page else page

# ----------------- PAGE 1: HOME (ABOUT ME) -----------------
if page_name == "Home":
    st.markdown('<div class="editorial-title">About Me</div>',
                unsafe_allow_html=True)

    st.markdown(
        """
        <div class="editorial-bio">
            I am a Business Information Systems undergraduate at the University of Sri Jayewardenepura, 
            currently in my second year. Alongside my academic focus on technology and management, 
            I am passionate about digital content creation, data analytics, and building digital platforms 
            that solve real-world problems. I am always eager to connect with like-minded professionals 
            and explore new opportunities in the tech and business space.
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
            st.info(
                "💡 Place `rukmal.jpg` in your project directory to display your photo here.")

        # Name Badge
        st.markdown(
            '<div style="display:flex; justify-content:center;"><div class="name-badge">Rukmal Manoj</div></div>',
            unsafe_allow_html=True
        )

        # ── SOCIAL MEDIA ICONS BAR ──
        st.markdown(
            """
            <div class="social-icons-container">
                <a href="https://instagram.com" target="_blank" class="social-icon-link" title="Instagram">
                    <i class="fab fa-instagram"></i>
                </a>
                <a href="https://youtube.com" target="_blank" class="social-icon-link" title="YouTube">
                    <i class="fab fa-youtube"></i>
                </a>
                <a href="https://www.linkedin.com/in/rukmal-manoj-1a47a7376" target="_blank" class="social-icon-link" title="LinkedIn">
                    <i class="fab fa-linkedin-in"></i>
                </a>
                <a href="https://github.com/Rukmal03" target="_blank" class="social-icon-link" title="GitHub">
                    <i class="fab fa-github"></i>
                </a>
                <a href="https://facebook.com" target="_blank" class="social-icon-link" title="Facebook">
                    <i class="fab fa-facebook-f"></i>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

# ----------------- PAGE 2: WHAT IF -----------------
elif page_name == "What IF":
    st.title("What IF")
    st.write("##")
    st.write("Welcome Homies.")
    st.markdown("### 🎞️ Featured Projects")
    st.info("Portfolio showcase pending.")

# ----------------- PAGE 3: GAME PLAYS -----------------
elif page_name == "Game Plays":
    st.title("Game Plays")
    st.write("##")
    st.write("Game Plays By **@lbedo**.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ghost Of Tsushima")
        st.video("https://youtu.be/xU6p9t3xV2A")
    with col2:
        st.subheader("Call of Duty: WWII")
        st.video("https://youtu.be/88r7el5zshc")

# ----------------- PAGE 4: CONTACT DETAILS -----------------
elif page_name == "Contact Details":
    st.title("Contact Details")
    st.write("##")

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
    <div style="width: 100%; max-width: 100%; overflow-x: hidden;">
        <form action="https://api.web3forms.com/submit" method="POST" style="background-color: rgba(255,255,255,0.6); padding: 20px; border-radius: 6px; border: 1px solid #999999;">
            <input type="hidden" name="access_key" value="{WEB3FORMS_ACCESS_KEY}">
            
            <div style="margin-bottom: 12px;">
                <label style="font-weight: 600; font-size: 0.95rem; font-family: sans-serif; color: #111111;">Name</label><br>
                <input type="text" name="name" required style="width: 100%; padding: 8px; border: 1px solid #777777; background: rgba(255,255,255,0.95); color: #000000; border-radius: 4px; box-sizing: border-box;">
            </div>
            <div style="margin-bottom: 12px;">
                <label style="font-weight: 600; font-size: 0.95rem; font-family: sans-serif; color: #111111;">Email Address</label><br>
                <input type="email" name="email" required style="width: 100%; padding: 8px; border: 1px solid #777777; background: rgba(255,255,255,0.95); color: #000000; border-radius: 4px; box-sizing: border-box;">
            </div>
            <div style="margin-bottom: 15px;">
                <label style="font-weight: 600; font-size: 0.95rem; font-family: sans-serif; color: #111111;">Message</label><br>
                <textarea name="message" rows="4" required style="width: 100%; padding: 8px; border: 1px solid #777777; background: rgba(255,255,255,0.95); color: #000000; border-radius: 4px; resize: vertical; box-sizing: border-box;"></textarea>
            </div>
            
            <button type="submit" style="background-color: #111111; color: white; padding: 10px 20px; border: none; cursor: pointer; font-weight: bold; width: 100%; text-transform: uppercase; letter-spacing: 1px; border-radius: 4px;">
                Send Message
            </button>
        </form>
    </div>
    """
    st.components.v1.html(contact_form_html, height=420, scrolling=False)
