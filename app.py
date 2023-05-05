import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np

st.title("Movie Ratings and Reviews :cinema:", )

"""
You can even add and remove rows or columns - cool right?
"""

# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.experimental_connection('snowpark')

# Perform query.
orig_df = conn.query('SELECT * from mytable;', ttl=6000)


df = st.experimental_data_editor(orig_df,num_rows="dynamic")
df["RATING"] = [int(x) for x in df["RATING"]]
st.write(" ")
st.write("Movie by Rating")

fig = plt.figure(figsize=(20, 12));
#plt.xticks(rotation=90)
sns.set(font_scale = 2)
sns.barplot(data=df, y="MOVIE", x="RATING", orient='h')
st.pyplot(fig)

st.write("We know streamlit loves 💖snowflake so much, so let's make wordclouds with them 😉")

design = st.selectbox("Choose wordcloud design", ["Streamlit", "Snowflake"])

if design=="Streamlit":
    draw = "streamlit logo2.jpg"
else:
    draw = "snowflake.png"

comment_words = ''
stopwords = set(STOPWORDS)
 
# iterate through the csv file
for val in df.REVIEW:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "
 

mask = np.array(Image.open(draw))
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                mask=mask,
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)

fig3 = plt.figure(figsize=(20, 12));
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(fig3)