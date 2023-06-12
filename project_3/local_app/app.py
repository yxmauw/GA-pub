import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from model_methods import predict

# configuration of the page
st.set_page_config(
    layout='centered',
    page_icon=Image.open('subreddit_icon.jpg'),
    page_title='Marvel vs. DC comics',
    initial_sidebar_state='auto'
)
st.image(Image.open('subreddit_icon.jpg'), width=100)
st.title('Subreddit Post classifier')
st.markdown('''
This app uses proprietary algorithm from 
subreddit posts published between 
April and July 2022 to generate predictions
''')

# Field for text input
st.markdown('''
Please copy and paste the 
subreddit post here
''')

new_post = st.text_input('Enter text here', '')

def predict_post():
    data = pd.Series(new_post)
    result = predict(data)
    if result == 1:
        post = 'Marvel'
    if result == 0:
        post = 'DC comics'
    st.success(f'### This post belongs to r/{post} subreddit')

if st.button('Submit'):
    with st.sidebar:
        try: 
            predict_post()
        except:
            st.warning('''
            Unable to detect text. 
            Please enter text for prediction. 
            \n\n Thank you 🙏. 
            ''')