#  Kubernetes Project: Multi-tier Microservices Architecture

This project was developed for the **Virtualization & Cloud Computing** course at **ESIEE Paris**. It features a full containerized stack managed by **Kubernetes (Minikube)**, including inter-service communication, database persistence, and external routing via an Ingress Gateway.

##  Architecture Overview

The application follows a microservices pattern with three main components:
* **Frontend Service**: A Python (Flask) web application providing a modern, styled user interface.
* **Backend Service**: A Python (Flask) API handling logic and database connectivity.
* **Database**: A **PostgreSQL 15** instance for persistent storage.

Communication is orchestrated using **Kubernetes DNS** (the Frontend calls `http://backend-service`) and external traffic is routed through an **Nginx Ingress Controller**.

##  Prerequisites

Ensure you have the following tools installed and running:
* **Docker Desktop** (Engine running)
* **Minikube**
* **kubectl**

Enable the Ingress addon in Minikube:
```bash
minikube addons enable ingress
```
### Network Bridge
Because we are using an Ingress on Windows, you must keep a terminal open with the following command to bridge the network:
```bash
minikube tunnel
```
### Local DNS Setup
Add this entry to your C:\Windows\System32\drivers\etc\hosts file to map the custom domain to your local machine
```bash
127.0.0.1 myservice.info
```
### Deploy to Kubernetes
```bash
kubectl apply -f manifests/
```
Check the status of your deployment
```bash
kubectl get pods
kubectl get ingress
```

Once all pods are in the Running state, visit the application at:
http://myservice.info 


## Docker Hub Repositoy
Custom images are publicly available on Docker Hub:

Frontend: axelblois/my-frontend:2.0

Backend: axelblois/my-backend:2.0
