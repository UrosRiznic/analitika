import pandas as pd
import matplotlib.pyplot as plt

def top_10_most_expensive_movies():
    df = pd.read_csv('test2.csv')

    # Sortiranje po koloni "budget" (budžet) u opadajućem redosledu i izdvajanje prvih 10
    top_10 = df.sort_values(by='Budget', ascending=False).head(10)

    # Prikazivanje grafikona
    plt.barh(top_10['title'], top_10['Budget'])
    plt.xlabel('Budžet')
    plt.ylabel('Naslov filma')
    plt.title('10 najskupljih filmova')
    plt.show()

def most_comon_actors_in_disney_movies():
    df = pd.read_csv('test2.csv')
    actors = []

    # Iteriranje kroz svaki redak u koloni "Starring" i dodavanje imena glumaca u listu
    for row in df['Starring']:
        if isinstance(row, str):  # preskačemo prazna polja
            actors.extend(row.split(','))  # dodajemo svakog glumca u listu

    # Kreiranje pandas Series objekta koji broji pojavljivanja svakog glumca
    actor_counts = pd.Series(actors).value_counts()

    # Kreiranje bar plot-a od prvih 5 najčešće pojavljujućih glumaca
    actor_counts.head(5).plot(kind='bar')
    plt.title('Top 5 glumaca u koloni "Starring"')
    plt.xlabel('Glumac')
    plt.ylabel('Broj pojavljivanja')
    plt.show()

most_comon_actors_in_disney_movies()
top_10_most_expensive_movies()