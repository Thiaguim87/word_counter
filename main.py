import streamlit as st
from time import sleep as sp
st.title('Welcome to Word Counter')

my_txt = st.text_area(label='Your text here:')

b = st.button(label='Count!')
if b:
    if my_txt != '':
        st.success('Success!')
        sp(1)
        words = list(my_txt.split())

        letters = list(my_txt)

        wCounter = len(words)

        lCounter = len(letters)

        st.write(f'Words: {wCounter} ')
        sp(0.6)
        st.write(f'Characters: {lCounter}')
    else:
        st.warning('Invalid text!')