# Book Store

O escopo do projeto é uma loja de livros. Ele foi criado para treinar a integração entre uma aplicação web, conexão a banco de dados e entrega de serviços em VNF.

<img src="./docs/img/get-ip-node.gif"/>
<img src="./docs/img/access-book-store.gif"/>

## Arquitetura
<img src="./docs/img/architecture.png"/>

## Tecnologias utilizadas
### Aplicação web
* Flask
* MySQL Connector Lib
* HTML
* CSS

### Banco de dados
* MySQL

### Serviço
* Docker
* Kubernetes

## Pré-requisitos
* Instalar docker
* Instalar kubernetes
* Instalar minukube

## Instalação
``` console
git clone https://github.com/LiviaKarolayne/book_store.git
cd book_store/
./util/init.sh
```
<img src="./docs/img/installation.gif"/>
<img src="./docs/img/get-pods.gif"/>
<img src="./docs/img/get-svcs.gif"/>

## Access Book Store App
``` console
kubectl get nodes -o wide
curl <IP Address>:30500
```
⚠️ Projeto em construção

⚠️ As vulnerabilidades de segurança ainda não foram tratadas
