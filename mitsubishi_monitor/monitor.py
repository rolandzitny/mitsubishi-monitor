"""
The monitor is used for direct connection with equipment such as a robotic arm and PLC with
the aim of obtaining statistical data on energy consumption, movement of monitors, axis load, etc.

This monitor was taken from Mitsubishi's RT Toolbox3 monitoring software and specifically the oscilloscope function.

Each constant in const.py was obtained by intercepting the
communication between the connected computer and the device itself.
"""
import socket
import logging
from .util import Error, WrongIpAddress

msg_filling = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')


class Monitor:
    def __init__(self, robot_ip_addr, robot_port, datatype, monitor_ip_addr='0.0.0.0', monitor_port=0):
        """
        Initialization of monitor.
        :param robot_ip_addr: IP address of device
        :param robot_port: port of device
        :param datatype: const.MonitorType - type of collected data
        :param monitor_ip_addr: IP address of monitor, mostly 0.0.0.0 will work
        :param monitor_port: port of monitor, if you are on linux works well with 0, on Windows firewall blocks
                             receiving port, so you have to enable it.
                             Control Panel -> Security/Firewall -> right click on inbound -> new rule ->
                             -> set new UDP! port
        """
        self._robot_ip_addr = robot_ip_addr
        self._robot_port = robot_port
        self._datatype = datatype
        self._monitor_ip_addr = monitor_ip_addr
        self._monitor_port = monitor_port
        self._socket = None
        self.logger = logging.getLogger(__name__)
        try:
            socket.inet_aton(self._robot_ip_addr)  # Check whether IP address is valid
        except socket.error:
            self.logger.warning("IP_ADDR: {} PORT: {},  IP_ADDR is not valid".format(self._robot_ip_addr, self._robot_port))
            raise Error(WrongIpAddress)

    def end_communication(self):
        """
        RealTime monitor uses UDP communication, therefore it needs to be ended with this message.
        Otherwise, sender of features (robotic arm) will continue to send features endlessly.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        msg = bytearray(b'\xff\x00\x00\x00\x00\x00') + msg_filling
        self._socket.sendto(msg, (self._robot_ip_addr, self._robot_port))

    def create_message(self):
        """
        Creates message for device.
        :return: msg
        """
        msg = bytearray(b'\x01\x00\x00\x00') + self._datatype + msg_filling
        return msg

    def start_monitor(self):
        """
        Send LLC (IEEE 802.2 - logical link  control) message
        which tells your device to send data at a certain frequency.
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((self._monitor_ip_addr, self._monitor_port))
        self._socket.sendto(self.create_message(), (self._robot_ip_addr, self._robot_port))

    def receive_data(self):
        """
        Receive UDP (in real-time) / TCP (otherwise) response from your device.
        This response needs to be parsed and this library provides parsing methods in util.py.
        """
        response = self._socket.recv(512)
        return response
