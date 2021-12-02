#!/bin/sh
export CLOISIM_RESOURCES_PATH=$PWD/sample_resources/
xhost +
docker-compose build
docker-compose up
xhost -

