docker stop userservice
docker rm userservice
docker build -t userservice .
docker run -d \
 -it \
 --restart on-failure \
 --name userservice \
 --net=host \
 -p 5000:5000 \
 userservice