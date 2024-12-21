#!/bin/bash

while true; do
    sleep 300 
    supervisorctl restart myapp
done

