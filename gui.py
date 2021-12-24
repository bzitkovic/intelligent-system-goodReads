import tkinter as tk
from tkinter import ttk
from visualization import *

def SetGUI(books, df):
        window = tk.Tk()
        window.title('GoodReads')
        
        entNumberOfPages = tk.Entry(master=window, width=15)
        entNumberOfPages.grid(row=1, column=0, padx=25, pady=10, sticky='W')

        lblNumber = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Number of pages:')
        lblNumber.grid(row=0, column=0, padx=20, sticky='W')       

        btnGetNumberOfPages = tk.Button(
            master = window,
            text = '➔',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
           command = lambda: GetHeatMap(df)
        )
        btnGetNumberOfPages.grid(row=1, column=1)

        lblGetHeatMap = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Get heat map')
        lblGetHeatMap.grid(row=2, column=0, padx=20, pady=10, sticky='W')

        btnGetHeatMap = tk.Button(
            master = window,
            text = '➔',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: GetHeatMap(df)
        )
        btnGetHeatMap.grid(row=2, column=1)      

        lblGetBoxplotRating = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Get boxplot for rating')
        lblGetBoxplotRating.grid(row=3, column=0, padx=20, pady=10, sticky='W')

        btnGetBoxplotRating = tk.Button(
            master = window,
            text = '➔',            
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: GetBoxPlot(df, 'rating')
        )
        btnGetBoxplotRating.grid(row=3, column=1)

        lblGetBoxplotReviews =  tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Get boxplot for reviews')
        lblGetBoxplotReviews.grid(row=4, column=0, padx=20, pady=10, sticky='W')

        btnGetBoxplotReviews = tk.Button(
            master = window,
            text = '➔',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: GetBoxPlot(df, 'reviews')
        )
        btnGetBoxplotReviews.grid(row=4, column=1, padx=20, pady=10)

        lblGetBoxplotTotalRatings = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Get boxplot for total ratings')
        lblGetBoxplotTotalRatings.grid(row=5, column=0, padx=20, pady=10, sticky='W')

        btnGetBoxplotTotalRatings = tk.Button(
            master = window,
            text = '➔',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: GetBoxPlot(df, 'totalratings')
        )
        btnGetBoxplotTotalRatings.grid(row=5, column=1, padx=20, pady=10)

        lblGetTopGenres = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Get top 8 genres')
        lblGetTopGenres.grid(row=6, column=0, padx=20, pady=10, sticky='W')

        btnGetTopGenres = tk.Button(
            master = window,
            text = '➔',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: GetHistogramGenres(books)
        )
        btnGetTopGenres.grid(row=6, column=1, padx=20, pady=10)

        return window