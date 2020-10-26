#!/usr/bin/env bash


pytest unitTests.py -s

printf "\n GET /todos test \n"
curl -v http://localhost:4567/todos

printf "\n POST /todos test \n"
curl \
  --header "Content-type: application/json" \
  --request POST \
  --data '{"title": "Test Title", "description": "Test Description"}' \
  http://localhost:4567/todos
  
printf "\n GET /todos/:id/tasksof \n"
curl --request GET http://localhost:4567/todos/1


curl --location --request GET http://localhost:4567/shutdown


