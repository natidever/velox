#!/bin/bash
gunicorn backend.backend.wsgi:application --bind 0.0.0.0:$PORT &

python velox_telegram_bot/main.py &

wait

