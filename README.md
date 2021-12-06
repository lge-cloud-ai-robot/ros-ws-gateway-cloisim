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

## TEST API
Open "http://localhost:9000/docs" with Web Browser

## TEST with ros-mon
* Install and Run ros-mon (https://github.com/lge-cloud-ai-robot/ros-mon)

* Open "ros-mon" (http://localhost:3000) with Web Browser

* Add Gateway Config for ros-ws-gateway-jackal
  + Gateway URI : the address of the host that you executed 'docker-compose up' and exposed port of the gateway (ex: 192.168.0.4:9000)
  + Control topic:  /cloi1/cmd_vel
  + Image topic: /cloi1/camera/color/image_raw/compressed

* Select cloisim Config in ros-mon web page
* Click Start button in ros-mon web page
