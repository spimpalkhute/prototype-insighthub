import streamlit as st
import pandas as pd
# Streamlit UI
st.set_page_config(
    page_title="Prototype-Insighthub",
    page_icon="👋",
)
st.title("Explore the world of Indian Startups")
df = pd.DataFrame({
    'first column': ['', 'Start-up Founder', 'Venture Capitalist'],
    })

option = st.selectbox(
    'You are:',
     df['first column'])

'You selected: ', option

