import pandas
from models import Book
import matplotlib.pyplot as plt
import numpy as np

def GetHeatMap(df):
    corr = df.corr()
    fig, ax = plt.subplots()
    im = ax.imshow(corr.values)

    ax.set_xticks(np.arange(len(corr.columns)))
    ax.set_yticks(np.arange(len(corr.columns)))
    ax.set_xticklabels(corr.columns)
    ax.set_yticklabels(corr.columns)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")
    plt.show()

def GetBoxPlot(df, columnName):
    if(columnName == 'rating'):
        df.boxplot(column=['rating'], grid=False, showfliers=False)
    elif(columnName == 'reviews'):
        df.boxplot(column=['reviews'], grid=False, showfliers=False)
    else:
        df.boxplot(column=['totalratings'], grid=False, showfliers=False)
    plt.show()

def GetHistogramGenres(books):
    genres = {}

    for book in books:
        for genre in book.genre:  
            if(genre not in genres.keys()):           
                genres[genre] = 1
            else:
                genres[genre] += 1

    sortedGenres = sorted(genres.items(), key=lambda item: item[1], reverse=True)[:8]
    dfGenres = pandas.DataFrame(sortedGenres, columns=['Genre', 'Frequency'])
    dfGenres.plot(kind='bar', x='Genre')

    plt.show()