# book_store
Uma aplicação web para loja de livros utilizando banco de dados, flask e kubernets.

sudo docker build -t livia/mysql:1.0 .

sudo docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=RootPassword -e MYSQL_DATABASE=Store -e MYSQL_USER=MyUser -e MYSQL_PASSWORD=MainPassword livia/mysql:1.0