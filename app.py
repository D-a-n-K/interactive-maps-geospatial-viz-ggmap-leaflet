import streamlit as st
import numpy as np
import pandas as pd

# Title
st.title('Sara\'s First Streamlit App')

# Header
st.header('Welcome to Streamlit')

# Slider widget
number = st.slider('Select a number', 0, 100, 50)
st.write(f'You selected: {number}')

# Text input
name = st.text_input('Enter your name', 'World')
st.write(f'Hello, {name}!')

# Display a simple chart
st.subheader('Data Chart')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Display a dataframe
st.subheader('Data Frame')
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})
st.dataframe(df)