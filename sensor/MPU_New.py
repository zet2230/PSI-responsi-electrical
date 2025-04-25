import smbus2
from time import sleep

# MPU6050 Registers
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

bus = smbus2.SMBus(1)
Device_Address = 0x68
#sleep(1)
def MPU_Init():
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    bus.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr + 1)
    value = (high << 8) | low
    if value > 32768:
        value = value - 65536
    return value

# Kalibrasi offset saat import pertama kali
MPU_Init()
offset_x = offset_y = offset_z = 0
samples = 100
for i in range(samples):
    offset_x += read_raw_data(GYRO_XOUT_H)
    offset_y += read_raw_data(GYRO_YOUT_H)
    offset_z += read_raw_data(GYRO_ZOUT_H)
    sleep(0.01)
offset_x /= samples
offset_y /= samples
offset_z /= samples

def read_gyro():
    gx = (read_raw_data(GYRO_XOUT_H) - offset_x) / 131.0
    gy = (read_raw_data(GYRO_YOUT_H) - offset_y) / 131.0
    gz = (read_raw_data(GYRO_ZOUT_H) - offset_z) / 131.0
    return gx, gy, gz

if __name__ == '__main__':
    while True:
        cahaya = read_gyro()
        print(cahaya)
        sleep(1)
