# PowerPredictionKe

Forecasting power demand plays an essential role in the energy industry, as it provides the basis for making decisions in power system planning and operation. Electrical companies use various methods for predicting electricity demand. These are applied to short-term, medium-term, or long-term forecasting.
The objective is to effectively untangle all the factors that lead to demand change and determine the underlying causes. This project explains how machine learning can help predict energy demand.  

# Contents:

  -Data set from the Rabai substation
  -Predictive model.
  To illustrate this process, we build a Predictive Machine Learning Model for predicting the demand for electricity using a real data set taken from the company.

# 1. Data set
A good model for predicting the demand for electricity requires to analyze the following types of variables: 
    - Calendar data: Season, hour, bank holidays, etc.
    -  Demand data: Historical consumption of electricity.

The first column represents the date and hour when the measure of each instance is done. The following column is the electric power demand for that hour of the day in this specific substation in Average Kilovolts.     

#  Time series charts
The time series charts of our dataset are represented here. The first one is the temperature at 23:00 for the final period of our data.

# Predictive model
This data is brought together in a single predictive model to discover associations between all the above variables.This will give us a more in-depth understanding of the causes of demand and allow better decision-making. 

# Testing analysis
The objective of the testing analysis is to evaluate the predictive power of the machine learning algorithm on new data that have not been seen before, the testing instances.This process will determine if the predictive model is good enough to be moved into the deployment phase.First, we perform the linear regression analysis between the outputs and the corresponding targets for an independent testing subset.

# Model deployment
Once we have our predictive model tested, we can apply it to predict the electric power demand for the next month using **Streamlit**. This process is called model deployment.
The project shows the hourly electric power demand prediction for tomorrow in kV, considering the following inputs:  yesterday and today's power demands. 
