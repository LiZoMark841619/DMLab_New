#!/bin/sh

# Ensure the PORT environment variable is set
if [ -z "$PORT" ]; then
  echo "Error: PORT environment variable is not set."
  exit 1
fi

# Run the application
exec gunicorn app:app --bind 0.0.0.0:$PORT