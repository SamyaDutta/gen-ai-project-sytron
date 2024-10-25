import streamlit as st
import backend as bk

# Set a background color and change text color using markdown
st.markdown(
    """
    <style>
    /* Base styling */
    body {
        background-color: #f3f8fb;
        color: #333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
    }
    .main {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        margin: auto;
    }

    /* Title Styling */
    .title {
        color: #47a6d1;
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        padding: 1rem 0;
    }

    /* Button styling */
    .stButton button {
        background-color: #47a6d1;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #3696b8;
    }

    /* Input field styling */
    .stTextInput > div > input {
        border: 1px solid #47a6d1;
        padding: 0.6rem;
        border-radius: 8px;
        font-size: 1rem;
        margin-top: 0.5rem;
    }

    /* Responsive layout */
    @media (max-width: 768px) {
        .main {
            width: 100%;
            padding: 1.5rem;
        }
        .title {
            font-size: 2rem;
        }
    }

    /* Footer styling */
    footer {
        text-align: center;
        font-size: 0.9rem;
        padding-top: 1rem;
        color: #777;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.markdown("<h1 class='title'>✨ Gen AI Project for SYTRON ✨</h1>", unsafe_allow_html=True)

# Input and button components in a container
with st.container():
    user_input = st.text_input("Enter your query here:", placeholder="Ask me anything!")
    go_button = st.button("Go")

    if go_button and user_input.strip():
        with st.spinner("Generating response..."):
            output = get_text_output(user_input)
            st.markdown("<h3 style='color: #47a6d1; margin-top: 20px;'>Response:</h3>", unsafe_allow_html=True)
            st.write(f"📝 {output}")

# Footer section
st.markdown(
    """
    <footer>
        Built with 💖 by SAMYA DUTTA
    </footer>
    """,
    unsafe_allow_html=True
)


