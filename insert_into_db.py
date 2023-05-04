import psycopg2
import pandas as pd

# Uspostavite vezu s bazom podataka
conn = psycopg2.connect(host="localhost",database="db_project",user="postgres",password="uros")

# Kreirajte novu tablicu
cur = conn.cursor()
cur.execute("""
       CREATE TABLE IF NOT EXISTS movies (
        ID SERIAL PRIMARY KEY,
        title VARCHAR(10000),
        Directed_by VARCHAR(10000),
        Story_by VARCHAR(10000),
        Based_on VARCHAR(10000),
        Produced_by VARCHAR(10000),
        Starring VARCHAR(10000),
        Music_by VARCHAR(10000),
        Production_company VARCHAR(10000),
        Distributed_by VARCHAR(10000),
        Release_dates VARCHAR(10000),
        Country VARCHAR(10000),
        Languages VARCHAR(10000),
        Budget VARCHAR(10000),
        Box_office VARCHAR(10000),
        Running_time VARCHAR(10000),
        Budget_ft VARCHAR(10000),
        Box_office_ft VARCHAR(10000),
        Release_date_dt VARCHAR(10000),
        imdb VARCHAR(10000),
        metascore VARCHAR(10000),
        rotten_tomatoes VARCHAR(10000)
    );
""")

# Učitajte podatke iz CSV datoteke
df = pd.read_csv('disney_movie_data_final.csv')

# Ubacite podatke u novu tablicu
for index, row in df.iterrows():
    cur.execute("""
        INSERT INTO movies (
		ID,
        title,
        Directed_by,
        Story_by,
        Based_on,
        Produced_by,
        Starring,
        Music_by,
        Production_company,
        Distributed_by,
        Release_dates,
        Country,
        Languages,
        Budget,
        Box_office,
        Running_time,
        Budget_ft,
        Box_office_ft,
        Release_date_dt,
        imdb,
        metascore,
        rotten_tomatoes
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """, (row['ID']
        , row['title']
        , row['Directed_by']
        , row['Story_by']
        , row['Based_on']
        , row['Produced_by']
        , row['Starring']
        , row['Music_by']
        , row['Production_company']
        , row['Distributed_by']
        , row['Release_dates']
        , row['Country']
        , row['Language']
        , row['Budget']
        , row['Box_office']
        , row['Running_time']
        , row['Budget_ft']
        , row['Box_office_ft']
        , row['Release_date_dt']
        , row['imdb']
        , row['metascore']
        , row['rotten_tomatoes']
        ))

# Spremite promjene i zatvorite vezu s bazom podataka
conn.commit()
cur.close()
conn.close()
