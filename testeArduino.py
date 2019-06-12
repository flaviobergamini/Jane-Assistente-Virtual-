import serial

comando = serial.Serial('/dev/ttyACM0',9600)

while True:
    print comando.readline()
