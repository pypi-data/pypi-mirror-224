import serial
import math
import serial.tools.list_ports as serial_list


def list_serial():
    serial_ports = serial_list.comports()
    serial_modules = dict()

    for i in serial_ports:
        try:
            ser = serial.Serial(i[0], 115200, timeout=0.5)
            ser.write(b'serial?\r\n')
            s = ser.read(size=64)
            serial_module = s.splitlines()[1]
            serial_module = str(serial_module).replace("'", "").replace("b", "")
            serial_modules["SERIAL:" + str(i[0])] = serial_module
            ser.close()
        except:
            pass
    return serial_modules


def scanDevices():
    return list_serial()


def userSelectDevice(scan_dictionary=None, additional_options=None):
    while True:
        # Scan first, if no list is supplied
        if scan_dictionary is None:
            print("Scanning for devices...")
            scan_dictionary = scanDevices()

        if len(scan_dictionary) < 1:
            scan_dictionary["***No Devices Found***"] = "***No Devices Found***"

        if additional_options is None:
            additional_options = ["Rescan", "Quit"]
        tmp_list = []
        for k, v in scan_dictionary.items():
            tmp_list2 = list()
            tmp_list2.append(v)
            tmp_list2.append(k)
            tmp_list.append(tmp_list2)
        add_op = list()
        for option in additional_options:
            add_op.append([option]*2)  # Put option in all columns

        user_str = list_selection(tmp_list, additional_options=add_op, index_req=True, 
                                  table_headers=["Selection", "Description"])
        user_str = user_str[2]  # With the data formatted in this way the ConnTarget will always be in user_str[2]

        # Process the user response
        if user_str.lower() in 'quit':
            return "quit"
        elif user_str.lower() in 'rescan':
            scan_dictionary = None
        else:
            # Return the address string of the selected module
            return user_str


def list_selection(selection_list, table_headers=None, index_req=True, additional_options=None, align="l"):
    # takes in a 2d list and display it with an index column for selection
    # get user input of selection
    # return 2d[selection]
    try:
        selection_list = selection_list.copy()
        additional_options = additional_options.copy()
        table_headers = table_headers.copy()
    except:
        pass

    if additional_options is not None and additional_options.__len__() > 0:
        if isinstance(additional_options, str):
            additional_options = additional_options.split(',')
        selection_list += additional_options

    if isinstance(selection_list, str):
        selection_list = selection_list.split(',')
    elif isinstance(selection_list, dict):
        selection_list = dict_to_list(selection_list)

    dispaly_table(selection_list, index_req=index_req, table_headers=table_headers, align=align)
    print("")
    # Request user selection
    while True:
        user_str = input("Please select an option:\n>")

        # Validate the response
        try:
            user_number = int(user_str)
            if 1 <= user_number <= len(selection_list):
                break
        except:
            print("INVALID SELECTION!")

    # Return the key associated with this entry
    return selection_list[user_number - 1]


def dispaly_table(table_data=None, table_headers=None, index_req=False, align="l"):
    ret_val = ""
    try:
        table_data = table_data.copy()
        if table_headers is not None:
            table_headers = table_headers.copy()
    except:
        pass
    if table_headers is []:
        table_headers = None
    if isinstance(table_data, str):
        table_data = table_data.split(',')
    elif isinstance(table_data, dict):
        table_data = dict_to_list(table_data)
    # Process list to make it into 2d list to display.
    try:
        if not isinstance(table_data[0], tuple) and not isinstance(table_data[0], list) and \
                not isinstance(table_data[0], dict):
            tmp_list = list()
            for item in table_data:
                tmp_list.append(list([item]))
            table_data = tmp_list
    except:
        pass

    if index_req:
        if table_headers is not None:
            table_headers.insert(0, "#")
        counter = 1
        for rows in table_data:
            rows.insert(0, counter)
            counter += 1

    # Calculate required column width for each column
    column_widths = []
    for rowData in table_data:
        index = 0
        for item in rowData:
            item_length = len(str(item))
            try:
                if column_widths[index] < item_length:
                    column_widths[index] = item_length
            except:  # if null pointer
                column_widths.append(item_length)
            index += 1
    if table_headers is not None:
        index = 0
        for item in table_headers:
            item_length = len(str(item))
            try:
                if column_widths[index] < item_length:
                    column_widths[index] = item_length
            except:  # if null pointer
                column_widths.append(item_length)
            index += 1

    # Calculate the edge to be displayed at the top and bottom
    top_edge = "+"
    middle_edge = "+"
    bottom_edge = "+"

    first_loop = True
    for columnWidth in column_widths:
        if first_loop is False:
            top_edge += "+"
            middle_edge += "+"
            bottom_edge += "+"
        top_edge += "-" * (columnWidth + 2)
        middle_edge += "-" * (columnWidth + 2)
        bottom_edge += "-" * (columnWidth + 2)
        first_loop = False

    top_edge = top_edge + "+"
    middle_edge = middle_edge + "+"
    bottom_edge = bottom_edge + "+"

    # Always add the top reguardless of table headers or not.
    ret_val += top_edge + "\n"
    # Add table headers section
    if table_headers is not None:
        row_string = "|"
        index = 0
        for item in table_headers:
            spaces = (column_widths[index] - len(str(item)) + 2)
            if align.lower() in "l":
                row_string += str(item) + " " * spaces + "|"
            elif align.lower() in "c":
                prefix = " " * math.floor(spaces/2)
                suffix = " " * math.ceil(spaces/2)
                row_string += prefix + str(item) + suffix + "|"
            elif align.lower() in "r":
                row_string += " " * spaces + str(item) + "|"
            index += 1
        ret_val += row_string + "\n"
        ret_val += middle_edge + "\n"
    # Add table data section
    for rowData in table_data:
        index = 0
        row_string = "|"
        for item in rowData:
            spaces = (column_widths[index] - len(str(item)) + 2)
            if align.lower() in "l":
                row_string += str(item) + " " * spaces + "|"
            elif align.lower() in "c":
                prefix = " " * math.floor(spaces/2)
                suffix = " " * math.ceil(spaces/2)
                row_string += prefix + str(item) + suffix + "|"
            elif align.lower() in "r":
                row_string += " " * spaces + str(item) + "|"

            index += 1
        ret_val += row_string + "\n"
    ret_val += bottom_edge
    print(ret_val)
    return ret_val


def dict_to_list(table_data):
    tmp_list = []
    for k, v in table_data.items():
        tmp_list2 = list()
        tmp_list2.append(v)
        tmp_list2.append(k)
        tmp_list.append(tmp_list2)
    table_data = tmp_list
    return table_data
