"""
The file util.py provides the general majority of exceptions and allows
you to use various methods of parsing the data obtained from the device.
"""
import struct


class Error(Exception):
    """Base Error class"""
    pass


class WrongIpAddress(Error):
    """Wrong format of target IP address"""
    pass


def parse_current_feedback(response):
    """
    Parse 8 current feedbacks from Mitsubishi robotic arm.
    :param response: UDP response from device
    :return:
    """
    data = struct.unpack('>ffffffff', response[11:43])
    return data
