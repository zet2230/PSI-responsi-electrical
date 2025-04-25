import smbus2
import time

# Alamat I2C BH1750 (default = 0x23)
BH1750_ADDR = 0x5c
# Mode sekali baca, resolusi tinggi
BH1750_ONE_TIME_HIGH_RES_MODE = 0x20

# Inisialisasi I2C bus (I2C-1 untuk Raspberry Pi)
bus = smbus2.SMBus(1)

def read_light():
    # Kirim perintah baca satu kali
    bus.write_byte(BH1750_ADDR, BH1750_ONE_TIME_HIGH_RES_MODE)
    time.sleep(0.18)  # tunggu konversi data (180ms)

    # Baca 2 byte data
    data = bus.read_i2c_block_data(BH1750_ADDR, 0x00, 2)
    raw = (data[0] << 8) | data[1]

    # Konversi ke lux
    lux = raw / 1.2
    return lux

# Loop baca terus-menerus
if __name__ == '__main__':
    while True:
       cahaya = read_light()
       print("Cahaya: %.2f lux" % cahaya)
       time.sleep(1)
