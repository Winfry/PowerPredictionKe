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


#st.title("ELECTRICITY CONSUMPTION")
st.write("""
# ELECTRICITY CONSUMPTION PREDICTION WEB APP ⚡️

This app predicts the **energy consumption for the next month**!📈  
Download a sample dataset here if you don't have one:""")

