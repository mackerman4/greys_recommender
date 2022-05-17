"""
Streamlit Grey's Anatomy Episode Recommender

"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import json
import time

# Open csv files of recs for all episodes
with open('file_names.json') as json_file:
    file_names = json.load(json_file)
    

    
st.write('''
# What Episode of Grey's Anatomy Should You Watch Next?

''')
st.write(
'''
## Episode Guide

''')

# Show dataframe of all episodes
all_episodes = pd.read_csv('all_episodes.csv')
st.dataframe(all_episodes)

# User selects episode from dropdown menu
ep_list = []
for key in file_names:
    ep_list.append(key)

ep_select = st.selectbox('Choose an episode from the list above:', (ep_list))

# Read in and show recommendations
filename = file_names[ep_select]
recs = pd.read_csv(filename)
recs.index+=1

with st.spinner('Wait for it...'):
    time.sleep(3)
st.success('Done!')

st.write('''
## Here are your 10 most recommended episodes:
''')
st.dataframe(recs)




