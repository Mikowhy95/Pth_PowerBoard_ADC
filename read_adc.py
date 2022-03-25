# Demo made for reading analog values and convert them to output
# Author: Mikowhy95
import time

import ADS1x15 # local copy of Adafruit libs

# TODO: write proper import from https://github.com/adafruit/Adafruit_Python_ADS1x15
# TODO: write proper import from https://github.com/adafruit/Adafruit_Python_GPIO

# Panther (since v1.2) uses PowerBoard (tested v1.0 with fixes) with implemented two ADS1015
# Analog to Digital Converters conected to RPi via I2C.
adcU12 = ADS1x15.ADS1015(address=0x48, busnum=1)
adcU13 = ADS1x15.ADS1015(address=0x49, busnum=1)

# Ports:
# Each ADC has 4 analog inputs connected to specific potentials:
# U12:
#   BAT2 voltage
#   IDIG current
#   BAT1 voltage
#   n / a
# U13:
#   Temperature 1
#   Temperature 2
#   Charging current 2
#   Charging current 1

# Below is a list that indexes each of the values to their
# respective position in the output vector "calculatedResults":
adcU12valuesIDs = [1, 2, 0]
adcU13valuesIDs = [3, 4, 5, 6]

# Names:
# ssed to display values clearly.
names = [ "VBAT1 [mV]",    "VBAT2 [mV]",    "IDIG [mA] ",    "TEMP1     ",
          "TEMP2     ",    "ICH1 [mA] ",    "ICH2 [mA] " ]

# Multiplier:
# value calculated by us,
# resulting from the hardware (voltage divider, current sensor gain, shunt value)
RTOP = 113000
RBOTTOM = 4700
MULT_VBAT = ((RTOP+RBOTTOM)/RBOTTOM)    # = 25,04255319148936
MULT_IDIG = 8
MULT_ICH = 2
MULT_TEMP = 1

multipliers  = [MULT_VBAT, MULT_VBAT, MULT_IDIG, MULT_TEMP,
                MULT_TEMP, MULT_ICH, MULT_ICH]

# Gain:
# change range of voltages that can be measured
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
gainsU12 = [2, 1, 2]
gainsU13 = [1, 1, 1, 1]

# Scale:
# depended on choosen gain, needed for calculation final values.
scalesU12 = [1, 2, 1]
scalesU13 = [2, 2, 2, 2]

while True:
    # Write all needed ADC channel values with specific Gains to a list.
    values = [0]*7
    for i in range(3):
        values[adcU12valuesIDs[i]] = adcU12.read_adc(i, gain=gainsU12[i]) * scalesU12[i]
    for i in range(4):
        values[adcU13valuesIDs[i]] = adcU13.read_adc(i, gain=gainsU13[i]) * scalesU13[i]

    # Calculate all output values and print them.
    calculatedResults = [0]*7
    for i in range(7):
        calculatedResults[i] = values[i]*multipliers[i]
        print(names[i],' ',calculatedResults[i])
    
    print()

    # Pause for one second.
    time.sleep(1)