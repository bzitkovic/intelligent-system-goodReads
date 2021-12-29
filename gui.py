from tkinter import (
    Entry,
    Label,
    Button,
    Checkbutton,
    IntVar,
    StringVar,
    Frame,
    Toplevel,
    font,
)
from tkinter.constants import CENTER
from visualization import (
    get_box_plot,
    get_heat_map,
    get_histogram_genres,
    get_tabloo_table,
)

WINDOW_TITLE = "Good Reads"
WINDOW_X_OFFSET = int(1080 / 3 - 100)
WINDOW_Y_OFFSET = int(1920 / 2 - 400)
WINDOW_IS_RESIZABLE = False
FONT_STYLE = "Ariel"
FONT_SIZE = 11
COLOR_PURPLE = "#7878ab"
COLOR_GREEN = "#78ab7c"


class GUI:
    def __init__(self, window, books, dataframe, decision_tree):
        self.window = window
        self.books = books
        self.dataframe = dataframe
        self.decision_tree = decision_tree
        self.configure_window()
        self.create_variables()
        self.create_UI()

    def configure_window(self):
        self.window.title(WINDOW_TITLE)
        self.window.geometry(f"800x400+{WINDOW_Y_OFFSET}+{WINDOW_X_OFFSET}")
        self.window.configure(bg=COLOR_PURPLE)
        self.window.resizable(WINDOW_IS_RESIZABLE, WINDOW_IS_RESIZABLE)

        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family=FONT_STYLE, size=FONT_SIZE)

    def create_variables(self):
        self.chk1_variable = IntVar()
        self.chk2_variable = IntVar()
        self.chk3_variable = IntVar()
        self.chk4_variable = IntVar()
        self.chk5_variable = IntVar()
        self.chk6_variable = IntVar()

        self.ent_number_of_pages_variable = StringVar()
        self.ent_minimum_rating_variable = StringVar()
        self.ent_minimum_reviews_variable = StringVar()
        self.ent_minimum_total_ratings_variable = StringVar()

        self.chk_options = [
            self.chk1_variable,
            self.chk2_variable,
            self.chk3_variable,
            self.chk4_variable,
            self.chk5_variable,
            self.chk6_variable,
        ]

        self.ent_values = [
            self.ent_number_of_pages_variable,
            self.ent_minimum_rating_variable,
            self.ent_minimum_reviews_variable,
            self.ent_minimum_total_ratings_variable,
        ]

    def create_UI(self):
        self.user_entry_frame = Frame(self.window, bg=COLOR_PURPLE)
        self.user_entry_frame.grid(row=0, column=1, pady=10, sticky="NEWS")

        self.visualization_frame = Frame(self.window, bg=COLOR_PURPLE)
        self.visualization_frame.grid(row=0, rowspan=2, column=0, pady=10, sticky="NEWS")

        self.checkbox_frame = Frame(self.window, bg=COLOR_PURPLE)
        self.checkbox_frame.grid(row=1, column=1, sticky="NEWS")

        self.recommend_frame = Frame(self.window, bg=COLOR_PURPLE)
        self.recommend_frame.grid(row=2, column=0, columnspan=2, pady=35, sticky="NEWS")

        self.create_visualization()
        self.create_user_entry()
        self.create_checkboxes()
        self.create_recommend_button()

    def create_user_entry(self):
        self.lbl_number = Label(self.user_entry_frame, bg=COLOR_PURPLE, text="Number of pages:")
        self.lbl_number.grid(row=0, column=0, padx=20, sticky="W")

        self.ent_number_of_pages = Entry(
            self.user_entry_frame,
            width=30,
            textvariable=self.ent_number_of_pages_variable,
        )
        self.ent_number_of_pages.grid(row=1, column=0, padx=25, pady=10, sticky="W")

        self.lbl_rating = Label(self.user_entry_frame, bg=COLOR_PURPLE, text="Minimum rating:")
        self.lbl_rating.grid(row=2, column=0, padx=20, sticky="W")

        self.ent_rating = Entry(
            self.user_entry_frame,
            width=30,
            textvariable=self.ent_minimum_rating_variable,
        )
        self.ent_rating.grid(row=3, column=0, padx=25, pady=10, sticky="W")

        self.lbl_reviews = Label(
            self.user_entry_frame,
            bg=COLOR_PURPLE,
            text="Minimum number od reviews:",
        )
        self.lbl_reviews.grid(row=0, column=1, padx=20, sticky="W")

        self.ent_reviews = Entry(
            self.user_entry_frame,
            width=30,
            textvariable=self.ent_minimum_reviews_variable,
        )
        self.ent_reviews.grid(row=1, column=1, padx=25, pady=10, sticky="W")

        self.lbl_total_ratings = Label(
            self.user_entry_frame,
            bg=COLOR_PURPLE,
            text="Minimum number od total ratings:",
        )
        self.lbl_total_ratings.grid(row=2, column=1, padx=20, sticky="W")

        self.ent_total_ratings = Entry(
            self.user_entry_frame,
            width=30,
            textvariable=self.ent_minimum_total_ratings_variable,
        )
        self.ent_total_ratings.grid(row=3, column=1, padx=25, pady=10, sticky="W")

    def create_checkboxes(self):
        self.lbl_genre = Label(self.checkbox_frame, bg=COLOR_PURPLE, text="Select prefered genre:")
        self.lbl_genre.grid(row=0, column=0, padx=20, sticky="W")

        self.chk1 = Checkbutton(
            self.checkbox_frame,
            bg=COLOR_PURPLE,
            text="Romance",
            variable=self.chk1_variable,
        )
        self.chk1.grid(row=1, column=0, padx=25, pady=5, sticky="W")

        self.chk2 = Checkbutton(
            self.checkbox_frame,
            bg=COLOR_PURPLE,
            text="Fiction",
            variable=self.chk2_variable,
        )
        self.chk2.grid(row=1, column=1, pady=5, sticky="W")

        self.chk3 = Checkbutton(
            self.checkbox_frame,
            bg=COLOR_PURPLE,
            text="Fantasy",
            variable=self.chk3_variable,
        )
        self.chk3.grid(row=2, column=0, padx=25, pady=5, sticky="W")

        self.chk4 = Checkbutton(
            self.checkbox_frame,
            bg=COLOR_PURPLE,
            text="Nonfiction",
            variable=self.chk4_variable,
        )
        self.chk4.grid(row=2, column=1, pady=5, sticky="W")

        self.chk5 = Checkbutton(
            self.checkbox_frame,
            bg=COLOR_PURPLE,
            text="History",
            variable=self.chk5_variable,
        )
        self.chk5.grid(row=3, column=0, padx=25, pady=5, sticky="W")

        self.chk6 = Checkbutton(
            self.checkbox_frame,
            bg=COLOR_PURPLE,
            text="Childrens",
            variable=self.chk6_variable,
        )
        self.chk6.grid(row=3, column=1, pady=5, sticky="W")

    def create_visualization(self):
        self.lbl_get_heat_map = Label(self.visualization_frame, bg=COLOR_PURPLE, text="Get heat map")
        self.lbl_get_heat_map.grid(row=0, column=0, padx=20, pady=10, sticky="W")

        self.btn_get_heat_map = Button(
            self.visualization_frame,
            text="➔",
            width=6,
            bd=3,
            bg=COLOR_GREEN,
            command=lambda: get_heat_map(self.dataframe),
        )
        self.btn_get_heat_map.grid(row=0, column=1)

        self.lbl_get_boxplot_rating = Label(self.visualization_frame, bg=COLOR_PURPLE, text="Get boxplot for rating")
        self.lbl_get_boxplot_rating.grid(row=1, column=0, padx=20, pady=10, sticky="W")

        self.btn_get_boxplot_rating = Button(
            self.visualization_frame,
            text="➔",
            width=6,
            bd=3,
            bg=COLOR_GREEN,
            command=lambda: get_box_plot(self.dataframe, "rating"),
        )
        self.btn_get_boxplot_rating.grid(row=1, column=1)

        self.lbl_get_boxplot_reviews = Label(
            self.visualization_frame,
            bg=COLOR_PURPLE,
            text="Get boxplot for reviews",
        )
        self.lbl_get_boxplot_reviews.grid(row=2, column=0, padx=20, pady=10, sticky="W")

        self.btn_get_boxplot_reviews = Button(
            self.visualization_frame,
            text="➔",
            width=6,
            bd=3,
            bg=COLOR_GREEN,
            command=lambda: get_box_plot(self.dataframe, "reviews"),
        )
        self.btn_get_boxplot_reviews.grid(row=2, column=1)

        self.lbl_get_boxplot_total_ratings = Label(
            self.visualization_frame,
            bg=COLOR_PURPLE,
            text="Get boxplot for total ratings",
        )
        self.lbl_get_boxplot_total_ratings.grid(row=3, column=0, padx=20, pady=10, sticky="W")

        self.btn_get_boxplot_total_ratings = Button(
            self.visualization_frame,
            text="➔",
            width=6,
            bd=3,
            bg=COLOR_GREEN,
            command=lambda: get_box_plot(self.dataframe, "totalratings"),
        )
        self.btn_get_boxplot_total_ratings.grid(row=3, column=1)

        self.lbl_get_top_genres = Label(self.visualization_frame, bg=COLOR_PURPLE, text="Get top 8 genres")
        self.lbl_get_top_genres.grid(row=4, column=0, padx=20, pady=10, sticky="W")

        self.btn_get_top_genres = Button(
            self.visualization_frame,
            text="➔",
            width=6,
            bd=3,
            bg=COLOR_GREEN,
            command=lambda: get_histogram_genres(self.books),
        )
        self.btn_get_top_genres.grid(row=4, column=1)

        self.lbl_get_tabloo_table = Label(self.visualization_frame, bg=COLOR_PURPLE, text="Get table for data")
        self.lbl_get_tabloo_table.grid(row=5, column=0, padx=20, pady=10, sticky="W")

        self.btn_get_tabloo_table = Button(
            self.visualization_frame,
            text="➔",
            width=6,
            bd=3,
            bg=COLOR_GREEN,
            command=lambda: get_tabloo_table(self.dataframe),
        )
        self.btn_get_tabloo_table.grid(row=5, column=1, padx=20, pady=10)

    def create_recommend_button(self):
        self.btn_get_user_entry = Button(
            self.recommend_frame,
            text="Recommend me a book",
            width=25,
            bd=3,
            bg=COLOR_GREEN,
            command=lambda: self.recommend_books(),
        )
        self.btn_get_user_entry.pack()

    def recommend_books(self):
        checked_options = self.get_checked_options()
        # TODO: get entry values

        # TODO: create dataframe with recommended books
        # TODO: pass dataframe and message to create_popup
        self.create_popup(
            self.dataframe,
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
        )

    def create_popup(self, dataframe, message):
        self.popup_window = Toplevel(self.window, bg=COLOR_PURPLE)
        self.popup_window.title("Recommended books")
        self.popup_window.geometry(f"600x200+{WINDOW_Y_OFFSET+100}+{WINDOW_X_OFFSET+75}")

        self.popup_frame = Frame(self.popup_window, bg=COLOR_PURPLE)
        self.popup_frame.grid(row=0, column=0, pady=30, padx=55)

        self.recommended_message = Label(
            self.popup_frame,
            text=message,
            justify=CENTER,
            bg=COLOR_PURPLE,
            wraplength=500,
        )
        self.recommended_message.pack()

        self.popup_button = Button(
            self.popup_window,
            text="Show recommendations",
            width=25,
            bd=3,
            bg=COLOR_GREEN,
            command=lambda: get_tabloo_table(dataframe),
        )
        self.popup_button.grid(row=1, column=0)

    def get_checked_options(self):
        chk_checked_values = []

        if self.chk_options[0].get() == 1:
            chk_checked_values.append("Romance")
        if self.chk_options[1].get() == 1:
            chk_checked_values.append("Fiction")
        if self.chk_options[2].get() == 1:
            chk_checked_values.append("Fantasy")
        if self.chk_options[3].get() == 1:
            chk_checked_values.append("Nonfiction")
        if self.chk_options[4].get() == 1:
            chk_checked_values.append("History")
        if self.chk_options[5].get() == 1:
            chk_checked_values.append("Childrens")

        return chk_checked_values
