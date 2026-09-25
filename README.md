# System Metrics Agent — DevOps

## Présentation
Projet de conteneurisation, orchestration et CI/CD d'une application Python de collecte de métriques système.

## Architecture
- `api` : API FastAPI (`/health`, `/metrics`, `/metrics/latest`)
- `agent` : collecte CPU/RAM/charge et envoi HTTP
- Docker Compose : réseau et dépendance entre services
- GitHub Actions : build, tests et publication Docker Hub

## Prérequis
- Git
- Docker / Docker Compose
- Compte GitHub
- Compte Docker Hub

## Installation locale
```bash
pip install -r requirements.txt
pytest -q
```

## Développement
```bash
docker build -f Dockerfile.dev -t system-metrics-agent:dev .
docker run --rm -p 8000:8000 system-metrics-agent:dev
```

Avec Compose :
```bash
docker compose up --build
```

## Production
```bash
docker build -t system-metrics-agent:latest .
docker compose up --build
```

Tester :
```bash
curl http://localhost:8000/health
curl http://localhost:8000/metrics/latest
```

## Docker Hub
Remplacer `TON_USERNAME` par votre identifiant Docker Hub.
```bash
docker build -t TON_USERNAME/system-metrics-agent:latest .
docker push TON_USERNAME/system-metrics-agent:latest
```

Déploiement depuis Docker Hub :
```bash
docker compose -f docker-compose.hub.yaml pull
docker compose -f docker-compose.hub.yaml up -d
```

## CI/CD
Le workflow `.github/workflows/ci-cd.yml` :
1. récupère le dépôt ;
2. construit l'image ;
3. exécute pytest ;
4. publie l'image uniquement après réussite des tests.

Secrets GitHub requis :
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

## Sécurité
Le fichier `.env` ne doit jamais être commité. Les secrets Docker Hub sont stockés dans GitHub Actions.

## Captures à ajouter au rendu
- build Docker ;
- tests pytest ;
- conteneurs actifs ;
- `/health` ;
- `/metrics/latest` ;
- pipeline GitHub Actions vert ;
- image Docker Hub.
