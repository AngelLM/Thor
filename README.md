<img src="doc/logo.png" width="500" align="center">

Thor is an Open Source and printable robotic arm with six degrees of freedom.
Its configuration (yaw-roll-roll-yaw-roll-yaw) is the same one that is used on most manipulator robots that currently exist in the market.
In its upright position, Thor is about 625mm and it can lift objects up to 750 grams.

<img src="doc/main.jpg" width="800" align="center">

The project started a year ago as my Final Degree Project called "Design and startup of an Open Source and printable 6DOF robotic arm" but a lot of things have changed since the presentation day.

The main purpose of this project was to create a robotic arm that could be used in universities and schools to teach robotics instead of using simulation software or low accurate models. Having this in mind, the final prototype had to be affordable and, of course, Open Source. Once the project begun, I realized that it could be helpful in many areas I had not imagined when I first came up with the idea: small automations, training in factories, makers...

As I said, this is a low-cost robotic arm. The cost of the whole materials is under 350€. Being this affordable, I think almost every school/university/maker could make good use of one at least!

In terms of licenses, I wanted this project to be Open Source because I want anyone to have the opportunity to study, modify and improve it. Given this decision, I designed it entirely using Open Source software. This way, everyone can open the source files and modify them without buying licenses of proprietary software (sometimes unaffordable). There is not a single reason for not hacking Thor!

More about this project on the [Hackaday post](https://hackaday.io/project/12989-thor)!

## Community  
If you are interested in this project, please consider joining [our mail list](https://groups.google.com/forum/#!forum/thor-opensource-3d-printable-robotic-arm).


# Repository Index
* [doc](https://github.com/AngelLM/Thor/tree/developer/doc) - Misc documentation files
* [electronics](https://github.com/AngelLM/Thor/tree/developer/electronics) - ControlPCB & SensorPCB KiCAD, gerbers & GCODE files
* [freecad-src](https://github.com/AngelLM/Thor/tree/developer/freecad-src) - FreeCAD source files of every piece of Thor
  * [accessories](https://github.com/AngelLM/Thor/tree/developer/freecad-src/accessories) - Accessories for Thor (tools & end-effectors)
  * [animation](https://github.com/AngelLM/Thor/tree/developer/freecad-src/animation) - FreeCAD files used to animate the assembly. Check the [ExplodedAssembly FreeCAD workbench](https://github.com/JMG1/ExplodedAssembly)
  * [modifications](https://github.com/AngelLM/Thor/tree/developer/freecad-src/modifications) - Modifications made by some users
* [step](https://github.com/AngelLM/Thor/tree/developer/step) - step files of every piece of Thor
* [stl](https://github.com/AngelLM/Thor/tree/developer/stl) - stl files of every piece of Thor
  * [modifications](https://github.com/AngelLM/Thor/tree/developer/stl/modifications) - Modifications made by other users
* firmware - The firmware used in this project is a GRBL modification that can be found on [this repository](https://github.com/AngelLM/grbl)
* [FAQ](https://github.com/AngelLM/Thor/blob/developer/FAQ.md) - Frequently Asked Questions
* [ThorBuilders](https://github.com/AngelLM/Thor/blob/developer/ThorBuilders.md) - List of Thor builders
# Contributors

* [AngelLM](https://github.com/AngelLM): Main author. Released the project as Open Source and is the current maintainer.

* [Danny-VdH](https://github.com/Danny-VdH): Check his modifications & features at [Hackaday post: Thor robot with addons and GUI](https://hackaday.io/project/16665-thor-robot-with-addons-and-gui)!

Do not hesitate on contributing to this project!


# Thanks

Until March of 2016 this project was sponsored by BQ, I would like to thank the company and my colleagues because without them, this project would have not been possible.
Also I would like to thank Miguel Hernando, who was my Final Degree Project tuthor, for his help and awesome tips.
Of course, I also would like to thank my friends and family for the support and the hours of listening.


# License

<img src="doc/By-sa.png" width="200">

All files included in this repository are licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/)
