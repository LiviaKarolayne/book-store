#!/bin/bash

img=$(docker images | grep db-store)

if [ -z "$img" ]; then
    echo "*** Starting database"
    docker build -t db-store db/
    minikube image load db-store
    kubectl apply -f kubernetes/db-pod.yaml
    kubectl apply -f kubernetes/db-svc.yaml
fi

img=$(docker images | grep app-store)

if [ -z "$img" ]; then
    echo "*** Starting Book Store App"
    docker build -t app-store .
    minikube image load app-store
    kubectl apply -f kubernetes/app-pod.yaml
    kubectl apply -f kubernetes/app-svc.yaml
fi

echo "Done!"