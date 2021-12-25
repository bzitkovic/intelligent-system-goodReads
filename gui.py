from tkinter import Tk, Entry, Label, Button
from visualization import get_box_plot, get_heat_map, get_histogram_genres, get_tabloo_table

def set_gui(books, dataframe):
    window = Tk()
    window.title("Good Reads")

    ent_number_of_pages = Entry(
        window,
        width=15
    )
    
    ent_number_of_pages.grid(
        row=1,
        column=0, 
        padx=25, 
        pady=10, 
        sticky="W"
    )

    lbl_number = Label(
        window, 
        font=(
            "Ariel", 
            12
        ), 
        bg="#7878ab", 
        text="Number of pages:"
    )

    lbl_number.grid(
        row=0, 
        column=0, 
        padx=20, 
        sticky="W"
    )

    btn_get_number_of_pages = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_heat_map(dataframe),
    )

    btn_get_number_of_pages.grid(
        row=1, 
        column=1
    )

    lbl_get_heat_map = Label(
        window, 
        font=(
            "Ariel", 
            12
        ), 
        bg="#7878ab", 
        text="Get heat map"
    )

    lbl_get_heat_map.grid(
        row=2, 
        column=0, 
        padx=20, 
        pady=10, 
        sticky="W"
    )

    btn_get_heat_map = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_heat_map(dataframe),
    )

    btn_get_heat_map.grid(
        row=2, 
        column=1
    )

    lbl_get_boxplot_rating = Label(
        window, 
        font=(
            "Ariel",
             12
        ), 
        bg="#7878ab", 
        text="Get boxplot for rating"
    )

    lbl_get_boxplot_rating.grid(
        row=3, 
        column=0, 
        padx=20, 
        pady=10, 
        sticky="W"
    )

    btn_get_boxplot_rating = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_box_plot(
            dataframe,
            "rating"
        ),
    )

    btn_get_boxplot_rating.grid(
        row=3,
        column=1
    )

    lbl_get_boxplot_reviews = Label(
        window, 
        font=(
            "Ariel", 
            12
        ), 
        bg="#7878ab", 
        text="Get boxplot for reviews"
    )

    lbl_get_boxplot_reviews.grid(
        row=4, 
        column=0, 
        padx=20, 
        pady=10, 
        sticky="W"
    )

    btn_get_boxplot_reviews = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_box_plot(
            dataframe, 
            "reviews"
        ),
    )

    btn_get_boxplot_reviews.grid(
        row=4, 
        column=1, 
        padx=20, 
        pady=10
    )

    lbl_get_boxplot_total_ratings = Label(
        window,
        font=("Ariel", 12),
        bg="#7878ab",
        text="Get boxplot for total ratings",
    )

    lbl_get_boxplot_total_ratings.grid(
        row=5, 
        column=0, 
        padx=20, 
        pady=10, 
        sticky="W"
    )

    btn_get_boxplot_total_ratings = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_box_plot(
            dataframe,
            "totalratings"
        ),
    )

    btn_get_boxplot_total_ratings.grid(
        row=5,
        column=1,
        padx=20, 
        pady=10
    )

    lbl_get_top_genres = Label(
        window, 
        font=(
            "Ariel",
            12
        ), 
        bg="#7878ab", 
        text="Get top 8 genres"
    )

    lbl_get_top_genres.grid(
        row=6, 
        column=0, 
        padx=20, 
        pady=10, 
        sticky="W"
    )

    btn_get_top_genres = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_histogram_genres(books),
    )

    btn_get_top_genres.grid(
        row=6, 
        column=1, 
        padx=20, 
        pady=10
    )

    lbl_get_tabloo_table = Label(
        window, 
        font=(
            "Ariel",
            12
        ), 
        bg="#7878ab", 
        text="Get table for data"
    )

    lbl_get_tabloo_table.grid(
        row=7, 
        column=0, 
        padx=20, 
        pady=10, 
        sticky="W"
    )

    btn_get_tabloo_table = Button(
        window,
        text="➔",
        width=6,
        bd=3,
        bg="#78ab7c",
        command=lambda: get_tabloo_table( window, dataframe),
    )

    btn_get_tabloo_table.grid(
        row=7, 
        column=1, 
        padx=20, 
        pady=10
    )

    return window
