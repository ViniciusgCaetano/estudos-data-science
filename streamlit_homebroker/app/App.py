import streamlit as st
import plotly.graph_objects as go
from plotly.colors import n_colors
from plotly.subplots import make_subplots
import numpy as np
import api_connections.get_candle_data as gcd
import api_connections.get_order_data as gmd
import api_connections.get_last_trades as glt
import assets.order_graph as aog
import assets.candle_graph as acg
import assets.last_trades as alt



st.set_page_config(layout="wide")

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
col1.title('BTC/USDT')
col2.metric('Price', 17415.93)
col3.metric('24h Change', 17415.93)
col4.metric('24h High', 17415.93)
col5.metric('24h Low', 17415.93)
col6.metric('24h Volume(BTC)', 17415.93)
col7.metric('24h Volume(USDT)', 17415.93)

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    order_json = gmd.get_orders('BTCUSDT', 15)
    fig = aog.order_book(order_json)
    config=dict(
                    displayModeBar=False, 
                )
    st.plotly_chart(fig, use_container_width=True, config=config, theme=None)


with col2:
    df = gcd.get_candles('BTCUSDT', '1d')
    fig = acg.candle_graph(df)
    config=dict(
                    displayModeBar=False,
                    
                )
     
    st.plotly_chart(fig, use_container_width=True, config=config)
    

with col3:
    df = glt.get_last_trades('BTCUSDT')
    fig = alt.last_trades(df)
    st.plotly_chart(fig, use_container_width=True, config=config)