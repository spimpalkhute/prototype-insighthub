import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import openpyxl

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

# Load your Excel file
excel_file_path = "Dataset_Unicorn.xlsx"  # Replace with your actual file path
df = pd.read_excel(excel_file_path)

# Display the DataFrame
st.write("DataFrame from Excel file:")
st.write(df)

# Choose columns for plotting
columns = st.multiselect("Select columns for plotting", df.columns)

# Check if columns are selected
if columns:
    # Plot using Plotly Express
    fig = px.line(df, x=df.index, y=columns, title="Excel Data Plot")
    st.plotly_chart(fig)
else:
    st.warning("Please select at least one column for plotting.")
