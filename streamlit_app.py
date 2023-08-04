import streamlit as st
st.title('Breakfast Favorites')

st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.title('🍌🍓 Breakfast Favorites 🥝🍇')
import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# Let's put a pick a list here so they can pick the fruit they want to include
st.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display the table on the page
st.dataframe(my_fruit_list)
