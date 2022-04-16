![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/sensors-on-carrier.jpg?raw=true)
_Solution to install sensors inside TouchScreen case for WHAQM project_

## WHAQM Sensor Carrier Board

Ultimately the sensor carrier board will be 3D printed but for now I just wanted to get something in place that would keep the build process moving along.  I happened to have some extra PCB prototyping boards in my parts supply so using them was a simple short term solution.  The process would include identifying a usable board and then drilling some holes to affix the sensors to the board with some M2 sized screws.  Using screws for my initial designs facilitated the ability to move various sensors as I explored placement options.  This would be very instrumental later as thermal issues became more problematic than expected. 

My initial selection of possible options produced these three boards:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/carrier-first-options.jpg?raw=true)_Some PCB options_

The first board on the left is an original Raspberry Pi Hat prototyping board and while it already has the case mounting holes pre-drilled it was too small to hold all three sensors. The middle board had enough space but needed holes drilled for mounting in the case.  The last board on the right is too large for the case and will need case mounting holes drilled as well.  

Originally I selected the middle board and proceeded to drill holes to accommodate the three sensor devices:  
![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/pcb_spacing.jpg?raw-true)_Sensor layout_

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/first-carrier-board.jpg?raw=true)_Holes drilled_

This board worked well for my initial builds but it soon became apparent that  due to thermal considerations there would be a requirement  for a more accommodating sensor placement.  As a result it was necessary to use the larger blank PCB and modify it to fit in the SmartiPi case as well as drill new holes.

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/carrier-final-cut.jpg?raw=true)

The process of sizing and cutting the board was rather simple using the SmartiPi case as a quide and a small saw to do the cuts. 

 Here are a few images of that process:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/case-cut-line.jpg?raw=true)_Marking a cut line_

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/cut-with-bandsaw.jpg?raw=true)_Cutting with bandsaw - watch those fingers!_

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/cut-coner.jpg?raw=true)_Small corner cut for case screws_

After the PCB was modified to size I experimented with sensor placement over a period of several weeks.  Each new configuration required a new set of holes and ultimately resulted in a board that looked like this:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/carrier-final-cut.jpg?raw=true)_Final board with holes for various sensor configurations_

My current sensor placement on the carrier board is shown in the image at the beginning of this document and for the readers reference the final hole placement is shown below:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/carrier-board.jpg?raw=true)_Current hole requirements_

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/case-power-pi-sensors.jpg?raw=true)_Finished!_

