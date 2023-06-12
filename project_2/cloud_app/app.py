# https://www.analyticsvidhya.com/blog/2021/07/streamlit-quickly-turn-your-ml-models-into-web-apps/
import streamlit as st
import pandas as pd
import numpy as np
from model_methods import predict

# configuration of the page
st.set_page_config(
    layout="centered", 
    page_icon="🏠", 
    page_title="Are you planning to sell your house?", 
    initial_sidebar_state='auto',
)

st.title("🏠Ames Housing Sale Price recommendation tool")
st.markdown('''
The algorithm driving this app is built on
historical housing sale price data to generate
recommended Sale Price! Please enter your house details 
to get a Sale Price suggestion 🙂
''')
###########################################################
st.info('Only Enter Numeric Values in the Following Fields')

gr_liv_area = st.text_input('Enter house ground living area in square feet. Accept values 334 to 3395 inclusive', '')
overall_qual = np.nan
total_bsmt_sf = st.text_input('Enter house total basement area in square feet. Accept values 0 to 3206 inclusive', '')
garage_area = st.text_input('Enter house garage area in square feet. Accept values 0 to 1356 inclusive', '')
year_built = st.text_input('Enter the year your house was built. Accept values 1872 to 2010 inclusive', '')
mas_vnr_area = st.text_input('Enter house masonry veneer area in square feet. Accept values 0 to 1129 inclusive', '')

def predict_price():
    data = list(map(float, [gr_liv_area,
                            (float(gr_liv_area))**2,
                            (float(gr_liv_area))**3,
                            overall_qual, 
                            total_bsmt_sf,
                            garage_area,
                            year_built,
                            mas_vnr_area]))
    result = np.format_float_positional((predict(data)[0]), unique=False, precision=0)
    st.info(f'# Our SalePrice suggestion is ${result}')
    st.write('with an estimated uncertainty of ± \$11K')

if st.button('Recommend Saleprice'):
    if gr_liv_area and overall_qual and total_bsmt_sf and garage_area and year_built and mas_vnr_area:
        with st.sidebar:
            try: 
                predict_price()
            except:
                st.warning('''Oops, looks like you missed a spot. 
                Please complete all fields to get a quote estimate 
                for property Sale Price 🙏. 
                \n\n Thank you. 🙂''')
