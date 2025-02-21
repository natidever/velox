# #!/bin/
# # cd /app
# cd /app/backend

# python manage.py migrate
# gunicorn backend.wsgi:application --bind 0.0.0.0:${PORT:-8000} &

# # python velox_telegram_bot/main.py &
# cd /app
# python velox_telegram_bot/main.py &


# wait

#!/bin/bash
cd /app

# Run Django commands
cd backend
python manage.py migrate
gunicorn backend.wsgi:application --bind 0.0.0.0:${PORT:-8000} &

# Run bot
cd ..
python velox_telegram_bot/main.py &

wait