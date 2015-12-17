import bpy
import math
import time

import sys
import serial
import glob

"""port=''.join(glob.glob("/dev/ttyUSB*"))
ser = serial.Serial(port,115200)
print("connected to: " + ser.portstr)"""


ob = bpy.data.objects['Armature']
bpy.context.scene.objects.active = ob

bpy.ops.object.mode_set(mode='POSE')

offset1=0
offset2=0
offset3=0
offset4=0
offset5=0



def get_local_orientation(pose_bone):
    local_orientation = pose_bone.matrix_channel.to_euler()
    if pose_bone.parent is None:
        return local_orientation
    else:
        x=local_orientation.x-pose_bone.parent.matrix_channel.to_euler().x
        y=local_orientation.y-pose_bone.parent.matrix_channel.to_euler().y
        z=local_orientation.z-pose_bone.parent.matrix_channel.to_euler().z
        return(x,y,z)


def sendAngles():
	
	bone1=ob.pose.bones['Art1']
	bone2=ob.pose.bones['Art2']
	bone3=ob.pose.bones['Art3']
	bone4=ob.pose.bones['Art4']
	bone5=ob.pose.bones['Art56']
	
	angle1=str(round(math.degrees(get_local_orientation(bone1)[2])+offset1))#[0]=x,[1]=y,[2]=z
	angle2=str(round(math.degrees(get_local_orientation(bone2)[0])+offset2))
	angle3=str(round(math.degrees(get_local_orientation(bone3)[0])+offset3))
	angle4=str(round(math.degrees(get_local_orientation(bone4)[2])+offset4))
	angle5=str(round(math.degrees(get_local_orientation(bone5)[0])+offset5))
	print( "%s  %s  %s  %s  %s  \n" %( angle1, angle2, angle3, angle4, angle5 ) )

	#ser.write((angle1+','+angle2).encode('UTF-8'))





def frameChange(passedScene):
	
	sendAngles()
    
bpy.app.handlers.frame_change_pre.append(frameChange)