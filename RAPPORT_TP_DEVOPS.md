# RAPPORT — TP DevOps
## Conteneurisation, Orchestration et Pipeline CI/CD
### Application Python : System Metrics Agent

## 1. Objectif
Le TP consiste à conteneuriser une application Python, orchestrer ses services avec Docker Compose, automatiser les tests et la construction avec GitHub Actions, puis publier et déployer l'image via Docker Hub.

## 2. Application
L'application comporte deux processus :
- API FastAPI : réception et consultation des métriques.
- Agent : collecte périodique des métriques système et envoi HTTP.

## 3. Conteneurisation
Deux Dockerfiles sont fournis :
- `Dockerfile.dev` pour le développement avec rechargement à chaud.
- `Dockerfile` pour la production avec build multi-stage, utilisateur non-root et healthcheck.

## 4. Orchestration
`docker-compose.yaml` définit :
- le service `api` ;
- le service `agent` ;
- un réseau Docker dédié ;
- le healthcheck de l'API ;
- la dépendance de l'agent envers l'API.

L'agent communique avec l'API via `http://api:8000/metrics`.

## 5. Tests
La suite de tests est exécutée avec :
```bash
pytest -q
```

## 6. CI/CD
Le workflow GitHub Actions réalise :
1. checkout ;
2. build de l'image ;
3. exécution des tests ;
4. publication sur Docker Hub si les tests réussissent.

Les secrets sont :
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

## 7. Publication et déploiement
L'image est publiée sur Docker Hub avec les tags :
- `latest`
- SHA du commit.

Le déploiement se fait ensuite avec :
```bash
docker compose -f docker-compose.hub.yaml pull
docker compose -f docker-compose.hub.yaml up -d
```

## 8. Vérifications
Commandes principales :
```bash
docker ps
curl http://localhost:8000/health
curl http://localhost:8000/metrics/latest
docker compose logs
```

## 9. Captures à insérer
1. Structure du projet.
2. Build Docker.
3. Tests pytest.
4. Docker Compose.
5. `docker ps`.
6. `/health`.
7. `/metrics/latest`.
8. GitHub Actions.
9. Docker Hub.

## 10. Conclusion
Le projet met en œuvre une chaîne DevOps complète : conteneurisation, orchestration, tests automatisés, intégration continue, publication d'images et déploiement à partir du registre Docker Hub.
