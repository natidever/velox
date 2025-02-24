#!/bin/bash
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

# Navigate to the app directory
cd /app

# Run Django migrations
cd backend
python manage.py makemigrations velox
python manage.py migrate

# Start the development server and bot reloader
cd ..
python dev_server.py