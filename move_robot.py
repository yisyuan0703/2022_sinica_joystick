import socket

HOST = "169.254.144.126" # the first three numbers should be the same as the TM Robot's IP address
# HOST = "127.0.0.1"

PORT = 5890 # port is fixed in TM Robot
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect():
    s.connect((HOST,PORT))

def disconnect():
    s.close()

def byte_xor(byte_a, byte_b):
    return bytes([a ^ b for a, b in zip(byte_a, byte_b)])

def cmd_ptp(n1,n2,n3,n4,n5,n6,index):
    joint = [n1,n2,n3,n4,n5,n6] # deg
    joint_str = ['','','','','','']
    speed = 100 # speed (%)
    accelerate = 20 # acceleration (ms)
    path_mix_rate = 100 # percentage of mixed path
    precise_cancel = 'true' # whether cancel the precise control

    for i in range(len(joint)):
        joint_str[i] = str(joint[i])

    data = str(index)+",PTP(”JPP”,"+','.join(joint_str)+","+str(speed)+","+\
        str(accelerate)+","+str(path_mix_rate)+","+str(precise_cancel)+"),"
    s_type = "float[] "\

    if index == 1:
        data = ",\r\n"+s_type+'targetP1= {'+','.join(joint_str)+'}\r\nPTP("JPP",targetP1'+","+str(speed)+","+\
        str(accelerate)+","+str(path_mix_rate)+","+str(precise_cancel)+"),"
    else:
        data = ',\r\ntargetP1= {'+','.join(joint_str)+'}\r\nPTP("JPP",targetP1'+","+str(speed)+","+\
        str(accelerate)+","+str(path_mix_rate)+","+str(precise_cancel)+")\r\nQueueTag(1),"

    length = len(data)

    checksum_str = 'TMSCT,'+str(length)+','+str(index%10)+data

    byte_a = bytes(checksum_str[0], "utf-8")
    for i in range(len(checksum_str)-1):
        byte_b = bytes(checksum_str[i+1], "utf-8")
        byte_a = byte_xor(byte_a,byte_b)

    checksum = byte_a.hex().upper()

    cmd_str = '$'+checksum_str+'*'+checksum+'\r\n'

    return cmd_str
