# Mitsubishi monitor - Mitsubishi MELFA robotic arm

This package allows you to use the _oscillograph_ function from the **RT Toolbox3** application for monitoring the 
required Mitsubishi MELFA robotic arms.

The purpose of this monitor is to record the energy consumption of the Mitsubishi robotic arm, but it also allows 
you to monitor other parameters, e.g. current position, speed, axial loading.

The overall communication is started by sending an initialization message, the length and shape of which is static, 
and the only part that changes is the type of required information from the monitored device. The monitored device 
then sends UDP packets with the required data approximately every 3.5 ms. The entire communication must then be 
terminated using the monitor method, otherwise the monitored device would constantly send data.

- Only realtime monitoring is implemented.

**Usage:**

```python
from mitsubishi_monitor import Monitor
from mitsubishi_monitor import DataType
from mitsubishi_monitor import parse_current_feedback

monitor = Monitor(robot_ip_addr='127.0.0.1',                 # IP addr of monitored device
                  robot_port=12000,                          # port of monitored device
                  datatype=DataType.CURRENT_FEEDBACK.value)  # type of monitoring

monitor.start_monitor()  # initialize communication

while True:
    data = parse_current_feedback(monitor.receive_data())  # receives UDP package
    print(data)
```
