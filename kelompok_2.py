import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px



st.title('Kelompok 2')
st.header("Ini adalah Data covid_19 di indonesia")

st.write("Membuat Tabel dari Data")
data = pd.read_csv('covid_19_indonesia_time_series_all.csv')

show_data = st.checkbox("Tampilkan Dataframe")
if show_data:
    st.write(data)

info = data.shape
if st.button("Lihat Total Data"):
    st.write(info)

Location = st.radio("pilih Lokasi covidnya", data.Location.unique())
Date = st.selectbox("pilih tanggal", data.Date.unique())
umur = st.slider('pilih umur mu', 13, 80)

arr = np.random.normal(1, 1, 100)
st.write(arr)
fig, ax = plt.subplots()
plt.hist(arr, bins=20)
st.pyplot(fig)

