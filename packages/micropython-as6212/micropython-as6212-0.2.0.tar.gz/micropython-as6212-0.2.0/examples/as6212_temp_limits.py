# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_as6212 import as6212

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
as6 = as6212.AS6212(i2c)

as6.temperature_high_limit = 35
as6.temperature_low_limit = 30
print(f"Temperature High Limit: {as6.temperature_high_limit:.2f}°C")
print(f"Temperature Low Limit: {as6.temperature_low_limit:.2f}°C")
print(f"Interrupt_mode: {as6.interrupt_mode}")

while True:
    print(f"Temperature: {as6.temperature:.2f}°C")
    print(f"Alert Triggered: {as6.alert}")
    print()
    time.sleep(1)
