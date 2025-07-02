import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
st.header('Dashboard Financeiro')

df = pd.read_csv("supermarket_sales.csv", sep=";",decimal=",")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(['Date'])

df['mes'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))
month = st.sidebar.selectbox('Mês', df['mes'].unique())

df_filtered = df[df['mes'] == month]
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

prod_total = df_filtered.groupby('Date')['Total'].sum().reset_index()
city_total = df_filtered.groupby('Date')['Total'].mean().reset_index()

with col1:
    fig_date = px.bar(df_filtered, x='Date',y='Total',color='City',title='Faturamento diário')
    col1.plotly_chart(fig_date,use_container_width=True)
with col2:
    fig_prod = px.bar(df_filtered, x='Date',y='Product line',color='City',title='Faturamento por tipo de produto',orientation='h')
    col2.plotly_chart(fig_prod,use_container_width=True)
with col3:
    st.subheader('Gráfico de linhas')
    col3.line_chart(prod_total,x='Date',y='Total',use_container_width=True)
with col4:
    fig_pay = px.pie(df_filtered,values='Total', names='Payment',title='Faturamento por pagamento')
    col4.plotly_chart(fig_pay,use_container_width=True)
with col5:
    fig_rating = px.bar(df_filtered,x='City',y='Rating',title='Rating')
    col5.plotly_chart(fig_rating,use_container_width=True)