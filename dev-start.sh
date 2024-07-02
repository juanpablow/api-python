#!/bin/sh

docker compose -f infra/compose.yaml start

sleep 10

fastapi dev app/main.py