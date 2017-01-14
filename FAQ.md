# FREQUENT ASKED QUESTIONS

**I have a question, where should I ask?**
I suggest you to use the [Google Groups Community](https://groups.google.com/forum/#!forum/thor-opensource-3d-printable-robotic-arm). In this way, other users with the same question will find the answer easily.

**Where can I find more documentation about this project?**
There are 3 main sites where you'll find info about this project:
* [Hackaday.io Project Page](https://hackaday.io/project/12989-thor)
* [GitHub Repository](https://github.com/AngelLM/Thor)
* [Google Groups Community](https://groups.google.com/forum/#!forum/thor-opensource-3d-printable-robotic-arm)

**Where can I find the latest version of Thor?**
You can find the updated version at [Thor's GitHub repository](https://github.com/AngelLM/Thor).

**How much costs to build this robot arm?**
The total cost of components is around 350€. It is understood that you have access to a 3D printer where you can print all the pieces.

**How much time is required to build this robot arm?**
The total printing time is around 200 hours. Once printed, the assembly takes 6 hours more or less.

**What are the components used in this project?**
Here is a [list of materials](https://github.com/AngelLM/Thor/blob/developer/ListOfMaterials.md) where you will find every component used in this project.

**Where can I buy the components?**
As most component I have used are also used to build 3D printers, you would find many of them in this kind of stores.

**Where can I buy a kit?**
Currently I don't know anyone who sells a Thor kit. I'm not selling kits because the printing time is such that it would be very expensive.

**What are the robot dimensions?**
Fully  stretched vertically Thor is 624,15mm (height) without the tool. In [this picture](https://github.com/AngelLM/Thor/blob/developer/ThorDimensions.png) you can see better it's dimensions.

**How much weight can Thor lift?**
Currently, the maximum load I succeeded to lift is 750 grams (including the tool weight). Thor can still lift that load when it's stretched horizontally, which is the worst scenario.

**What is the fastest speed Thor can reach?**
At this time I have not tested this yet. Coming soon.

**What is its positioning accuracy?**
It depends on each articulation. The first two articulations have an accuracy of less than a degree. Third one has about a degree. Forth has about an error of 2 degrees. And the lasts two articulations have the worst accuracy, with an error of 3-4 grades more or less.
Note 1: All of this data was collected manually and refers to my own prototype. The accuracy is directly linked to the printing accuracy and the assembly.  
Note 2: as the current design has not feedback sensors to ensure the position I have assumed that the robot is moving well and is not missing steps.

**What are the electronics used in this project?**
The board that runs the firmware is an Arduino Mega. The board where all actuators and sensors are connected to is a custom PCB I designed.

Note: Some users are using commercial boards to control Thor instead of using the Arduino Mega and making the Control PCB board.

**What is the firmware used to control the movements?**
I'm using a [modified version of GRBL](https://github.com/AngelLM/grbl) to control Thor.

**How is the communication between the user and the robot arm?**
Currently, the communication is not too intuitive. To control the robot I send the values of each articulation rotation via serial to the Arduino. As I am using GRBL to control it, the code sent is a custom G-Code.

Note: There are users developing a Graphical User Interface (GUI) that are much more intuitive that my method.

**How can I collaborate to this project?**
You can give feedback to the community, show your progress, share the project, answer other users' questions, etc.
If you are interested in the development of the project you can also make your own modifications and share them with the community.
Let's make this greater!

**Under what license this project is shared?**
All files of the project are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/).

**What I'm allowed to do with the CC-BY-SA license?**
As the [CC-BY-SA License](http://creativecommons.org/licenses/by-sa/4.0/) goes, you are free to share and adapt the material for any purpose, even commercially.
In any case that you must give appropriate credit, provide a link to the license and indicate if changes were made. If you remix, transform, or build upon the material you must distribute your contributions under the same license as the original.
No warranties are given. The license may not give you all of the permissions necessary for your intended use.

**Why are you sharing Thor for free?**
One of the main purposes of this project is to bring people closer to robotics. I thought that it would have more success sharing it for free.
Also, as I'm really concerned about OpenSource, I did it using OpenSource tools. It made sense to me to share it using an OpenSource license too.
Finally, as this project is Open, anyone can upgrade it and share it with the community. Making this project greater than what could have been if developed only by me.

**What tools have you used in the development of Thor?**
These are the software tools I have used:
 * [FreeCAD](http://www.freecadweb.org/): 3D Design
 * [Blender](https://www.blender.org/): 3D Design
 * [KiCaD](kicad-pcb.org/): Electronic Design
 * [Atom](https://atom.io/): Building Text Editor
 * [Cura](https://ultimaker.com/en/products/cura-software): Slicing Software
 * [bCNC](https://github.com/vlachoudis/bCNC): CNC controller
These are the hardware tools I have used:
 * [Prusa i3 custom](http://reprap.org/wiki/Prusa_i3): 3D Printer
 * [Witbox](https://www.bq.com/es/witbox-2): 3D Printer
 * [Cyclone PCB Factory](http://reprap.org/wiki/Cyclone_PCB_Factory): CNC
