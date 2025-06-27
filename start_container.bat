#!/bin/bash

HOST="/data/Docker/CiscoBanfi"  # write here the path of mounted volume

echo "docker run -d \
             --restart always \
             -v $HOST:/app/host \
             --name scobanfi_bot ciscobanfi_image"             
             
docker run -d \
             --restart always \
             -v $HOST:/app/host \
             --name scobanfi_bot ciscobanfi_image

