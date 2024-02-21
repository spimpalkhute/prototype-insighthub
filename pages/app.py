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

st.sidebar.markdown(
        "<h3 style='text-align: center; color: white;'>InsightHub: Empowering Investment Decisions in India's Entrepreneurial Landscape </h1>",
        unsafe_allow_html=True)

df = pd.read_csv("Dataset_Unicorn.csv", encoding='latin1')


col1, col2 = st.columns((2))

df['Operating Revenue (FY23)'] = pd.to_numeric(df['Operating Revenue (FY23)'].str.replace(',', ''), errors='coerce')
df['Operating Revenue (FY22)'] = pd.to_numeric(df['Operating Revenue (FY22)'].str.replace(',', ''), errors='coerce')

df['Employee Benefit (FY23)'] = pd.to_numeric(df['Employee Benefit (FY23)'].str.replace(',', ''), errors='coerce')
df['Employee Benefit (FY22)'] = pd.to_numeric(df['Employee Benefit (FY22)'].str.replace(',', ''), errors='coerce')

df['Loss/ Profit (FY23)'] = pd.to_numeric(df['Loss/ Profit (FY23)'].str.replace(',', ''), errors='coerce')
df['Loss/ Profit (FY22)'] = pd.to_numeric(df['Loss/ Profit (FY22)'].str.replace(',', ''), errors='coerce')

df['Advertisement Spends (FY23)'] = pd.to_numeric(df['Advertisement Spends (FY23)'].str.replace(',', ''), errors='coerce')
df['Advertisement Spend (FY22)'] = pd.to_numeric(df['Advertisement Spend (FY22)'].str.replace(',', ''), errors='coerce')

df1 = pd.read_csv('unicorns100.csv')
df_cols = [
    'Company',
    'Founded In',
    'Current Status',
    'Sector',
    'Headquarters',
    'Total Funding',
    'Valuation',
    'Years to Unicorn'
]
df1 = df1[df_cols]

df1['Years to Unicorn'] = pd.to_numeric(df1['Years to Unicorn'].str.replace('years', '').str.replace('Years', ''), errors='coerce')
df1['Valuation'] = df1['Valuation'].str.replace('$', '').str.replace('+', '').str.replace('<', '').str.replace('Less than', '')
df1['Val_num'] = df1['Valuation'].str.replace('Mn', '').str.replace('Bn', '')
df1['Val_num'] = pd.to_numeric(df1['Val_num'], errors='coerce')

df1.loc[df1['Valuation'].notnull() & df1['Valuation'].astype(str).str.endswith('Mn'), 'Val_num'] *= 1000000
df1.loc[df1['Valuation'].notnull() & df1['Valuation'].astype(str).str.endswith('Bn'), 'Val_num'] *= 100000000

df1['Total Funding'] = df1['Total Funding'].str.replace('$', '').str.replace('+', '').str.replace('<', '').str.replace('Less than', '')

df1['Funding_num'] = df1['Total Funding'].str.replace('Mn', '').str.replace('Bn', '')
df1['Funding_num'] = pd.to_numeric(df1['Funding_num'], errors='coerce')

df1.loc[df1['Total Funding'].notnull() & df1['Total Funding'].astype(str).str.endswith('Mn'), 'Funding_num'] *= 1000000
df1.loc[df1['Total Funding'].notnull() & df1['Total Funding'].astype(str).str.endswith('Bn'), 'Funding_num'] *= 100000000

#Filter data based on
st.sidebar.header("Filter based on:")
company_name = st.sidebar.multiselect("Company:", df1["Company"].unique())

#graphs time
#graph 1
df_melted = df.melt(value_vars=['Loss/ Profit (FY23)', 'Loss/ Profit (FY22)'], var_name='Year', value_name='Loss/ Profit')
textbox_style = """
    <style>
        .textbox {
            background: rgba(255, 255, 255, 0.1);
            padding: 2px;
            border-radius: 15px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            color: #ffffff;
            text-align: center;
        }
        .textbox h1 {
            font-size: 32px;
            font-weight: bold;
            margin: 0;
        }
    </style>
"""
with col1:
    if company_name:
            subset_df = df1[df1['Company'].isin(company_name)]
            mean_valuation = subset_df['Val_num'].mean()
    else:
        mean_valuation = df1['Val_num'].mean()
    st.markdown(textbox_style, unsafe_allow_html=True)
    st.markdown(f"<div class='textbox'><h1>₹{mean_valuation:,.2f}</h1></div>", unsafe_allow_html=True)
    fig = px.box(df_melted, x='Year', y='Loss/ Profit', title="Loss/ Profit Comparison (FY23 vs FY22)")
    st.plotly_chart(fig,use_container_width=True, height = 200)

top_companies = df.nlargest(10, 'Operating Revenue (FY23)')
top_companies1 = df.nlargest(10, 'Employee Benefit (FY23)')
with col2:
    choice = st.radio("Top 10 in terms of:", ["Operating Revenue", "Employee Benefit"])
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


with col1:
    pie_fig = px.pie(data_frame=df1, names='Sector', title='Sector Distribution')
    st.plotly_chart(pie_fig,use_container_width=True, height = 200)
with col2:
    startup_counts = df1['Founded In'].value_counts().reset_index()
    startup_counts.columns = ['Founded In', 'Number of Startups']
    fig = px.bar(startup_counts, x='Founded In', y='Number of Startups',
             labels={'Founded In': 'Year Founded', 'Number of Startups': 'Number of Startups'},
             title='Number of Unicorns Founded Each Year')
    st.plotly_chart(fig,use_container_width=True, height=100)
