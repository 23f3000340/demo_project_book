FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# install python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy project
COPY . /app

# create a non-root user (optional)
RUN useradd --create-home appuser || true
RUN chown -R appuser:appuser /app
USER appuser

ENV PATH="/home/appuser/.local/bin:$PATH"

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "bookstore_project.wsgi:application", "-w", "2", "-b", "0.0.0.0:8000"]
