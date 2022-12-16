from tkinter import *
import requests
from tkinter import messagebox


def fetchNews():
    country = country_text.get().lower()
    cc = 'none'
    country_code_api = 'https://api.printful.com/countries'
    country_code = requests.get(country_code_api)
    country_code_data = country_code.json()
    results = country_code_data['result']
    for result in results:
        if country == result['name'].   lower():
            cc = result['code']
    if cc == 'none':
        messagebox.showerror('Error', 'Country not found {}'.format(country))

    custom_link = 'https://newsapi.org/v2/top-headlines?country=' + \
        cc.lower() + '&apiKey=3ed8c02dfc00453fa5ec3d4960e8dfeb'
    response = requests.get(custom_link)
    api_data = response.json()
    my_articles = api_data['articles']
    my_titles = ''
    c = 1
    for article in my_articles:
        my_titles = my_titles + str(c) + '.' + article['title'] + '\n'
        v = int(c) + 1
        c = v
    title.config(text=my_titles)


app = Tk()
app.title("Quick News app.")
app.geometry('1700x500')

country_text = StringVar()
country_text = Entry(app, textvariable=country_text)
country_text.pack()

search_button = Button(app, text='Get News', width=12, command=fetchNews)
search_button.pack()

title = Label(app, text='', font=('bold', 11))
title.pack()

app.mainloop()  