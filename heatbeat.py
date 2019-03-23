import serial

arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600)

print("Starting")

while True:
    comando = input("Introduzca un comando: ")
    arduino.write(comando.encode())
    if comando == 't':
        print("led encendido")
    elif comando == 'f':
        print("led apagado")
    
    
arduino.close()