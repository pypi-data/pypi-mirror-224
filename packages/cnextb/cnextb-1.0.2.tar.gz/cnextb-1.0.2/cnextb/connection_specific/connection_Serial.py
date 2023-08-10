import datetime
import serial


def serial_read_until(port, char, timeout):
    return_str = b""
    start_time = datetime.datetime.now()
    done = False

    # Loop until done
    while done is False:
        # Loop through waiting chars
        while port.inWaiting() > 0:
            # Read 1 char
            new_char = port.read(1)
            # If this is the exit char
            if new_char == char:
                # Return the current string
                return return_str
            # Else append to the current string
            else:
                return_str += new_char
                # Reset start time for latest char
                start_time = datetime.datetime.now()

        # If no further chars to read and timeout has passed, exit with what we currently have
        now_time = datetime.datetime.now()
        if (now_time - start_time).seconds > timeout:
            return return_str

    return return_str


class SerialConn:
    def __init__(self, conn_target):
        self.conn_target = conn_target

        self.Connection = serial.Serial(port=self.conn_target, baudrate=115200, parity=serial.PARITY_NONE,
                                        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

    def close(self):
        self.Connection.close()
        return True
    
    def sendCommand(self, command):
        command = (command + "\r\n").encode()
        self.Connection.write(command)
        result = serial_read_until(self.Connection, b">", 3).strip()
        result = result.decode()
        result = result.strip('> \t\n\r')
        return result.strip()
