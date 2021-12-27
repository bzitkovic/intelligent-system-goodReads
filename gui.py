from tkinter import Tk, Entry, Label, Button, Checkbutton, IntVar, StringVar
from visualization import (
    get_box_plot,
    get_heat_map,
    get_histogram_genres,
    get_tabloo_table,
)
from recommendation import get_all_user_options


def set_gui(books, dataframe):
    window = Tk()
    window.title("Good Reads")

    chk1_variable = IntVar()
    chk2_variable = IntVar()
    chk3_variable = IntVar()
    chk4_variable = IntVar()
    chk5_variable = IntVar()
    chk6_variable = IntVar()

    ent_number_of_pages_variable = StringVar()
    ent_minimum_rating_variable = StringVar()
    ent_minimum_reviews_variable = StringVar()
    ent_minimum_total_ratings_variable = StringVar()

    chk_options = [
        chk1_variable,
        chk2_variable,
        chk3_variable,
        chk4_variable,
        chk5_variable,
        chk6_variable,
    ]

    ent_values = [ent_number_of_pages_variable]

    # User entry
    lbl_number = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Number of pages:"
    )

    lbl_number.grid(row=0, column=2, padx=20, sticky="W")

    ent_number_of_pages = Entry(
        window, width=20, textvariable=ent_number_of_pages_variable
    )

    ent_number_of_pages.grid(row=1, column=2, padx=25, pady=10, sticky="W")

    lbl_rating = Label(window, font=("Ariel", 12), bg="#7878ab", text="Minimun rating:")

    lbl_rating.grid(row=2, column=2, padx=20, sticky="W")

    ent_rating = Entry(window, width=20, textvariable=ent_minimum_rating_variable)

    ent_rating.grid(row=3, column=2, padx=25, pady=10, sticky="W")

    lbl_reviews = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Minimun number od reviews:"
    )

    lbl_reviews.grid(row=0, column=3, padx=20, sticky="W")

    ent_reviews = Entry(window, width=20, textvariable=ent_minimum_reviews_variable)

    ent_reviews.grid(row=1, column=3, padx=25, pady=10, sticky="W")

    lbl_total_ratings = Label(
        window,
        font=("Ariel", 12),
        bg="#7878ab",
        text="Minimun number od total ratings:",
    )

    lbl_total_ratings.grid(row=2, column=3, padx=20, sticky="W")

    ent_total_ratings = Entry(
        window, width=20, textvariable=ent_minimum_total_ratings_variable
    )

    ent_total_ratings.grid(row=3, column=3, padx=25, pady=10, sticky="W")

    lbl_genre = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Select prefered genre:"
    )

    lbl_genre.grid(row=4, column=2, padx=20, sticky="W")

    chk1 = Checkbutton(window, text="Romance", variable=chk1_variable)

    chk1.grid(row=5, column=2, padx=25, pady=10, sticky="W")

    chk2 = Checkbutton(window, text="History", variable=chk2_variable)

    chk2.grid(row=5, column=2, pady=10, sticky="E")

    chk3 = Checkbutton(window, text="Nonfiction", variable=chk3_variable)

    chk3.grid(row=6, column=2, padx=25, pady=10, sticky="W")

    chk4 = Checkbutton(window, text="Fantasy", variable=chk4_variable)

    chk4.grid(row=6, column=2, pady=10, sticky="E")

    chk5 = Checkbutton(window, text="Fiction", variable=chk5_variable)

    chk5.grid(row=7, column=2, padx=25, pady=10, sticky="W")

    chk6 = Checkbutton(window, text="Childrens", variable=chk6_variable)

    chk6.grid(row=7, column=2, pady=10, sticky="E")

    btn_get_user_entry = Button(
        window,
        text="Recommend me a book",
        width=25,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_all_user_options(chk_options, ent_values, dataframe),
    )

    btn_get_user_entry.grid(row=7, column=3, padx=25, pady=10, sticky="W")

    # Visualization
    lbl_get_heat_map = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Get heat map"
    )

    lbl_get_heat_map.grid(row=0, column=0, padx=20, pady=10, sticky="W")

    btn_get_heat_map = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_heat_map(dataframe),
    )

    btn_get_heat_map.grid(row=0, column=1)

    lbl_get_boxplot_rating = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Get boxplot for rating"
    )

    lbl_get_boxplot_rating.grid(row=1, column=0, padx=20, pady=10, sticky="W")

    btn_get_boxplot_rating = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_box_plot(dataframe, "rating"),
    )

    btn_get_boxplot_rating.grid(row=1, column=1)

    lbl_get_boxplot_reviews = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Get boxplot for reviews"
    )

    lbl_get_boxplot_reviews.grid(row=2, column=0, padx=20, pady=10, sticky="W")

    btn_get_boxplot_reviews = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_box_plot(dataframe, "reviews"),
    )

    btn_get_boxplot_reviews.grid(row=2, column=1, padx=20, pady=10)

    lbl_get_boxplot_total_ratings = Label(
        window,
        font=("Ariel", 12),
        bg="#7878ab",
        text="Get boxplot for total ratings",
    )

    lbl_get_boxplot_total_ratings.grid(row=3, column=0, padx=20, pady=10, sticky="W")

    btn_get_boxplot_total_ratings = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_box_plot(dataframe, "totalratings"),
    )

    btn_get_boxplot_total_ratings.grid(row=3, column=1, padx=20, pady=10)

    lbl_get_top_genres = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Get top 8 genres"
    )

    lbl_get_top_genres.grid(row=4, column=0, padx=20, pady=10, sticky="W")

    btn_get_top_genres = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_histogram_genres(books),
    )

    btn_get_top_genres.grid(row=4, column=1, padx=20, pady=10)

    lbl_get_tabloo_table = Label(
        window, font=("Ariel", 12), bg="#7878ab", text="Get table for data"
    )

    lbl_get_tabloo_table.grid(row=5, column=0, padx=20, pady=10, sticky="W")

    btn_get_tabloo_table = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_tabloo_table(dataframe),
    )

    btn_get_tabloo_table.grid(row=5, column=1, padx=20, pady=10)

    return window
