import streamlit as st

# ----------------- CONFIGURATION & THEMING -----------------
st.set_page_config(
    page_title="Rukmal Manoj | Portfolio",
    page_icon="💼",
    layout="centered"
)

# Editorial Minimalist CSS Theme (Matching the image)
st.markdown("""
    <style>
    /* Warm grey/taupe full-bleed background */
    .main {
        background-color: #d5d1d4;
        color: #4a4a4a;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    /* Standard, clean, and bold header text */
.editorial-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: bold !important;
    color: #FFFFFF !important;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

/* Standard, clean, and bold header text */
.editorial-bio {
    text-align: center;
    font-size: 1.1rem;
    line-height: 1.6;
    color: #FFFFFF !important;
    opacity: 0. !important;
    max-width: 750px;
    margin: 0 auto 2rem auto;
    font-weight: normal !important;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
    }
    
    /* Thin dividing line matching the screenshot */
    .editorial-divider {
        width: 150px;
        height: 1px;
        background-color: #999999;
        margin: 0 auto 2.5rem auto;
    }
    
    /* Container block to center your profile image */
    .image-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 2rem;
    }

    /* Name Badge overlay style from the image */
    .name-badge {
        background-color: #ffffff;
        color: #000000;
        padding: 8px 24px;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        letter-spacing: 2px;
        border: 1px solid #c0bec1;
        text-transform: uppercase;
        margin-top: -20px;
        z-index: 10;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    
    /* Clean tab styling modifications to keep it premium */
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 0.9rem;
        letter-spacing: 1px;
        font-weight: 400;
        color: #666666;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- EDITORIAL HEADER (MATCHING SCREENSHOT) -----------------
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

st.markdown('<div class="editorial-divider"></div>', unsafe_allow_html=True)

# Centered Image Layout with the structured white name box underneath
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    st.image("rukmal.jpg", use_container_width=True)
    st.markdown(
        '<div style="display:flex; justify-content:center;"><div class="name-badge">Rukmal Manoj</div></div>',
        unsafe_allow_html=True
    )

st.write("##")  # Spacer

# ----------------- TABS FOR OTHER CONTENT -----------------
tab1, tab2, tab3 = st.tabs(
    [" What IF", " Game Playes ", " Contact Details"])

with tab1:
    st.write("##")
    st.write(
        "Welcome homies.")
    st.markdown("### 🎞️ Featured Projects")
    st.info("Portfolio showcase pending.")

with tab2:
    st.write("##")
    st.write("Game Playes By @lbedo.")

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.subheader("Ghost Of Tsushima")
        st.video("https://youtu.be/xU6p9t3xV2A")
    with col2:
        st.subheader("Call of Duty: WWII")
        st.video("https://youtu.be/88r7el5zshc")

with tab3:
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

    # Web3Forms Integration
    WEB3FORMS_ACCESS_KEY = "af82c152-73aa-42f8-8d53-53e162073c10"

    contact_form_html = f"""
    <form action="https://api.web3forms.com/submit" method="POST" style="background-color: rgba(255,255,255,0.4); padding: 24px; border-radius: 4px; border: 1px solid #b5b1b4;">
        <input type="hidden" name="access_key" value="{WEB3FORMS_ACCESS_KEY}">
        
        <div style="margin-bottom: 15px;">
            <label style="font-weight: 500; font-size: 0.9rem; font-family: sans-serif;">Name</label><br>
            <input type="text" name="name" required style="width: 100%; padding: 8px; border: 1px solid #a09da0; background: rgba(255,255,255,0.8);">
        </div>
        <div style="margin-bottom: 15px;">
            <label style="font-weight: 500; font-size: 0.9rem; font-family: sans-serif;">Email Address</label><br>
            <input type="email" name="email" required style="width: 100%; padding: 8px; border: 1px solid #a09da0; background: rgba(255,255,255,0.8);">
        </div>
        <div style="margin-bottom: 20px;">
            <label style="font-weight: 500; font-size: 0.9rem; font-family: sans-serif;">Message</label><br>
            <textarea name="message" rows="4" required style="width: 100%; padding: 8px; border: 1px solid #a09da0; background: rgba(255,255,255,0.8); resize: vertical;"></textarea>
        </div>
        
        <button type="submit" style="background-color: #333333; color: white; padding: 10px 20px; border: none; cursor: pointer; font-weight: bold; width: 100%; text-transform: uppercase; letter-spacing: 1px;">
            Send Message
        </button>
    </form>
    """
    st.components.v1.html(contact_form_html, height=420)
