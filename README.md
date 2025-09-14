# Docker-Fullstack-App
Creating a fullstack application with docker container and traefik. In the applikation there are containers created for frontend, backend-api a and postgres databas.


# Project-Mapp Structure:
cd Docker-Fullstack-App

mkdir traefik
cd traefik

mkdir backend-api
touch backend-api/app.py backend-api/Dockerfile backend-api/requirements.txt

mkdir db-postgres
touch db-postgres/Dockerfile db-postgres/requirements.txt

mkdir frontend
touch frontend/index.html frontend/Dockerfile

touch .env
touch docker-compose.yaml



