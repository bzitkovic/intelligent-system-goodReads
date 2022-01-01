from pandas import read_csv, DataFrame
from scipy.sparse import data
from models import Book
from gui import GUI
from decision_tree_model import make_decision_tree, make_prediction_total_rating
from tkinter import Tk
from visualization import get_decision_tree

dataframe = read_csv("GoodReadsData.csv", delimiter=",")

# Remove all rows that contain NULL values
dataframe.dropna(inplace=True)


books = []

for index, row in dataframe.iterrows():
    author = row["author"]
    book_format = row["bookformat"]
    description = row["desc"]
    genres = row["genre"].split(",")
    isbn = row["isbn"]
    link = row["link"]
    pages = row["pages"]
    rating = row["rating"]
    reviews = row["reviews"]
    title = row["title"]
    total_ratings = row["totalratings"]

    new_book = Book(
        author,
        book_format,
        description,
        genres,
        isbn,
        link,
        pages,
        rating,
        reviews,
        title,
        total_ratings,
    )

    books.append(new_book)

if __name__ == "__main__":

    # above_total_rating = dataframe[(dataframe['totalratings'] > total_rating) & (dataframe['reviews'] == 1214)]

    decision_tree = make_decision_tree(dataframe)

    window = Tk()
    gui = GUI(window, books, dataframe, decision_tree)
    gui.window.mainloop()
