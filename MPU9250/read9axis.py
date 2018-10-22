# coding: utf-8
## @package faboMPU9250
#  This is a library for the FaBo 9AXIS I2C Brick.


import MPU9250
import time
import sys
import csv

mpu9250 = MPU9250.MPU9250()


try:
    with open('data1.csv', 'w') as f:
        datasave = csv.writer(f)
    
        while True:
            accel = mpu9250.readAccel()
            print(" ax = " , ( accel['x'] ))
            print(" ay = " , ( accel['y'] ))
            print(" az = " , ( accel['z'] ))

            gyro = mpu9250.readGyro()
            print(" gx = " , ( gyro['x'] ))
            print(" gy = " , ( gyro['y'] ))
            print(" gz = " , ( gyro['z'] ))

            mag = mpu9250.readMagnet()
            print(" mx = " , ( mag['x'] ))
            print(" my = " , ( mag['y'] ))
            print(" mz = " , ( mag['z'] ))

            temper = mpu9250.readTemperature()
            print("temp", (temper['temp']))
            print()

            datasave.writerow([accel['x'], accel['y'], accel['z']])

        time.sleep(0.05)

except KeyboardInterrupt:
    sys.exit()
