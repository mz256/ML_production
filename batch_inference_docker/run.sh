#!/bin/bash

# options:
# 	$ bash run.sh
# 	$ bash run.sh --meta

# Build image from Dockerfile and log STDOUT
tag=docker-model
echo ">> Building image..."
docker build -t $tag -f Dockerfile . &> build.log

if [ "$1" == "--meta" ]
then
	# Print metadata in shell
	echo ">> The stored metadata:"
	docker run $tag cat /home/jovyan/model/metadata.json 
fi

echo ">> Performing inference..."
docker run $tag python3 inference.py &> inference.log

echo ">> Cleaning up stopped containers and images..."
bash cleanup.sh &> cleanup.log
