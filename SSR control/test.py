import streamlit as st

if st.button('Say hello'):
    print('hello')
else:
    st.write('Goodbye')