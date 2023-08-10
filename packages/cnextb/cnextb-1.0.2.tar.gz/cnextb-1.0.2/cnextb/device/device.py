import time
import os
import logging
from cnextb.connection import PYConnection


class CnextbDevice:

    def __init__(self, con_string, timeout="5"):

        self.con_string = con_string
        if "serial" not in con_string.lower():
            self.con_string = con_string.lower()

        try:
            self.timeout = int(timeout)
        except:
            raise Exception("Invalid value for timeout, must be a numeric value")

        if checkModuleFormat(self.con_string) is False:
            raise Exception("Module format is invalid!")

        # replacing colons
        numb_colons = self.con_string.count(":")
        if numb_colons == 2:
            self.con_string = self.con_string.replace('::', ':')
        # Create the connection object
        self.connectionObj = PYConnection(self.con_string)
        self.ConCommsType = self.connectionObj.ConnTypeStr
        # Exposes the connection type and module for later use.
        self.connectionName = self.connectionObj.ConnTarget
        self.connectionTypeName = self.connectionObj.ConnTypeStr
        time.sleep(0.1)
        #item = self.connectionObj.connection.sendCommand("*tst?")
        #if "OK" in item:
        #    pass
        #elif "FAIL" in item:
        #    pass
        #elif item is not None:
        #    pass
        #else:
        #    raise Exception("No module responded to *tst? command!")
        #time.sleep(0.1)

        logging.debug(os.path.basename(__file__) + " con_string : " + str(self.con_string))

    def sendCommand(self, command_string):
        response = self.connectionObj.connection.sendCommand(command_string)
        # send response to log
        logging.debug(os.path.basename(__file__) + ": received: " + response)
        return response

    def executeAndCheckCommand(self, command):
        result = self.sendCommand(command)
        #if result == "OK":
        if 'OK' in result:
            return True
        else:
            return False

    def openConnection(self):
        logging.debug("Attempting to open connection")
        del self.connectionObj
        self.connectionObj = PYConnection(self.con_string)
        return self.connectionObj

    def closeConnection(self):
        logging.debug("Attempting to close connection")
        self.connectionObj.connection.close()

    def resetDevice(self, timeout=10):
        logging.debug(os.path.basename(__file__) + ": sending command: *rst")
        retval = self.con_string
        self.connectionObj.connection.sendCommand("*rst", expectedResponse=False)
        self.connectionObj.connection.close()
        logging.debug(os.path.basename(__file__) + ": connecting back to " + retval)

        temp = None
        start_time = time.time()
        time.sleep(0.6)  # most devices are visable again after 0.6 seconds.
        while temp is None:
            try:
                temp = CnextbDevice(retval)
            except:
                time.sleep(0.2)  # wait before trying again if not timed out.
                if (time.time() - start_time) > timeout:
                    logging.critical(os.path.basename(__file__) + ": connection failed to " + retval)
                    return False

        self.connectionObj = temp.connectionObj
        time.sleep(1)
        return True


def checkModuleFormat(con_string):
    con_type = ["SERIAL"]

    con_type_specified = con_string[:con_string.find(':')]

    correct_con_type = False
    for value in con_type:
        if value.lower() == con_type_specified.lower():
            correct_con_type = True

    if not correct_con_type:
        logging.warning("Invalid connection type specified in Module string, use SERIAL")
        return False

    numb_colons = con_string.count(":")
    if numb_colons > 2 or numb_colons <= 0:
        logging.warning("Invalid number of colons in module string")
        return False

    return True
