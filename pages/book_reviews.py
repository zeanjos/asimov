import streamlit as st
import pandas as pd
st.set_page_config(layout='centered')

reviews = pd.read_csv(r'C:\Users\Administrator\Desktop\asimov\customer reviews.csv')
top100 = pd.read_csv(r'C:\Users\Administrator\Desktop\asimov\Top-100 Trending Books.csv')

books = top100['book title'].unique()
book = st.sidebar.selectbox('books', books)
dfbook = top100[top100['book title'] == book]
df_reviews = reviews[reviews['book name'] == book]
st.divider()
bt = dfbook['book title'].iloc[0]
bg = dfbook['genre'].iloc[0]
bp = f"${dfbook['book price'].iloc[0]}"
br = dfbook['rating'].iloc[0]
by = dfbook['year of publication'].iloc[0]
dfbook
df_reviews
st.title(bt)
st.subheader(bg)
col1, col2, col3 = st.columns(3)
col1.metric('Price', bp)
col2.metric('Genre', bg)
col3.metric('Year of publication', by)

for row in reviews.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])
