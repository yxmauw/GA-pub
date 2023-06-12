import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from model_methods import predict
import base64 # for title image
from load_css import local_css # for highlighting text

@st.cache # cached so that latency for subsequent runs are shorter
def import_nltk():
    import nltk
    nltk.download('wordnet')
    nltk.download('omw-1.4')

# configuration of the page
st.set_page_config(
    layout='centered',
    page_icon=Image.open('project_3/cloud_app/subreddit_icon.png'),
    page_title='Marvel vs. DC comics',
    initial_sidebar_state='auto'
)

# embed source link in title image using base64 module
# reference: https://discuss.streamlit.io/t/how-to-show-local-gif-image/3408/4
# reference: https://discuss.streamlit.io/t/local-image-button/5409/4
im = open("project_3/cloud_app/subreddit_icon.png", "rb")
contents = im.read()
im_base64 = base64.b64encode(contents).decode("utf-8")
im.close()
html = f'''<a href='https://www.reddit.com/'> 
            <img src='data:image/png;base64,{im_base64}' width='100'>
            </a><figcaption>Credit: reddit.com</figcaption>'''
st.markdown(html, unsafe_allow_html=True)

st.title('Subreddit Post classifier')
local_css("project_3/cloud_app/highlight_text.css")
text = '''The algorithm driving this app is built using subreddit posts published 
between April and July 2022. It is only able to classify between 
<span class='highlight blue'> **Marvel** </span>
and 
<span class='highlight blue'> **DC Comics** </span>
subreddits.'''
st.markdown(text, unsafe_allow_html=True)

# Area for text input
import_nltk() # import nltk module if not yet cached in local computer
new_post = st.text_input('Please copy and paste the subreddit post here', '')

# process new input
def predict_post():
    data = pd.Series(new_post) # pd.Series format new input coz that is the format that predict() recognises
    result = predict(data)
    if result == 1:
        post = 'Marvel'
    if result == 0:
        post = 'DC comics'
    st.write(f'### This post belongs to') 
    st.success(f'# {post}')
    st.write(f'### subreddit')

# instantiate submit button
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
