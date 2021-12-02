#!/usr/bin/env python
import time
import random

import roslibpy



client = roslibpy.Ros(host='localhost',port=9000)
client.run()
time.sleep(1)

publisher= roslibpy.Topic(client, '/cloi1/cmd_vel', 'geometry_msgs/msg/Twist')
key = input('Press any key')

while client.is_connected:
    x = 0.0
    a = 0.0
    key = input('Input Key :[e] is stop, [q] is quit , wasd')
    if key=='w':
        x=0.55
    elif key=='a':
        a=0.55
    elif key=='s':
        x=-0.55
    elif key=='d':
        a=-0.55
    elif key=='e':
        x=0.0
        a=0.0
    elif key=='q':
        publisher.publish(roslibpy.Message(
        {
            'linear': { 'x': 0.0, 'y': 0.0, 'z': 0.0}, 
            'angular': { 'x': 0.0, 'y': 0.0, 'z': 0.0}
        }))
        time.sleep(1)
        break
    publisher.publish(roslibpy.Message(
                {
                'linear': { 'x': x, 'y': 0.0, 'z': 0.0}, 
                'angular': { 'x': 0.0, 'y': 0.0, 'z': a}
                }))
    print("Send!!")
publisher.unadvertise()
client.terminate()
    
