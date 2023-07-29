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

import fbprophet
from fbprophet import Prophet
#from prophet import Prophet 
from fbprophet.plot import plot_plotly

import base64