# Modbus-Simulator-Setup
This setup is intended to be used on any IoT Gateway depending on the OS and ARCH for edge processing and connecting to real Modbus addresses.

## Setting up ModbusPal:
ModbusPal is a Java Modbus simulator with GUI to control and simulate the Modbus connection.
The below components are required if you are palnning to use Modbus to USB converter. For which Serial Communication should be enabled for ModbusPal library. 
```
rxtxSerial.dll
rxtxParallel.dll
RXTXcomm.jar
```
Based on the ARCH and OS you can download the above componets https://bitbucket.org/jlauer/mfz-cdn/downloads/ 
Thanks to [Joe Lauer](https://bitbucket.org/jlauer/).

## For setting up in Windows x64:

**Note:** Set the JAVA path properly pointing to JDK and not to JRE. If JRE is set, uninstall it from Control Panel.
Should set JAVA Path in the environment (Windows):
```
JAVA_HOME: C:\Program Files\Java\jdk1.8.0_202
JRE_HOME: %JAVA_HOME%\jre
Path: %JAVA_HOME%\bin
```
```
Copy RXTXcomm.jar ---> <JAVA_HOME>\jre\lib\ext
Copy rxtxSerial.dll ---> <JAVA_HOME>\jre\bin
Copy rxtxParallel.dll ---> <JAVA_HOME>\jre\bin
```

Run:
> java -jar ModbusPal.jar

A GUI will pop-up on the screen.
![alt text](https://github.com/niladri30/Modbus-Simulator-Setup/blob/master/modbuspal1.PNG)

## Starting the Modbus Simulator
1. Open the ModbusPal Server.
2. Check settings. TCP Port: 502
3. Add a module slave:
    - Choose Add in Module Slaves fieldset.
    - A new window will open.
4. Select 1 from the list-view and assign a name to the slave.
5. Choose Add.
6. Edit holding registers for the slave:
	  - Choose the button with the eye image.
7. On the Holding registers tab choose Add.
8. In the Add registers popup input 1 to 10 and choose Add.
9. In the table double click on the first row at the column named "value" and put the value 533.
	  - Address 1: 533
10. Close the popup.
11. Choose Run.
12. Open Console to see the messages.

## Python code to read the messages
Install [PyModbusTCP](https://pypi.org/project/pyModbusTCP/)
> pip install pyModbusTCP

Execute the python script `Modbus_read.py` to read the values from holding registers.
