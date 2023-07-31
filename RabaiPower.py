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
    fig.add_trace(go.Scatter(x=df['Datetime'],y=df['AvgKv1'],name='AvgKv1'))
    
    fig.layout.update(title_text="Energy Consumption History",xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

#new_title = '<p style="font-family:Lobster; color:Green; font-size: 42px;">Step 1: Feed in dataset</p>'
#st.markdown(new_title, unsafe_allow_html=True)

def example (content):
     st.markdown(f'<p style="text-align:center;background-image: linear-gradient(to right,#ee8004, #fbe54b);color:#080807;font-family:Peace Sans; font-size:40px;border-radius:2%;">{content}</p>', unsafe_allow_html=True)
example("Step 1: Tune Parameter") 

option=0
Tariff=("Tariff A - Domestic Tariff","Tariff B - Low Voltage for commercial", "Tariff E1 - Medium Voltage General Industrial Tariff" )
Selected_period = st.selectbox("***SELECT YOUR PREFFERED TARIFF:***", Tariff)
st.write("Don't know what tariff you're applying? [Refer here](https://www.tnb.com.my/assets/files/Tariff_Rate_Final_01.Jan.2014.pdf)")  
if Selected_period=="Tariff A - Domestic Tariff":
     option=0

if Selected_period=='Tariff B - Low Voltage Commercial Tariff':
     option=1

if Selected_period=='Tariff E1 - Medium Voltage General Industrial Tariff':
     option=2

period_forecast=31
Pt=("1 Week","2 Weeks","1 Month")
Selected_period=st.selectbox("Determine the period to forecast:",Pt)
if Selected_period=="1 Week":
     period_forecast=7*24+2
     type="H"

if Selected_period=="2 Weeks":
     period_forecast=14*24+2
     type="H"

if Selected_period=="1 Month":
     period_forecast=31
     type="d"






example("STEP 2: FEED IN THE DATASET")
st.subheader('***INPUT DATASET***')
data_file = st.file_uploader("Upload at least past 1 month Energy Usage ",type=["csv"])               



if data_file is not None:
     #st.write(type(data_file))
     file_details={"filename":data_file.name, "filetype":data_file.type, "filesize":data_file.size}
     #st.write(file_details)
     df=pd.read_csv(data_file)
     with st.spinner('Visualizing data....'):
          my_expander = st.expander("   Raw Data Preview", expanded=True)
          with my_expander:
               st.subheader('Raw Data Preview')
               st.write('This dataset contains energy and power consumed per hour for **3** months from **July 2022 ** to **September 2022 **')
               st.dataframe(df)
               plot_raw_data()




with st.spinner('Training model......'):
     #df.columns['ds','y']
     df=df.reset_index().rename(columns={'Datetime':'ds', 'AvgKv1':'y'})
     model = Prophet()
     model.fit(df)
     future_dates =  model.make_future_dataframe(periods=period_forecast, freq=type)
     prediction = model.predict(future_dates)
     fig1=plot_plotly(model,prediction, xlabel='Datetime', ylabel='Electricity Consumption')
     fig3=model.plot(prediction, xlabel='Date', ylabel='Electricity Consumption')
     fig2=model.plot_components(prediction)
     future=prediction[['ds','yhat']]
     periodd=future.tail(period_forecast)
     #fig0=plotly(periodd,xlabel='d=Datetime', ylabel='Electricity Consumption')
     fig0=periodd.plot(x='ds', xlabel='Datetime', ylabel='Electricity Consumption' )

     m,n=periodd.shape
     values = periodd.values  
     matrix = np.concatenate([values])

     import operator
     Output = max(matrix, key = operator.itemgetter(1))
     highesttime= Output[0]
     highestdemand= Output[1]

     sum=0
     tsum=0
     sum100=0
     sum200=0
     sum300=0
     sum600=0
     sum900=0
     i=0
     cost=0
     tcost=0
     total=0
     bringtonext1=0
     bringtonext2=0
     bringtonext3=0
     bringtonext4=0
     minimumc=0
     if option==0:

          while sum<=200 and i<(m-1):
               sum+=matrix[i][1]
               sum100+matrix[i][1]
               i+=1
          if sum>200:
               bringtonext1=sum-200
               sum=200


          sum100=sum
          cost100=sum*0.2180
          cost+=cost100


          while sum>200 and sum<=300 and i<=(m-1):
                sum+=matrix[i][1]
                sum200+=matrix[i][1]
                i+=1
          total=sum200+bringtonext1
          if total>100:
                bringtonext2=total-100
                sum200=100
                total=100
                sum=300
          cost200=total*0.3340
          cost+=cost200
          #sum200+=bringtonext1
          sum+=bringtonext1


          
                   