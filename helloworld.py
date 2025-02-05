import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='centered') #centralizar tudo o que eu colocar no código para a página.

reviews = pd.read_csv(r'C:\Users\Administrator\Desktop\asimov\customer reviews.csv')
top100 = pd.read_csv(r'C:\Users\Administrator\Desktop\asimov\Top-100 Trending Books.csv') #ler, verificar arquivo e indexar as informações contidas no arquivo csv
top100 = top100.rename(columns = {
    'book title': 'Titulo do Livro',
    'book price': 'Preço do Livro',
    'year of publication': 'Ano de publicação',
    'rating': 'Avaliação',
    'genre': 'Genero',
    'author': 'Autor',
    'url': 'Link',
    'Rank': 'Ranking'
})
precom = top100['Preço do Livro'].max() # preço máximo
precomin = top100['Preço do Livro'].min() # preço minimo
pee = st.sidebar.slider('Preço', precomin, precom, precom) # coloca o preço minimo e preço máximos definido na variavel
#lá em cima, o último precom mostra que vai comçar a mostrar com o valor maior, se a ultima variavel fosse precomin iria começar a mostrar o menor valor primeiro.
books = top100[top100['Preço do Livro'] <= pee]

st.divider()
figura = px.bar(books['Ano de publicação'].value_counts(), labels = {'index': 'Ano de publicação', 'value': 'Tabela de contagem'})
figura2 = px.histogram(books['Preço do Livro'], labels = {'index': 'Preço do livro', 'value': 'Contador'})

cont1, cont2 = st.columns(2)
cont1.plotly_chart(figura, use_container_width=True)
cont2.plotly_chart(figura2, use_container_width=True)

st.divider()
st.dataframe(books)
st.line_chart()