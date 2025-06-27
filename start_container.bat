#!/bin/bash

HOST="/data/host"  # write here the path of mounted volume

echo "docker run -d \
             --restart always \
             -v $HOST:/data/host \
             --name scobanfi_bot ciscobanfi_image"             
             
docker run -d \
             --restart always \
             -v $HOST:/data/host \
             --name scobanfi_bot ciscobanfi_image

