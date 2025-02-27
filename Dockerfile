FROM python:3.11-slim as prod


WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 
    # DJANGO_SETTINGS_MODULE=backend.settings
    

# RUN apt-get update && apt-get install -y --no-install-recommends \
# build-essential \
# && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user matching host UID/GID
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} appuser && \
    useradd -u ${UID} -g ${GID} -ms /bin/bash appuser

COPY . .

RUN pip install -e .



RUN chown -R appuser:appuser /app

USER appuser
EXPOSE 8000

CMD ["bash", "start.sh"]

#DEVELOPMENT IMAGE
FROM python:3.11-slim as dev


WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
    # DJANGO_SETTINGS_MODULE=backend.settings


# RUN apt-get update && apt-get install -y --no-install-recommends \
# build-essential \
# && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user matching host UID/GID
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} appuser && \
    useradd -u ${UID} -g ${GID} -ms /bin/bash appuser

COPY . .

RUN pip install -e .



RUN chown -R appuser:appuser /app

USER appuser
EXPOSE 8000

CMD ["bash", "start_dev.sh"]




