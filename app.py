import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

# Streamlit UI
st.set_page_config(
    page_title="Prototype-Insighthub",
    page_icon="👋",
)
st.divider()
st.markdown(
        "<h3 style='text-align: center; color: white;'>InsightHub: Empowering Investment Decisions in India's Entrepreneurial Landscape </h1>",
        unsafe_allow_html=True)
st.markdown('')
st.markdown('**Overview**')
df = pd.DataFrame({
    'first column': ['', 'Start-up Founder', 'Venture Capitalist'],
    })

option = st.selectbox(
    'You are:',
     df['first column'])

'You selected: ', option

file_path = "Dataset_Unicorn.csv"  # Replace with your actual file path
df = pd.read_csv(file_path, encoding='utf-8')

# Display the DataFrame
st.write("Indian Unicorns:")
st.write(df)

# Choose columns for plotting
#columns = st.multiselect("Select columns for plotting", df.columns)

# Check if columns are selected
#if columns:
    # Plot using Plotly Express
    #fig = px.line(df, x=df.index, y=columns, title="Unicorn Data Plot")
    #st.plotly_chart(fig)
#else:
    #st.warning("Please select at least one column for plotting.")
