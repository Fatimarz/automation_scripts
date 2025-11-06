import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#file upload
uploaded=st.file_uploader('Upload CSV', type=['csv'])
if uploaded is not None:
    df=pd.read_csv(uploaded)

#cleaning
df.columns = df.columns.str.strip().str.lower()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

st.subheader('cleaned data')
st.dataframe(df)
st.write(df.describe())

st.subheader('Grade Distribution')
st.bar_chart(df['grade'].value_counts())
st.write('Min marks', df['marks'].min())
st.write('Max Marks', df['marks'].max())
