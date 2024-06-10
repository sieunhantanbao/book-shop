# Deploy the app to K8S
## Prerequisites Installation Tools
- [Docker Engine](https://docs.docker.com/engine/install/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download#Service)
- [Taskfile](https://taskfile.dev/installation/)
- [Helm](https://helm.sh/docs/intro/install/)

## Deploy database (Postgresql, Redis)
```bash
   task deploy_db
```
## Run Db Migration
```bash
   task run_migration
```

## Run volume mount
```bash
   task mount_api_volume
```

## Deploy Backend API (FastAPI)
```bash
   task deploy_api
```

## Deploy Frontend Client (React)
```bash
   task deploy_frontend
```