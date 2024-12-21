#!/bin/bash
docker compose down -v --rmi all; docker compose up --build -d --force-recreate