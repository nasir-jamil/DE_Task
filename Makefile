build:
#   Build the image
	docker-compose build

create: build
#   Create the container
	docker-compose create

up: create
#   Run DB Server
	docker compose up database -d
#   Ingest data
	docker compose up solution-python
#   Create the output file
	docker compose up output-python
#   Remove container
#	docker compose down

#   Will remove all images and volumes after user confirmation
#   docker system prune -a --volumes
