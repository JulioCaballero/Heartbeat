import serial

arduino = serial.Serial('/dev/ttyUSB0', baudrate=115200)

print("Starting")
msj=''
while True:
    #comando = input("Introduzca s para medir tus pulsos: ")
    #arduino.write(comando.encode())
    # if comando == 's':
        while arduino.inWaiting()>0:
            msj += arduino.readline().decode('utf-8')
            print(msj)
            msj=''
    
arduino.close()