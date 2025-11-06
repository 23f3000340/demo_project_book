#!/usr/bin/env bash
set -e

# wait-for-db: simple retry loop
echo "Starting entrypoint..."

if [ -n "$POSTGRES_HOST" ]; then
  echo "Waiting for Postgres at $POSTGRES_HOST:$POSTGRES_PORT..."
  RETRIES=30
  until python -c "import sys, psycopg2; psycopg2.connect(\"dbname='${POSTGRES_DB:-postgres}' user='${POSTGRES_USER:-postgres}' host='${POSTGRES_HOST:-db}' password='${POSTGRES_PASSWORD:-}'\")" 2>/dev/null || [ $RETRIES -le 0 ]; do
    echo "Postgres unavailable - sleeping"
    sleep 1
    RETRIES=$((RETRIES-1))
  done
fi

echo "Apply database migrations"
python manage.py migrate --noinput

echo "Collect static files"
python manage.py collectstatic --noinput

exec "$@"
