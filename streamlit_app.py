import streamlit as st
st.title('Breakfast Favorites')

st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.title('🍌🍓 Breakfast Favorites 🥝🍇')
import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
st.dataframe(my_fruit_list)
