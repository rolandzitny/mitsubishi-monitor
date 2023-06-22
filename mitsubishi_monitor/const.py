"""
File const.py contains all possible and predefined types of monitoring.
MonitorType determines the types of obtained data.

Important:
    READ_TIME (approximately every 3.5 milliseconds) uses UDP, every other MonitorFreq uses TCP
"""
import enum


class DataType(enum.Enum):
    """
    To understand check documentation to RToolBox, specifically part about oscillograph.
    """
    END_COM                 = bytearray(b'\xff\x00')    # End UDP communication
    CURRENT_FEEDBACK        = bytearray(b'\xf3\x03')
    AXIS_LOAD_LEVEL         = bytearray(b'\x10\x00')
    POSITION_FEEDBACK       = bytearray(b'\x09\x00')
    JOINT_POSITION_CMD      = bytearray(b'\xea\x03')
    XYZ_POSITION_CMD        = bytearray(b'\xe9\x03')
    JOINT_POSITION_FB       = bytearray(b'\xf0\x03')
    XYZ_POSITION_FB         = bytearray(b'\xef\x03')
    POSITION_DROOP          = bytearray(b'\x0d\x00')
    SPEED_FB                = bytearray(b'\x0f\x00')
    VOLTAGE                 = bytearray(b'\x13\x00')
    RMS_CURRENT             = bytearray(b'\xf6\x03')
    REGENERATION_LEVEL      = bytearray(b'\x14\x00')
    ENCODER_TEMPERATURE     = bytearray(b'\x11\x00')
    CURRENT_COMMAND         = bytearray(b'\xf2\x00')
    TOLERABLE_COMMAND_PLUS  = bytearray(b'\xf5\x03')
    TOLERABLE_COMMAND_MINUS = bytearray(b'\xf4\x03')
    FORCE_SENSOR            = bytearray(b'\x65\x00')
    FORCE_POS_CMD_XYZ       = bytearray(b'\x68\x00')
    COL_THRESHOLD_PLUS      = bytearray(b'\x70\x00')
    COL_THRESHOLD_MINUS     = bytearray(b'\x71\x00')
    COL_PRESUMED_TORQUE     = bytearray(b'\x6f\x00')
    COL_TORQUE              = bytearray(b'\x0b\x00')
    REF_VAL_OF_COL_LVL      = bytearray(b'\x72\x00')
    ERR_OF_PRESUMED_TORQUE  = bytearray(b'\x83\x00')
    EX_T_COORD_SPEED        = bytearray(b'\x18\x00')
    EX_T_COORD_POSITION     = bytearray(b'\x19\x00')
    SPLINE_PATH_POINT_OF_ADJ= bytearray(b'\x1a\x00')
    ROBOT_INFORMATION       = bytearray(b'\x0c\x00')
    STATE_OF_DSI_INPUT      = bytearray(b'\x84\x00')
    DSI_A_SIGNAL            = bytearray(b'\x85\x00')
    DSI_B_SIGNAL            = bytearray(b'\x86\x00')
    SCNI_SIGNAL             = bytearray(b'\x87\x00')
    PM_SCORE_GEAR           = bytearray(b'\x1d\x00')
    PM_SCORE_ENCODERDATA    = bytearray(b'\x1e\x00')
    PM_SCORE_ENCODERCOMM    = bytearray(b'\x1f\x00')
