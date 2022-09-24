start-frontend:
	cd frontend && \
	npm start

start-backend:
	./bootstrap.sh

pip-setup:
	pipenv install

start-docker:
	docker-compose up

db-init:
	cd database-start && \
	./db-bootstrap.sh