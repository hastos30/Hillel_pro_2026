
#!/bin/sh
set -eu

echo "Starting BookStore..."

echo "Checking Django configuration..."
python manage.py check

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Django server..."
exec "$@"
