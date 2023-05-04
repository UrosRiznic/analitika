import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders
import os

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

    # Kreiranje PDF-a
    pdf_filename = 'top_10_movies.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.drawString(100, 750, '10 najskupljih filmova')
    for i, row in top_10.iterrows():
        c.drawString(100, 720 - (i * 50), f"{row['title']} - {row['Budget']}$")
    c.save()

    # Slanje PDF-a e-poštom
    from_email = 'urosriznic@yahoo.com'
    to_email = 'urosriznic9@gmail.com'
    subject = 'Top 10 najskupljih filmova'
    body = 'Pozdrav,\n\nU privitku se nalazi PDF sa popisom 10 najskupljih filmova.\n\nLijep pozdrav,\nVaš program'
    send_email(from_email, to_email, subject, body, [pdf_filename])

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
