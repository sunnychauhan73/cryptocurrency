import yfinance as yf
import streamlit as st
import pandas as pd 
from datetime import datetime
from datetime import date 
from dateutil.relativedelta import relativedelta 
import plotly.express as px 
import graphviz
crypto_mapping = {"Bitcoin" : "BTC-USD", "Ethereum":"ETH-USD"}
st.title("Crypto Tracker")
crypto_option = st.sidebar.selectbox("Which crypto do you want to Visualize" ,("Bitcoin","Ethereum"))
start_date = st.sidebar.date_input("Start Date" , date.today() - relativedelta(months=1))
end_date = st.sidebar.date_input("End Date",date.today())
data_interval = st.sidebar.selectbox(
    "Data Interval",
    (
    "1m",
    "1m",
    "5m",
    "15m",
    "30m",
    "60m",
    "90m",
    "1h",
    "1d",
    "5d",
    "1wk",
    "1mon",
    "3mon",
    
    
),
)
symbol_crypto = crypto_mapping[crypto_option]
data_crypto = yf.Ticker(symbol_crypto)
value_selector = st.sidebar.selectbox( "value_selector" ,("Open","High","Low","Close","Volume"))
if st.sidebar.button("Generate"):
    crypto_hist = data_crypto.history(
        start=start_date , end=end_date , interval=data_interval)
    fig = px.line(crypto_hist, 
                 x=crypto_hist.index , y=value_selector,
                 labels = {"x": "Date"}) 
    st.plotly_chart(fig)            
                    
st.header("Data Flow Diagram")  
a = graphviz.Graph(engine="neato")  
a.node("Database") 
a.edge("input","process")   
a.edge("process","input", "INPUT UNIT") 
a.edge("output","process", "OUTPUT UNIT") 
a.edge("process","output")  
a.node("Client")   
st.graphviz_chart(a)         
        