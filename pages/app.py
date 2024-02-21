import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go

# Streamlit UI
st.set_page_config(
    page_title="Prototype-Insighthub",
    page_icon=":chart_with_upwards_trend:"
    layout="wide",
)
st.divider()
st.markdown(
        "<h3 style='text-align: center; color: white;'>InsightHub: Empowering Investment Decisions in India's Entrepreneurial Landscape </h1>",
        unsafe_allow_html=True)

df = pd.read_csv("Dataset_Unicorn.csv", encoding='latin1')
df['Operating Revenue (FY23)'] = pd.to_numeric(df['Operating Revenue (FY23)'].str.replace(',', ''), errors='coerce')
df['Operating Revenue (FY22)'] = pd.to_numeric(df['Operating Revenue (FY22)'].str.replace(',', ''), errors='coerce')

df['Employee Benefit (FY23)'] = pd.to_numeric(df['Employee Benefit (FY23)'].str.replace(',', ''), errors='coerce')
df['Employee Benefit (FY22)'] = pd.to_numeric(df['Employee Benefit (FY22)'].str.replace(',', ''), errors='coerce')

df['Loss/ Profit (FY23)'] = pd.to_numeric(df['Loss/ Profit (FY23)'].str.replace(',', ''), errors='coerce')
df['Loss/ Profit (FY22)'] = pd.to_numeric(df['Loss/ Profit (FY22)'].str.replace(',', ''), errors='coerce')

df['Advertisement Spends (FY23)'] = pd.to_numeric(df['Advertisement Spends (FY23)'].str.replace(',', ''), errors='coerce')
df['Advertisement Spend (FY22)'] = pd.to_numeric(df['Advertisement Spend (FY22)'].str.replace(',', ''), errors='coerce')

#graphs time
df_melted = df.melt(value_vars=['Loss/ Profit (FY23)', 'Loss/ Profit (FY22)'], var_name='Year', value_name='Loss/ Profit')

fig = px.box(df_melted, x='Year', y='Loss/ Profit', title="Loss/ Profit Comparison (FY23 vs FY22)")
fig.show()

top_companies = df.nlargest(10, 'Operating Revenue (FY23)')

fig = go.Figure()
fig.add_trace(go.Bar(x=top_companies['Company Name'], y=top_companies['Operating Revenue (FY23)'],
                     name='Operating Revenue (FY23)'))
fig.add_trace(go.Bar(x=top_companies['Company Name'], y=top_companies['Operating Revenue (FY22)'],
                     name='Operating Revenue (FY22)'))

fig.update_layout(barmode='group',
                  title='Operating Revenue Comparison (FY23 vs FY22) for Top Companies',
                  xaxis_title='Company',
                  yaxis_title='Operating Revenue')

fig.show()
