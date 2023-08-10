class PYConnection:
     
    def __init__(self, con_string): 
        
        # Finds the separator. 
        pos = con_string.find(':')
        if pos == -1:
            raise ValueError('Please check your module name!')
        # Get the connection type and target. 
        self.ConnTypeStr = con_string[0:pos].upper()

        self.ConnTarget = con_string[(pos+1):]
        if "SERIAL" not in self.ConnTypeStr:
            self.ConnTarget = con_string[(pos + 1):].upper()
         
        if self.ConnTypeStr.lower() == 'serial':
            from cnextb.connection_specific.connection_Serial import SerialConn
            self.connection = SerialConn(self.ConnTarget)
         
        else: 
            raise ValueError("Invalid connection type in module string!")
