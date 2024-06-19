# Book Store

![Under Construction](https://img.shields.io/badge/🚧%20under%20construction-grey?style=for-the-badge)

The scope of the project is a bookstore. It was created to train the integration between a web application, database connection and service delivery in VNF.

<img src="./docs/img/get-ip-node.gif"/>
<img src="./docs/img/access-book-store.gif"/>

## Architecture
<img src="./docs/img/architecture.png"/>

## Technologies used
### Web application
* Flask
* MySQL Connector Lib
* HTML
* CSS

### Database
* MySQL

### Infra
* Docker
* Kubernetes

## Prerequisites
* Install docker
* Install kubernetes
* Install minikube

## Installation
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

⚠️ Security vulnerabilities have not yet been addressed
