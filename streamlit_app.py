# Import python packages
import streamlit as st
streamlit.title('my parents new healthy diner')
from snowflake.snowpark.functions import col
import requests
import pandas as pd

st.title(":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom smooothie!
    """
)


name_on_order = st.text_input("Name on smoothie:")
st.write("The name on your smoothie will be:", name_on_order)

cnx= st.connection("snowflake")
session = cnx
    
