import serial
import time

ser1 = serial.Serial(port="COM10",
    baudrate=3000000,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)

def connect():
    if ser1.isOpen():
        ser1.close()
    ser1.open()
    time.sleep(0.5)

    if ser1.isOpen():
        ser1.write('B0D\r'.encode())
        ser1.write('B0W006\r'.encode())
        time.sleep(0.1)
        return True
    else:
        return False

def disconnect():
    if not ser1.isOpen():
        ser1.open()
    ser1.close()
    time.sleep(0.5)

    if not ser1.isOpen():
        return True
    else:
        return False

def init_angle():
    init_pose = []

    ser1.write('R0\r'.encode())
    ser1.write('CFF076\r'.encode())

    time.sleep(0.01)

    ser1.read_until('\r'.encode())

    out = ser1.read_until('\r'.encode())

    angle = out.decode().split(' ')

    for i in range(len(angle)-1):
        init_pose.append(int(angle[i], base=16))

    return init_pose

def read_angle(self, init_pose):

    angle_list = []

    ser1.write('R0\r'.encode())
    ser1.write('CFF078\r'.encode())

    time.sleep(0.01)

    out1 = ser1.read_until('\r'.encode())
    out2 = ser1.read_until('\r'.encode())
    angle = out2.decode().split(' ')

    for i in range(len(angle)-1):
        angle_list.append(round((int(angle[i], base=16)-init_pose[i])*107.28836*10**-6,3))

    scale = 16 # equals to hexadecimal
    num_of_bits = 8
    angle_list.append(str(bin(int(out1, scale))[2:].zfill(num_of_bits)))

    return angle_list