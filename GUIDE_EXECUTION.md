# GUIDE D'EXECUTION

1. Ouvrir un terminal dans le dossier du projet.
2. Vérifier Docker :
   docker --version
   docker compose version

3. Tester Python :
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pytest -q

4. Construire la production :
   docker build -t system-metrics-agent:latest .

5. Lancer :
   docker compose up --build

6. Tester :
   curl http://localhost:8000/health
   curl http://localhost:8000/metrics/latest

7. Docker Hub :
   docker login
   docker build -t TON_USERNAME/system-metrics-agent:latest .
   docker push TON_USERNAME/system-metrics-agent:latest

8. GitHub :
   créer DOCKERHUB_USERNAME et DOCKERHUB_TOKEN dans Settings > Secrets and variables > Actions.

9. Pousser :
   git add .
   git commit -m "Projet DevOps complet"
   git branch -M main
   git push -u origin main

10. Après publication :
   modifier TON_USERNAME dans docker-compose.hub.yaml, puis :
   docker compose -f docker-compose.hub.yaml pull
   docker compose -f docker-compose.hub.yaml up -d
