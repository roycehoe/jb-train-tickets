# Introduction

A technical test by GovTech

# Getting started

## Backend

- Install [poetry](https://python-poetry.org/docs/1.3#installing-with-the-official-installer) on your machine
- Go into the backend directory
- Install all project dependencies with `poetry install`
- Activate the project virtual environment by running the command `poetry shell`
- Run the command `uvicorn main:app --reload` to start the backend server on your machine. The server should be running on localhost:8000
- Optional: To view the Swagger UI of this application, create a .env file in the backend directory and add the following line: `IS_DEV="True"`. You may visit the Swagger UI page at localhost:8000/docs

## Frontend

- Install `pnpm` with `npm` on your machine
- Go into the frontend directory
- Install all project dependencies with `pnpm install`
- Create a .env file in the frontend directory and add the following line: `VITE_BASE_URL=http://localhost:8000` to specify the location of the backend service
- Run the command `pnpm run dev` to start a development server on your local machine
- Visit `http://localhost:5173` to view the application

## Containerization

Alternatively, you may containerize the entire application:

- Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/)
- Go to the root of this directory and run the command `docker-compose build && docker-compose up` to build and starts all the project's containers
- View the application on `localhost:80`

# Objectives attempted

## Frontend

- Implemented a user view for users to view all items in the store
- Implemented an admin view for admins to seamlessly create, update, and delete any items of their choosing
- Created a mock navbar to allow Uncle Jack to easily toggle between the admin and user view
- Standardized item card format and page layout between admin and user view, improving usability by giving admins a consistent view to quickly compare and edit item data when toggling between both views
- Integrated creation of new items with deletion and editing of old items, for a more seamless user admin experience
- Utilised HTML form `required` attribute to improve the admin user experience by preventing input errors

## Backend

- Utilised SQLAlchemy ORM to improve security of application, preventing possible SQL injection attacks by parameterising database queries
- Utilised Pydantic to validate request schemas, and automate the raising of request schema related errors
- Utilised loguru to log all CRUD related operations

## Deployment

- Containerised both backend and frontend services with Docker; Utilised docker-compose to enable communication between said services over the same network
- Configured a reverse proxy with Nginx to enable running of both frontend and backend services on the same machine, simplifying deployment, and reducing infrastructure complexity and cost
- Used a cloud technology provider (DigitalOcean) to provision a server to deploy my application
