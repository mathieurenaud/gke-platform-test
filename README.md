# Technologies Used

Docker
Python
Google Container Engine

# Prep Steps

First, install google cloud sdk (https://cloud.google.com/sdk/downloads) and register for a google account.
Then install kubectl with `gcloud components install kubectl`
In the google cloud platform console:
1. Create project, not project id
2. For project, enable container engine api and container registry api
3. Once APIs are enabled, ready to start container cluster, build container and run it

# In the shell

## Store project id for reuse

```bash
export PROJECT_ID="app-direct-test-mat-renaud"
```

## Configure gcloud

```bash
gcloud config set project $PROJECT_ID
gcloud config set compute/zone us-east1-b
gcloud auth login
```

## Start a small GKE container cluster

```bash
gcloud container clusters create platform-test-cluster --num-nodes=3
```

## Build my container and push it

```bash
docker build -t gcr.io/${PROJECT_ID}/platform-test:v1 
gcloud docker -- push gcr.io/${PROJECT_ID}/platform-test:v1
```

## Run my container on my cluster

```bash
kubectl run platform-test --replicas=3 --image=gcr.io/${PROJECT_ID}/platform-test:v1 --port 8000
kubectl expose deployment platform-test --type=LoadBalancer --port 8000
```

## Check it out!
_For the sake of demo, last deployed IP is 35.193.48.65_
```bash
# It may take a a minute after the previous step for the service to be available for requests
export IP=$(kubectl get service platform-test -o jsonpath={.status.loadBalancer.ingress[*].ip})
curl http://$IP:8000/
```
