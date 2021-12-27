from pandas import DataFrame
import matplotlib.pyplot as plt
from numpy import arange, around
import tabloo


def get_heat_map(dataframe):
    corr = dataframe.corr()
    fig, ax = plt.subplots()
    im = ax.imshow(corr.values)

    ax.set_xticks(arange(len(corr.columns)))
    ax.set_yticks(arange(len(corr.columns)))
    ax.set_xticklabels(corr.columns)
    ax.set_yticklabels(corr.columns)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=25, ha="right", rotation_mode="anchor")

    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            ax.text(
                j,
                i,
                around(corr.iloc[i, j], decimals=2),
                ha="center",
                va="center",
                color="black",
            )

    plt.show()


def get_box_plot(dataframe, columnName):
    if columnName == "rating":
        dataframe.boxplot(column=["rating"], grid=False, showfliers=False)
    elif columnName == "reviews":
        dataframe.boxplot(column=["reviews"], grid=False, showfliers=False)
    else:
        dataframe.boxplot(column=["totalratings"], grid=False, showfliers=False)

    plt.show()


def get_histogram_genres(books):
    genres = {}

    for book in books:
        for genre in book.genre:
            if genre not in genres.keys():
                genres[genre] = 1
            else:
                genres[genre] += 1

    sorted_genres = sorted(genres.items(), key=lambda item: item[1], reverse=True)[:8]
    dataframe_genres = DataFrame(sorted_genres, columns=["Genre", "Frequency"])
    dataframe_genres.plot(kind="bar", x="Genre")

    plt.show()


def get_tabloo_table(window, dataframe):
    window.destroy()
    tabloo.show(dataframe)
