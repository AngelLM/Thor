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

ik_solver = ChainIkSolverPos_LMA(thor)
current_angles = JntArray(thor.getNrOfJoints())

result_angles = JntArray(thor.getNrOfJoints())
fin=0

while fin!=1:
	x=input("x: ")
	y=input("y: ")
	z=input("z: ")

	target_frame = Frame(Vector(x,y,z))

	print 'Current: ', degrees(current_angles[0]), degrees(current_angles[1]), degrees(current_angles[2]), degrees(current_angles[3]), degrees(current_angles[4]), degrees(current_angles[5]), '\n'

	ik_solver.CartToJnt(current_angles, target_frame, result_angles)

	while result_angles[0]<-6.28 or result_angles[0]>6.28 or result_angles[1]<-3.14 or result_angles[1]>3.14 or result_angles[2]<-3.14 or result_angles[2]>3.14 or result_angles[3]<-6.28 or result_angles[3]>6.28 or result_angles[4]<-3.14 or result_angles[4]>3.14 or result_angles[5]<-6.28 or result_angles[5]>6.28:
		if result_angles[0]<-6.28:
			result_angles[0]=result_angles[0]+6.28
		if result_angles[0]>6.28:
			result_angles[0]=result_angles[0]-6.28
		if result_angles[1]<-3.14:
			result_angles[1]=result_angles[1]+3.14
		if result_angles[1]>3.14:
			result_angles[1]=result_angles[1]-3.14
		if result_angles[2]<-3.14:
			result_angles[2]=result_angles[2]+3.14
		if result_angles[2]>3.14:
			result_angles[2]=result_angles[2]-3.14
		if result_angles[3]<-6.28:
			result_angles[3]=result_angles[3]+6.28
		if result_angles[3]>6.28:
			result_angles[3]=result_angles[3]-6.28
		if result_angles[4]<-3.14:
			result_angles[4]=result_angles[4]+3.14
		if result_angles[4]>3.14:
			result_angles[4]=result_angles[4]-3.14
		if result_angles[5]<-6.28:
			result_angles[5]=result_angles[5]+6.28
		if result_angles[5]>6.28:
			result_angles[5]=result_angles[5]-6.28

	for i in [0, 1, 2, 3, 4, 5]:
		if result_angles[i]<0.001 and result_angles[i]>-0.001:
			result_angles[i]=0

	print 'Result: ', degrees(result_angles[0]), degrees(result_angles[1]), degrees(result_angles[2]), degrees(result_angles[3]), degrees(result_angles[4]), degrees(result_angles[5]), '\n'
	
	current_angles=result_angles
	s0.write("G01 F2000 X"+str(degrees(result_angles[0]))+" Y"+str(degrees(result_angles[1]))+" Z"+str(degrees(result_angles[2]))+" \n")
	s1.write("G01 F2000 X"+str(degrees(result_angles[3]))+" Y"+str(degrees(result_angles[4]))+" Z"+str(degrees(result_angles[5]))+" \n")
	
	fin=input("Fin? 1")

s0.write('M18 \n')
s1.write('M18 \n')

s0.close()
s1.close()