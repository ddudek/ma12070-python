import smbus
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='MA12070 configuration')
parser.add_argument('--pmp', type=int, default=1, help='PMP value (default: 1)')
args = parser.parse_args()

# I2C channel 1 is connected to the GPIO pins
channel = 1

#  MA12070 defaults to address 0x20
address = 0x20

# Register addresses
# 0x1D = PMP Register
reg_write_dac = 0x1D

value_pmp = args.pmp

def status(bus):
    for offset in [ 0x1d, 0x40, 0x35, 0x36, 0x7e, 0x60, 0x61, 0x62, 0x64, 0x65, 0x66, 0x6d, 0x75, 0x7c ]:
        b = bus.read_byte_data(address, offset)
        print('offset {0}: value={1} / {2}'.format(hex(offset), hex(b), bin(b)))

# Initialize I2C (SMBus)
bus = smbus.SMBus(channel)


print('status before writes:')
status(bus)

# Write out I2C command: address, reg_write_dac, msg,
bus.write_byte_data(address, reg_write_dac, value_pmp)

print('status after writes:')
status(bus)

bus.close()
