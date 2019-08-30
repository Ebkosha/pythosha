from robodk import*
from robolink import*
RDK = Robolink()

program = RDK.AddProgram('shift')

program.setDO(2, 1)
pause(1)
program.setDO(1, 0)
pause(1)

RDK.RunCode("shift", True)

pause(3)

program.Delete()