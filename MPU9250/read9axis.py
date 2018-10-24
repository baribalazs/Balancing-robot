# Created to test and evaluate complementary and Kalman Filter
# allways invoke the registry writer first.

import MPU9250
import time
import sys
import csv

mpu9250 = MPU9250.MPU9250()

K = 0.98
K1 = 1-K

time_diff = 0.02

def distance(a, b):
    return math.sqrt((a*a) + (b*b))

def y_rotation(x, y, z):
    radians = math.atan2(x, distance(y, z))
    return -math.degrees(radians)

def x_rotation(x, y, z):
    radians = math.atan2(y, distance(x, z))
    return math.degrees(radians)

accel = mpu9250.readAccel()
gyro = mpu9250.readGyro()
mag = mpu9250.readMagnet()
temper = mpu9250.readTemperature()

aTempX = accel['x']
aTempY = accel['y']
aTempZ = accel['z']

gTempX = gyro['x']
gTempY = gyro['y']
gTempZ = gyro['z']

last_x = x_rotation(aTempX, aTempY, aTempZ)
last_y = y_rotation(aTempX, aTempY, aTempZ)

gyro_offset_x = gTempX
gyro_offset_y = gTempY

gyro_total_x = (last_x) - gyro_offset_x
gyro_total_y = (last_y) - gyro_offset_y
    

try:
    with open('data1.csv', 'w') as f:
        datasave = csv.writer(f)
    
        while True:
            accel = mpu9250.readAccel()
            gyro = mpu9250.readGyro()
            mag = mpu9250.readMagnet()
            temper = mpu9250.readTemperature()
            
            accelX = accel['x']
            accelY = accel['y']
            accelZ = accel['z']

            gyroX = gyro['x']
            gyroY = gyro['y']
            gyroZ = gyro['z']

            gyroX -= gyro_offset_x
            gyroY -= gyro_offset_y

            gyro_x_delta = (gyroX * time_diff)
            gyro_y_delta = (gyroY * time_diff)

            gyro_total_x += gyro_x_delta
            gyro_total_y += gyro_y_delta

            rotation_x = x_rotation(accelX, accelY, accelZ)
            rotation_y = y_rotation(accelX, accelY, accelZ)
    
            #Complementary Filter
            last_x = K * (last_x + gyro_x_delta) + (K1 * rotation_x)
            last_y = K * (last_y + gyro_y_delta) + (K1 * rotation_y)

            #print("temp", (temper['temp']))
            
            datasave.writerow([accelX, accelY, accelZ, gyroX, gyroY, gyroZ last_x, last_y, mag['x'], mag['y'], mag['z']])

        time.sleep(0.02)

except KeyboardInterrupt:
    sys.exit()