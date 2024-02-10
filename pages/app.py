import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go


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
top_companies = df.nlargest(10, 'Operating Revenue (FY23)')
df = pd.read_csv("Dataset_Unicorn.csv", encoding='latin-1')

df['Operating Revenue (FY23)'] = pd.to_numeric(df['Operating Revenue (FY23)'].str.replace(',', ''), errors='coerce')
df['Operating Revenue (FY22)'] = pd.to_numeric(df['Operating Revenue (FY22)'].str.replace(',', ''), errors='coerce')

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
option = st.selectbox(
    'You are:',
     df['first column'])

'You selected: ', option

# Choose columns for printing the dataset
selected_columns = st.multiselect("Select columns:", df.columns)
if selected_columns:
    st.dataframe(df[selected_columns])

# Check if columns are selected for plotting
if selected_columns:
    # Plot using Plotly Express
    fig = px.line(df, x=df.index, y=selected_columns, title="CSV Data Plot")
    st.plotly_chart(fig)
else:
    st.warning("Please select at least one column.")
