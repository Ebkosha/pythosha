from robodk import*
from robolink import*
RDK = Robolink()
robot = RDK.Item("KUKA KR 3 R540")

x = 401.838
y = 0.000
z = 234.142

t1 = RDK.AddTarget("t1")
fz = t1.Pose()
print(fz)
mz = fz[2, 3]
print(mz)
rz = mz - z + 1
print(rz)
pause(2)

target = RDK.AddTarget("T1")
target.setAsCartesianTarget()
target.setJoints([0,0,0,0,0,0])
target.setPose(KUKA_2_Pose([x, y, rz, -180.000, 0.000, 180.000]))
robot.MoveJ(target)

'''joints = robot.Joints().list()
print(angle)
r1=joints[0]
r6=joints[5]
r6=r6-r1 #Выравнивание фланса на 90. относительно Y 
r6=r6-angel #Поворот фланса по объекту
joints[5] = r6 #обозначение поворота для фланса
robot.MoveJ(joints) #вращение фланса

robot.MoveJ(joints)  # вращение фланса
r = requests.get("http://192.168.20.143:5001").text
try:
    exec(r) #присвоение Z координаты
except:
    pass
z=Zpos'''

fz = t1.Pose()
print(fz)
mz = fz[2, 3]
print(mz)
rz = mz - z + 1
print(rz)

pause(2)

target.setPose(KUKA_2_Pose([x, y, rz, -180.000, 0.000, 180.000]))
t1.Delete()
target.Delete()