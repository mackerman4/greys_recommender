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

st.markdown("Grey's Anatomy episodes can be distilled into 13 topics based on their summaries. The below graphs reveal how these topics changed over the years.")
from PIL import Image
image = Image.open('tableau_graphs.png')
st.image(image, caption='Topic breakdowns of episodes')

st.markdown('Find episodes most similar to your favorite episodes with this recommender. Just use the episode guide to find your favorite episode and select it from the dropdown menu below!')

st.write(
'''
## Episode Guide

''')
st.caption('_Note that Season/Episode refers first to season, then episode, which is led by a zero if single digit (e.g. 101 is season 1 episode 1)._')

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
