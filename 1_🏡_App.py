import pandas as pd
import numpy as np

import streamlit as st

st.write('''
    # **Hello Streamlit!**
''')

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]    
})

st.write(df.transpose())