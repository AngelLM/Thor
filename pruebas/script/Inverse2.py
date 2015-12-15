from PyKDL import *
from math import *

thor = Chain()
thor.addSegment(Segment(Joint(Joint.RotZ), Frame(Vector(0,0,201.5))))
thor.addSegment(Segment(Joint(Joint.RotY), Frame(Vector(0,0,160))))
thor.addSegment(Segment(Joint(Joint.RotY), Frame(Vector(0,0,89.5))))
thor.addSegment(Segment(Joint(Joint.RotZ), Frame(Vector(0,0,104.5))))
thor.addSegment(Segment(Joint(Joint.RotY), Frame(Vector(0,0,66.5))))
thor.addSegment(Segment(Joint(Joint.RotZ)))

ik_solver = ChainIkSolverPos_LMA(thor)

current_angles = JntArray(thor.getNrOfJoints())
result_angles = JntArray(thor.getNrOfJoints())
sending_angles = JntArray(thor.getNrOfJoints())

fin=0

while fin==0:
	x=input("x: ")
	y=input("y: ")
	z=input("z: ")

	target_frame = Frame(Vector(x+0.001,y+0.001,z+0.001))

	print 'Angulo de partida: ', degrees(current_angles[0]), degrees(current_angles[1]), degrees(current_angles[2]), degrees(current_angles[3]), degrees(current_angles[4]), degrees(current_angles[5]), '\n'

	ik_solver.CartToJnt(current_angles, target_frame, result_angles)

	print 'Angulos antes del round: ', degrees(result_angles[0]), degrees(result_angles[1]), degrees(result_angles[2]), degrees(result_angles[3]), degrees(result_angles[4]), degrees(result_angles[5]), '\n'


	for i in [0, 1, 2, 3, 4, 5]:
		sending_angles[i]=round(degrees(result_angles[i]),0)

	print 'Angulos tras round: ', sending_angles[0], sending_angles[1], sending_angles[2], sending_angles[3], sending_angles[4], sending_angles[5], '\n'
	
	while fin==0 and (sending_angles[0]>180 or sending_angles[0]<-180 or sending_angles[1]>90 or sending_angles[1]<-90 or sending_angles[2]>90 or sending_angles[2]<-90 or sending_angles[3]>180 or sending_angles[3]<-180 or sending_angles[4]>90 or sending_angles[4]<-90 or sending_angles[5]>180 or sending_angles[5]<-180):
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
				print 'break',i,'\n'
				fin=1

	print 'Angulos tras filtro: ', sending_angles[0], sending_angles[1], sending_angles[2], sending_angles[3], sending_angles[4], sending_angles[5], '\n'
	
	for i in [0, 1, 2, 3, 4, 5]:
		current_angles[i]=radians(sending_angles[i])

#	fin=input("Fin? 1")