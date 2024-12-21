#!/bin/bash


# Set Execution Privilege
chmod +x ./images/build.sh
# Run build.sh
./images/build.sh

# Docker compose  up
docker compose up --build -d