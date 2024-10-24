from lib.imu import MPU6050
from time import sleep
from machine import Pin, I2C


i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=200000)   #initiate sda and scl pin for MPU6050
imu = MPU6050(i2c)  #initiate MPU6050 class


while True:
    ax = round(imu.accel.x, 2)  #extracting information from MPU6050 class methods
    ay = round(imu.accel.y, 2)
    az = round(imu.accel.z, 2)
    gx = round(imu.gyro.x)
    gy = round(imu.gyro.y)
    gz = round(imu.gyro.z)
    tem = round(imu.temperature, 2)
    print(f'gx: {gx}\tgy: {gy}\tgz: {gz}\ttem: {tem}')
    sleep(0.2)
