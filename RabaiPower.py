import streamlit as st
import pandas as pd
import datetime as dt
import seaborn as sns
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from plotly import graph_objs as go

import prophet
from prophet import Prophet
#from prophet import Prophet 
from prophet.plot import plot_plotly
import base64

sum=0
sum100=0
sum200=0
sum300=0
sum600=0
sum900=0
i=0
cost=0
cost100=0
cost200=0
cost300=0
cost600=0
cost900=0


image = Image.open('elec.jpeg')
st.image(image, width=500,) 


#st.title("ELECTRICITY CONSUMPTION")
st.write("""
# ELECTRICITY CONSUMPTION PREDICTION WEB APP ⚡️

This app predicts the **energy consumption for the next month**!📈  
Download a sample dataset here if you don't have one:""")



df = pd.read_csv("RabaiSub.csv")
coded_second=base64.b64encode(df.to_csv(index=False).encode()).decode()
st.markdown(f'<a href="data:file/csv;base64,{coded_second}" download="example.csv">Download Example Dataset</a>',unsafe_allow_html=True)

with st.sidebar:


     image=Image.open('untitled.png')
     st.image(image,use_column_width=True) 
     st.header('About Us')
     st.write("""**KPLC**  The Company's vision is to be Kenya's energy solutions provider of choice by providing quality and reliable service to power people for better lives and enable the country's socio-economic development in a sustainable manner. 
             

      Connect with us and discover products and solutions to solve your business needs.
""")
     st.subheader('We Unlock these Impossibilities:')
     st.markdown(
"Real-time electricity monitoring platform  \n"
"Far-distance controlling system  \n"
"On-Spot alterting service  \n"  
"Energy forecasting application  \n"       
)





def plot_raw_data():
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df['Datetime'],y=df['Energy_kWh'],name='Energy_kWh'))
    
    fig.layout.update(title_text="Energy Consumption History",xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

#new_title = '<p style="font-family:Lobster; color:Green; font-size: 42px;">Step 1: Feed in dataset</p>'
#st.markdown(new_title, unsafe_allow_html=True)

def example (content):
     st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,#ee8004, #fbe54b);color:#080807;font-family:Peace Sans; font-size:40px;border-radius:2%;">{content}</p>', unsafe_allow_html=True)
example("Step 1: Tune Parameter") 
  

      