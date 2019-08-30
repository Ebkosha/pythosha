from robodk import*
from robolink import*
RDK = Robolink()

prog = RDK.AddProgram('AutoProgram')

program.setDO(2, 1)
pause(1)
program.setDO(1, 0)
pause(1)