import pandas as pd
import sqlite3

df = pd.read_csv("db/books.csv", sep=";", error_bad_lines=False, encoding="latin-1")
df = df[['BookTitle', 'BookAuthor']]
try:
    con = sqlite3.connect('biblioteca.db')
    cur = con.cursor()
    sql = "INSERT INTO livros('nome', 'autor') VALUES(?, ?)"
    for index, row in df.iterrows():
        cur.execute(sql, (row.BookTitle, row.BookAuthor))
    print('Sucesso na inserção dos dados')
except Exception as error:
    print(error)
finally:
    con.commit()
    cur.close()
    con.close()