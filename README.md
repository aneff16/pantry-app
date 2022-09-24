# pantry-app

## What Is It?
This is a simple app written in JavaScript with React on the frontend and Flask, Python, and SQLAlchemy on the backend.  The purpose is to allow users to login and track grocery items in their pantry.  The backend was created with support for multiple users in mind, but currently the app only runs with a single default user.

## Initial Setup
To run this app, you need to have [Node.js](https://nodejs.org/en/), Python 3 with pipenv installed and Docker.
### Set Up Virtual Environment
Run the command `make pip-setup`.
### Set Up Database in Docker
Run the command `make start-docker db-init`.

## How to Run
Open two seperate shells.

In one, run the command `make start-backend`.  This starts the Flask API that connects to the database.

In the other, run the command `make start-frontend`.  This will start the app on localhost:3000.
