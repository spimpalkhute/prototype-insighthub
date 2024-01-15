import streamlit as st
import pandas as pd
import datetime

# Streamlit UI
st.set_page_config(
    page_title="Prototype-Insighthub",
    page_icon="👋",
)
st.title("Explore the world of Indian Startups")
st.divider()
    st.markdown(
        "<h3 style='text-align: center; color: black;'>InsightHub: Empowering Investment Decisions in India's Entrepreneurial Landscape </h1>",
        unsafe_allow_html=True)
    with open('./clock.time', 'r') as f:
        last_updated_on = f.readlines()[0]
    st.caption(last_updated_on)
    st.markdown('')
    st.image('img/tfinder_schema.png')
    st.markdown('')
    st.markdown('**Overview**')
df = pd.DataFrame({
    'first column': ['', 'Start-up Founder', 'Venture Capitalist'],
    })

option = st.selectbox(
    'You are:',
     df['first column'])

'You selected: ', option
    
