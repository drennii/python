import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

#Streamlit app title and des



if selected_author != "All":
    filtered_books_df = filtered_books_df[filtered_books_df['Author'] == selected_author ]
if selected_year  !="All":
    filtered_year_df = filtered_books_df[filtered_books_df['Year'] == selected_author]
if selected_genre != "All":
  filtered_genre_df = filtered_books_df[filtered_books_df['Genre'] == selected_author]

filtered_books_df = filtered_books_df[
    (filtered_books_df['User Rating'] >= min_rating) & (filtered_books_df['Price'] <= max_price )
]

st.subheader("Summary Statistics")
total_books = filtered_books_df.shape[0]
unique_titles = filtered_books_df['Name'].nunique()
average_rating = filtered_books_df['User Rating'].mean()
average_price = filtered_books_df['Price'].mean()

col1 , col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Total Titles", total_titles)
col3.metric("Total Rating", total_rating)
col4.metric("Total Price", total_price)

st.subheader("Dataset Preview")
st.write(filtered_books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Selling Books")
    top_titles = filtered_books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("Top 10 Authors")
    top_authors = filtered_books_df['Authors'].value_counts().head(10)
    st.bar_chart(authors)

st.subheader("Genre Distribution")
fig = px.pie(filtered_books_df, names='Genre', title='Most Liked Genre (2009-2022)', color='Genre',
             color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of Fiction vs Non Fiction Books Over the Years")
size = filtered_books_df.groupby(['Year','Genre']).size().reset_index(name='Counts')
fig = px.bar(size, x='Year', y='Counts', color='Genre', title='Number of Fiction Books from 2009 to 2022',
             color_discrete_sequence=px.colors.sequential.Plasma, barmode='group')
st.plotly_chart(fig)

st.subheader("Top 15 authors by counts of books published (2009-2022)")
top_authors = filtered_books_df['Author'].value.counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']
fig = px.bar(top_authors , x='Count' , y='Author' , orientation='h',
          title = 'Top 15 Authors by counts of books published',
          labels={'Count':'Counts of Books published' ,  'Author': 'Author'}
          color = 'Count', color_continous_scale=px.colors.sequential.Plasma)

st.plotly_chart(fig)

st.subheader('Filter Data by Genre')
genre_filter = st.selectbox("Select Genre", filtered_books_df['Genre'].unique())
filtered_genre_df = filtered_books_df[filtered_books_df['Genre'] == genre_filter]
st.write(filtered_genre_df)