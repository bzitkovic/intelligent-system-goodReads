from tkinter import Tk, Entry, Label, Button
from visualization import get_box_plot, get_heat_map, get_histogram_genres


def SetGUI(books, df):
    window = Tk()
    window.title("Good Reads")

    entNumberOfPages = Entry(window, width=15)
    entNumberOfPages.grid(row=1, column=0, padx=25, pady=10, sticky="W")

    lblNumber = Label(window, font=("Ariel", 12), bg="#7878ab", text="Number of pages:")
    lblNumber.grid(row=0, column=0, padx=20, sticky="W")

    btnGetNumberOfPages = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_heat_map(df),
    )
    btnGetNumberOfPages.grid(row=1, column=1)

    lblGetHeatMap = Label(window, font=("Ariel", 12), bg="#7878ab", text="Get heat map")
    lblGetHeatMap.grid(row=2, column=0, padx=20, pady=10, sticky="W")

    btnGetHeatMap = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_heat_map(df),
    )
    btnGetHeatMap.grid(row=2, column=1)

    lblGetBoxplotRating = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Get boxplot for rating"
    )
    lblGetBoxplotRating.grid(row=3, column=0, padx=20, pady=10, sticky="W")

    btnGetBoxplotRating = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_box_plot(df, "rating"),
    )
    btnGetBoxplotRating.grid(row=3, column=1)

    lblGetBoxplotReviews = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Get boxplot for reviews"
    )
    lblGetBoxplotReviews.grid(row=4, column=0, padx=20, pady=10, sticky="W")

    btnGetBoxplotReviews = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_box_plot(df, "reviews"),
    )
    btnGetBoxplotReviews.grid(row=4, column=1, padx=20, pady=10)

    lblGetBoxplotTotalRatings = Label(
        window,
        font=("Ariel", 12),
        bg="#7878ab",
        text="Get boxplot for total ratings",
    )
    lblGetBoxplotTotalRatings.grid(row=5, column=0, padx=20, pady=10, sticky="W")

    btnGetBoxplotTotalRatings = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_box_plot(df, "totalratings"),
    )
    btnGetBoxplotTotalRatings.grid(row=5, column=1, padx=20, pady=10)

    lblGetTopGenres = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Get top 8 genres"
    )
    lblGetTopGenres.grid(row=6, column=0, padx=20, pady=10, sticky="W")

    btnGetTopGenres = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_histogram_genres(books),
    )
    btnGetTopGenres.grid(row=6, column=1, padx=20, pady=10)

    return window
