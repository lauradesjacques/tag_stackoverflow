import streamlit as st

title = st.text_input('Entrer la question', '  ')

st.button("Submit", type="primary")

options = st.multiselect(
    'topic',
    ['Tag1', 'Tag2', 'Tag3', 'Tag4'])
