start-frontend:
	cd frontend && \
	npm install && \
	npm start

start-backend:
	./bootstrap.sh

pip-setup:
	pipenv install

start-docker:
	docker-compose up --detach && \
	sleep 20 
	# wait for container to be ready 

stop-docker:
	docker-compose down

db-init:
	cd database-start && \
	./db-bootstrap.sh