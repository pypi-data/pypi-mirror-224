from __future__ import annotations
import serial
import serial.tools.list_ports as serialports
import atexit


class SerialDeviceInfo:
    def __init__(self, vid=None, pid=None, serial_number=None):
        self.vid = vid
        self.pid = pid
        self.serial_number = serial_number

    def __eq__(self, other: SerialDeviceInfo):
        return self.vid == other.vid and \
            self.pid == other.pid and \
            self.serial_number == other.serial_number


class SerialPortScanner:
    def __init__(self):
        self.ports = {}  # Opened serial ports - {str(board ID): Serial object}
        self.port_names = {}  # Port names - {str(board ID): str(USB COM port names (eg COM3 or /dev/ttyACM2)}
        self.nPorts = 0  # Number of opened serial ports
        self._en_debug = True

    def enable_debug(self, en=True):
        self._en_debug = en

    # ---------------------- SERIAL ----------------------#

    def find_ports(self, target_device: SerialDeviceInfo = None):
        """
        Looks through available serial ports for a device with a particular
        VendorID and ProductID and unique ID
        Returns port string or None if not found.

        find_port(str) -> [str(port),str(SNR)] OR []
        """
        # Map devices to (VID, PID, SER) as strings

        # Retrieve target IDs
        board_ids = [self.ports.keys()]  # Board serial numbers (each should be unique)

        i = 1
        if self._en_debug:
            print("Finding devices...")
        for port in serialports.comports():  # Scan available COM ports
            # ignore devices without device info
            if (port.pid is None) or (port.vid is None):
                continue
            _id = port.serial_number
            # print(port, hex(port.vid), hex(port.pid), port.serial_number)
            if target_device is None:
                self.port_names[_id] = port.device  # Assign ID to port

            # Check VID and PID are consistent
            elif (port.vid == target_device.vid and  # VID
                  port.pid == target_device.pid):  # PID
                # FIXME - doesn't currently check for serial number

                # print('\t{:0>12x} on {}'.format(id,))
                if self._en_debug:
                    print('\t{} on {} [{}]'.format(_id, port.device, port.description))
                try:
                    i_id = board_ids.index(_id)
                    # print('Exists! Closing: {}'.format(board_ids[i_id]))
                    # If entry exists, close old port and update location
                    # #TO DO: CLOSE PORT IF OPEN!##########

                    # MEANTIME - keep all entries (REMOVE THIS WHEN IDs ARE UNIQUE!)
                    _id = (i << 8) + _id
                    i += 1
                    print('\t...duplicate ID! Modifying duplicate {:0>12x} to {:0>12x}'.format(board_ids[i_id], id))
                except ValueError:
                    board_ids.append(_id)

                # TO DO - send a checking command to device to confirm whisker board

                self.port_names[_id] = port.device  # Assign ID to port
                self.ports[_id] = None  # Assuming all ports are closed at this point.
                # TO DO: CHECK FOR PORTS WHICH ALREADY MATCH EXISTING

        # if self._en_debug:
        #     print("{} device(s) found at: {}".format(len(self.port_names),
        #                                              list(self.port_names.values())))
        if len(self.port_names) == 0:
            return None
        return list(self.port_names.values())[0]  # NB only need one

    def open_serial_ports(self, baud=115200):
        print("Opening ports...")
        if len(self.port_names) == 0:
            print("No devices found!")
            raise SystemExit
        devices = self.ports.keys()
        for _id in devices:  # range(len(self.ports)): #Open serial ports
            try:
                self.ports[_id] = serial.Serial(self.port_names[_id], baud,
                                                timeout=2)  # self.ser_ports.append([ser,self.ports[i][1]])
                print("\t{}".format(self.port_names[_id]))

                atexit.register(self.close_serial_ports)  # Arrange to close ports on system exit
            except serial.serialutil.SerialException as e:
                print(e)
                raise SystemExit

        self.nPorts = len(self.ports)  # Set number of open boards

    def close_serial_ports(self):
        print("Closing serial ports...")
        # for id, port in self.ports.items():
        for port in self.ports.values():
            print("\t{}".format(port.port))
            port.close()
        self.ports = {}

        print("Done!")
