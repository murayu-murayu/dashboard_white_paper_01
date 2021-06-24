import pandas as pd
import streamlit as st
import plotly.express as px


st.title('白書ダッシュボード')
st.text('情報通信白書等から国内外のIT産業の動向が分かるデータのダッシュボード化')


df_department = pd.read_csv('./csv_data/department.csv', encoding='shift_jis')
df_iot_competitiveness = pd.read_csv('./csv_data/iot_competitiveness.csv', encoding='shift_jis')


# 部門別国内生産額等
st.header('■ 部門別国内生産額等')

wage_list = ['部門別名目国内生産額（十億円）', '部門別実質国内生産額（十億円）', '部門別名目GDP（十億円）', '部門別実質GDP（十億円）', '部門別雇用者数（千人）']
option_wage = st.selectbox(
    '選択',
    (wage_list))

max_x = df_department[option_wage].max() * 1.1

fig = px.bar(df_department,
            x=option_wage,
            y="部門名",
            color="部門名",
            animation_frame="年",
            range_x=[0,max_x],
            orientation='h',
            width=700,
            height=500)

st.plotly_chart(fig)


# IoT国際競争力指標
st.header('■ IoT国際競争力指標')
st.text('IoT・ICTの分野別の国・地域別市場シェア')

year_list = df_iot_competitiveness["年"].unique()

option_year = st.selectbox(
    '選択',
    (year_list))

df_iot_competitiveness_year = df_iot_competitiveness[(df_iot_competitiveness["年"] == option_year)]

fig = px.treemap(df_iot_competitiveness_year,
            path=[px.Constant(option_year), '分野', '国・地域'],
            values='シェア(%)',
            color='国・地域',
            color_discrete_sequence=px.colors.sequential.Blues
            #width=1200,
            #height=600
            )

st.plotly_chart(fig)


st.text('■　出典：令和2年版情報通信白書(総務省)')
st.text('■　出典：IoT国際競争力指標(2019年実績)(総務省)')

