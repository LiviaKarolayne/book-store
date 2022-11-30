USE Store;

CREATE TABLE books (
    id integer not null auto_increment,
    title varchar(100),
    author varchar(100),
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO books (title, author) VALUES ("Clean Code: A Handbook of Agile Software Craftsmanship", "Robert C. Martin");
INSERT INTO books (title, author) VALUES ("Clean Architecture: A Craftsman's Guide to Software Structure and Design", "Robert C. Martin");
INSERT INTO books (title, author) VALUES ("Design Patterns: Elements Of Reusable Object-oriented Software - Importado - Ingles", "Erich Gamma");
INSERT INTO books (title, author) VALUES ("Computer Networking: A Top-Down Approach", "James Kurose");