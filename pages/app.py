import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go

# Streamlit UI
st.set_page_config(
    page_title="Prototype-Insighthub",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.markdown(
        "<h3 style='text-align: center; color: white;'>InsightHub: Empowering Investment Decisions in India's Entrepreneurial Landscape </h1>",
        unsafe_allow_html=True)

df = pd.read_csv("Dataset_Unicorn.csv", encoding='latin1')
#Filter data based on
st.sidebar.header("Filter based on:")
company_name = st.sidebar.multiselect("Company:", df["Company Name"].unique())

col1, col2 = st.columns((2))

df['Operating Revenue (FY23)'] = pd.to_numeric(df['Operating Revenue (FY23)'].str.replace(',', ''), errors='coerce')
df['Operating Revenue (FY22)'] = pd.to_numeric(df['Operating Revenue (FY22)'].str.replace(',', ''), errors='coerce')

df['Employee Benefit (FY23)'] = pd.to_numeric(df['Employee Benefit (FY23)'].str.replace(',', ''), errors='coerce')
df['Employee Benefit (FY22)'] = pd.to_numeric(df['Employee Benefit (FY22)'].str.replace(',', ''), errors='coerce')

df['Loss/ Profit (FY23)'] = pd.to_numeric(df['Loss/ Profit (FY23)'].str.replace(',', ''), errors='coerce')
df['Loss/ Profit (FY22)'] = pd.to_numeric(df['Loss/ Profit (FY22)'].str.replace(',', ''), errors='coerce')

df['Advertisement Spends (FY23)'] = pd.to_numeric(df['Advertisement Spends (FY23)'].str.replace(',', ''), errors='coerce')
df['Advertisement Spend (FY22)'] = pd.to_numeric(df['Advertisement Spend (FY22)'].str.replace(',', ''), errors='coerce')

#graphs time
#graph 1
df_melted = df.melt(value_vars=['Loss/ Profit (FY23)', 'Loss/ Profit (FY22)'], var_name='Year', value_name='Loss/ Profit')

with col1:
    fig = px.box(df_melted, x='Year', y='Loss/ Profit', title="Loss/ Profit Comparison (FY23 vs FY22)")
    st.plotly_chart(fig,use_container_width=True, height = 200)

top_companies = df.nlargest(10, 'Operating Revenue (FY23)')
top_companies1 = df.nlargest(10, 'Employee Benefit (FY23)')
with col2:
    choice = st.radio("Top 10 in terms of:", ["Operating Revenue", "Employee Benefit"]
    if choice == "Operating Revenue":
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=top_companies['Company Name'], y=top_companies['Operating Revenue (FY23)'],
                     name='Operating Revenue (FY23)'))
        fig1.add_trace(go.Bar(x=top_companies['Company Name'], y=top_companies['Operating Revenue (FY22)'],
                     name='Operating Revenue (FY22)'))
        fig1.update_layout(barmode='group',
                  title='Operating Revenue (FY23 vs FY22)',
                  xaxis_title='Company',
                  yaxis_title='Operating Revenue')
    else:
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(x=top_companies1['Company Name'], y=top_companies1['Employee Benefit (FY23)'],
                     name='Employee Benefit (FY23)'))
        fig1.add_trace(go.Bar(x=top_companies1['Company Name'], y=top_companies1['Employee Benefit (FY22)'],
                     name='Employee Benefit (FY22)'))
        fig1.update_layout(barmode='group',
                  title='Employee Benefit (FY23 vs FY22)',
                  xaxis_title='Company',
                  yaxis_title='Employee Benefit')
    st.plotly_chart(fig1,use_container_width=True, height = 200)
