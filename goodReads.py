import pandas
from models import Book
from visualization import *
from gui import *
import matplotlib.pyplot as plt
import numpy as np

df = pandas.read_csv("GoodReadsData.csv", delimiter=',')

# Remove all rows that contain NULL values
df.dropna(inplace=True)

books = []

for index, row in df.iterrows():
    genres = []

    author = row['author']
    bookFormat = row['bookformat']
    description = row['desc']
    genres = row['genre'].split(',')
    isbn = row['isbn']
    link = row['link']
    pages = row['pages']
    rating = row['rating']
    reviews = row['reviews']
    title = row['title']
    totalRatings = row['totalratings']

    book = Book(author, bookFormat, description, genres, isbn, link, pages, rating, reviews, title, totalRatings)    
    books.append(book)

gui = SetGUI(books, df)
gui.geometry('550x300')
gui.configure(bg='#7878ab')
gui.mainloop()





