# lib-project

Minha primeira API pra adicionar e consultar dados em um banco de dados.
utilizando Flask, sqlite3 e pandas.

1. Por meio de um script usando [pandas](https://github.com/rodriguesrafaelm/lib-project/blob/main/data_collector.py), formatei adicionei os dados encontrados no [dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset) ao SQL.
2. Criei um [arquivo](https://github.com/rodriguesrafaelm/lib-project/blob/main/controladores.py) para criar o conector e armazenar as funções utilizadas em cada metodo(get, post e delete)  
3. Criei as rotas utilizando o [Flask](https://github.com/rodriguesrafaelm/lib-project/blob/main/main.py)
<br>

# Rotas:<br>

##### [GET] URL/livros -> Retorna JSON com todos os livros do banco de dados. <br>
##### [POST] URL/livros -> Adiciona um livro. O ID é AUTOINCREMENTAL no banco de dados. Formato: {"nome":"Nome do livro", 'autor':"Nome do autor"}<br>
##### [DELETE] URL/livros -> Remove um livro. Formato: {"id":"ID do livro"}<br>
##### [GET] URL/livros/id -> Retorna um livro com o ID correspondente ao valor de <id>. Caso não exista, retorna mensagem 'Livro não encontrado'.<br>

 <br><br><br><br>  
###### O arquivo CSV utilizado pra criar o banco de dados foi baixado no kaggle, removi do github pra não ficar redundante. 
###### Link do CSV https://www.kaggle.com/datasets/saurabhbagchi/books-dataset
###### Futuramente irei implementar um metodo UPDATE.
