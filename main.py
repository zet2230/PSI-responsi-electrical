from time import sleep

from sensor.MPU_New import read_gyro
from sensor.BH import read_light
from sensor.load_cell import baca_berat

from aktuator.servo import set_angle
from aktuator.stepper import one_step, forward, backward

#sleep(1)
while True:
    data = []
    # kode buat baca sensor dan running motor, perlu pakai async io strukturnya
    sleep(1)
