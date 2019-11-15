#!/bin/sh

# psycopg2 fails to install on my machine without manually specifying LDFLAGS for openssl
# using fish shell, for me that's `set -gx LDFLAGS "-L/usr/local/opt/openssl/lib"`
pipenv install --dev

echo "FLASK_APP=hex.application:create_application
FLASK_ENV=development
ENV=dev
DATABASE_URI=postgresql://localhost/hex_dev" >> .env

echo "ENV=test
DATABASE_URI=postgresql://localhost/hex_test" >> .env.test

echo "Run the database migrations!"
echo "hex db create && hex db migrate"
echo "hex db create test && hex db migrate test"