import POCOLib
from robotremoteserver import RobotRemoteServer

testlib = POCOLib.POCOLib()

RobotRemoteServer(testlib, host='0.0.0.0')

testlib.deinit()
