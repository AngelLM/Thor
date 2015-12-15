from PyKDL import *
from math import *
import serial
import time

puerto0='/dev/ttyUSB0'
puerto1='/dev/ttyUSB1'

s0=serial.Serial(puerto0,115200)
s1=serial.Serial(puerto1,115200)
time.sleep(2)

s0.write('M17 \n')
s1.write('M17 \n')

thor = Chain()
thor.addSegment(Segment(Joint(Joint.RotZ), Frame(Vector(0,0,201.5))))
thor.addSegment(Segment(Joint(Joint.RotY), Frame(Vector(0,0,160))))
thor.addSegment(Segment(Joint(Joint.RotY), Frame(Vector(0,0,89.5))))
thor.addSegment(Segment(Joint(Joint.RotZ), Frame(Vector(0,0,104.5))))
thor.addSegment(Segment(Joint(Joint.RotY), Frame(Vector(0,0,66.5))))
thor.addSegment(Segment(Joint(Joint.RotZ)))

"""q_min = JntArray(thor.getNrOfJoints())
q_max = JntArray(thor.getNrOfJoints())

q_min[0]=-3.14
q_min[1]=-1.57
q_min[2]=-1.57
q_min[3]=-3.14
q_min[4]=-1.57
q_min[5]=-3.14

q_max[0]=3.14
q_max[1]=1.57
q_max[2]=1.57
q_max[3]=3.14
q_max[4]=1.57
q_max[5]=3.14


fksolver = ChainFkSolverPos_recursive(thor)
iksolver = ChainIkSolverVel_pinv_givens(thor)"""

ik_solver = ChainIkSolverPos_LMA(thor)
# inv_pos_solver = ChainIkSolverPos_NR_JL(thor,q_min,q_max,fksolver,iksolver)

current_angles = JntArray(thor.getNrOfJoints())
result_angles = JntArray(thor.getNrOfJoints())
sending_angles = JntArray(thor.getNrOfJoints())

fin=0

while fin!=1:
	x=input("x: ")
	y=input("y: ")
	z=input("z: ")

	target_frame = Frame(Vector(x+0.001,y+0.001,z+0.001))
	
	print 'Angulo de partida: ', degrees(current_angles[0]), degrees(current_angles[1]), degrees(current_angles[2]), degrees(current_angles[3]), degrees(current_angles[4]), degrees(current_angles[5]), '\n'

	ik_solver.CartToJnt(current_angles, target_frame, result_angles)

	for i in [0, 1, 2, 3, 4, 5]:
		sending_angles[i]=round(degrees(result_angles[i]),0)
	
	while sending_angles[0]>180 or sending_angles[0]<-180 or sending_angles[1]>90 or sending_angles[1]<-90 or sending_angles[2]>90 or sending_angles[2]<-90 or sending_angles[3]>180 or sending_angles[3]<-180 or sending_angles[4]>90 or sending_angles[4]<-90 or sending_angles[5]>180 or sending_angles[5]<-180:
		for i in [0,3,5]:
			if sending_angles[i]>180:
				sending_angles[i]=sending_angles[i]-360
			elif sending_angles[i]<=-180:
				sending_angles[i]=sending_angles[i]+360

		for i in [1,2,4]:
			if sending_angles[i]>=360:
				sending_angles[i]=sending_angles[i]-360
			elif sending_angles[i]<=-360:
				sending_angles[i]=sending_angles[i]+360
			elif sending_angles[i]>=270:
				sending_angles[i]=sending_angles[i]-360
			elif sending_angles[i]<=-270:
				sending_angles[i]=360+sending_angles[i]
			elif (sending_angles[i]>90 and sending_angles[i]<270) or (sending_angles[i]<-90 and sending_angles[i]>-270):
				print 'Angulos intentados: ', sending_angles[0], sending_angles[1], sending_angles[2], sending_angles[3], sending_angles[4], sending_angles[5], '\n'
				for j in [0,1,2,3,4,5]:
					sending_angles[j]=current_angles[j]
				print 'Punto inalcanzable, introduce otro',i,'\n'


	print 'Angulos enviados: ', sending_angles[0], sending_angles[1], sending_angles[2], sending_angles[3], sending_angles[4], sending_angles[5], '\n'
	
	for i in [0, 1, 2, 3, 4, 5]:
		current_angles[i]=radians(sending_angles[i])

	s0.write("G01 F2000 X"+str(sending_angles[0])+" Y"+str(sending_angles[1])+" Z"+str(sending_angles[2])+" \n")
	s1.write("G01 F2000 X"+str(sending_angles[3])+" Y"+str(sending_angles[4])+" Z"+str(sending_angles[5])+" \n")
	s0.flush()
	s1.flush()
	
	fin=input("Fin? 1")

s0.write('M18 \n')
s1.write('M18 \n')

s0.close()
s1.close()