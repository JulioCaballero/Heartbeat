import serial

arduino = serial.Serial('/dev/ttyUSB0',9600)

print("Starting")

while True:
    # comando = raw_input()
    print("led encendido")