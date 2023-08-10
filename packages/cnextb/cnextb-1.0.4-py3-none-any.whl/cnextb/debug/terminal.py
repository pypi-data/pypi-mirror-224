from cnextb.device import *


def main():

    module_str = userSelectDevice(additional_options=["rescan", "quit"])

    if module_str == "quit":
        return 0
    print("Selected module is: " + module_str)

    cnextb_device = CnextbDevice(module_str)

    while True:
        user_input = input("Send command to " + str(module_str) + " :" + "\n>")

        if user_input.startswith("$"):
            if "$s" in user_input.lower().replace(" ", ""):
                break
            elif "$c" in user_input.lower():
                cnextb_device.closeConnection()
                return 0
            pass
        else:
            print(cnextb_device.sendCommand(user_input))


if __name__ == "__main__":
    while True:
        main()
