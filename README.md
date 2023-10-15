# Codetain Transportation Route app
Codetain Recruitment Task

## Task description
An application that manages transport routes for registered users.

## Requirements
* Docker engine & docker compose / or Docker Desktop
* Python3 installed

## Components
* Webpanel - served by Angular - http://localhost:4200
* API - served by FastAPI - http://localhost:8000
* MailDev - opensource SMTP server - http://localhost:1080
* PostgreSQL db container - http://localhost:8774

## How to run via Docker
* Clone this repository
* Go to /deployment directory
* execute `docker-compose up -d --force-recreate --build`
* Enjoy!

## How to run locally
* Clone this repository
* Go to main directory of downloaded repository
* run command `prisma generate --schema ./app/database/prisma/schema.prisma` - to generate tables
* run command `uvicorn main:app --reload --port "port_of_choice"`
* build database and MailDev with docker
    *  docker-compose build postgres-db
    *  docker-compose build maildev
* Enjoy!

## How to run migrations (how to develop, maintain, fix this code :))
1. Add new entity, or changes in /database/prisma/schema.prisma
2. run command `prisma migrate dev --schema ./app/database/prisma/schema.prisma` - this will apply migrations and purge the database


## Swagger
Swagger is located at: http://localhost:8000/docs

## MailDev
It's an opensource SMTP server with graphical inbox hosted on http://localhost:1080 - it is used for validation purposes of registered users

## TODO:
[ ] - check jinja templates if they're able to manage REST-Template cross-talk, if not, stick to Angular.
[ ] - create all necessary views
[ ] - Add summaries, and all necessities to Swagger docs
[ ] - Integrate JWT logic for Authorization of REST API / validate session by JWT expirationDate
[ ] - Write unit tests
[ ] - Add template and overall handling for deleting user by administrator
[ ] - Clean up code (unused, redundant or obsolete things)