import streamlit as st

# ඔබේ HTML සහ CSS කේතය Streamlit වෙත ඇතුළත් කිරීම
st.markdown(
    """
    <head>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sofia">
    <style>
    /* මුළු ඇප් එකේම text සඳහා Sofia font එක යෙදීම */
    html, body, [class*="css"] {
        font-family: "Sofia", sans-serif;
    }
    </style>
    </head>
    """,
    unsafe_allow_html=True
)

# දැන් ඔබ ලියන ඕනෑම text එකක් "Sofia" font එකෙන් දර්ශනය වේ
st.title("Welcome to Eventza")
st.write("This text is now using the Sofia font.")
