# ROS-WS-GATEWAY Example(ros-ws-gateway with Cloisim)

## Download resource
```
git clone https://github.com/lge-ros2/sample_resources.git
```

## BUILD
```
export CLOISIM_RESOURCES_PATH=$PWD/sample_resources/
docker-compose build
```
## RUN
```
export CLOISIM_RESOURCES_PATH=$PWD/sample_resources/
xhost +
docker-compose up
```

## TEST
Open "http://localhost:9000/docs" with Web Browser
