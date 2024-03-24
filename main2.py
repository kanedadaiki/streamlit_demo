import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit レイアウト')

st.sidebar.write('Interactive Widgets')

text = st.sidebar.text_input('貴方の趣味を教えてください')
condition = st.sidebar.slider('貴方の調子は?', 0, 100, 50)

'貴方の趣味:', text
'コンディション:', condition


