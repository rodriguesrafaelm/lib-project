import sqlite3

def connect_db(): #conector
    con = sqlite3.connect('db/biblioteca.db')
    cur = con.cursor()
    return con, cur

def add_livro(livro, autor):
    try:
        con, cur = connect_db()
        statement = "INSERT INTO livros(nome, autor)"\
                    "Values(?, ?); "
        cur.execute(statement, (livro, autor))
        con.commit()
    except Exception:
        print('Erro ao inserir')
    finally:
        cur.close()
        con.close()

def remover_livro(id):
    try:
        con, cur = connect_db()
        statement = "DELETE FROM livros "\
                    "WHERE id_livro = ? ; "
        cur.execute(statement, (id,))
        con.commit()
    except Exception as erro:
        print(erro)
    finally:
        cur.close()
        con.close()


def listar():
    try:
        con, cur = connect_db()
        statement = 'SELECT * from livros'
        cur.execute(statement)
        query_results = cur.fetchall()
    except Exception as erro:
        print(erro)
    finally:
        cur.close()
        con.close()
        if query_results:
            return query_results


def selecionar_livro(id):
    try:
        con, cur = connect_db()
        statement = 'SELECT * from livros WHERE id_livro = ?'
        cur.execute(statement, (id,))
        query_results = cur.fetchone()
    except Exception as erro:
        print(erro)
    finally:
        cur.close()
        con.close()
        if query_results:
            return query_results