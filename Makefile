install:
# psycopg2 fails to install on my machine without manually specifying LDFLAGS for openssl
# using fish shell, for me that's `set -gx LDFLAGS "-L/usr/local/opt/openssl/lib"`
	pipenv install --dev
	@echo -e "FLASK_APP=hex.application:create_application\nFLASK_ENV=development\nENV=dev\nFLASK_DEBUG=1\nDATABASE_URI=postgresql://localhost/hex_dev" > .env
	@echo -e "ENV=test\nDATABASE_URI=postgresql://localhost/hex_test" > .env.test


migrate:
# a postgresql instance with a hex_dev and hex_test db is required
# make sure to set the DATABASE_URI in the appropriate .env file(s)
	hex db migrate
	hex db migrate test