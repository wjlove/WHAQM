**An attempt to expand on the excellent work of balenAIR**

#Pre-Alpha work - You have been warned! This is only the outline for the readme

This project is new iteration on the balenAIR project and attempts to add some enhanced functionality including the the ability
to have a graphical UI local to the device and the ability to collect information from other devices in the balenAIR family.  By itself it is a completely contained air quaility monitor with a navigatable touch screen display.  When combined with other devices it comes a centralized plaform for displaing the air quality of multiple locations along with historical information.   

A new alerting system will provide not only warnings about current hazardous conditions but also display furture trending information to predict possible hazardous situations. 

## Hardware - 
(need links and detail)
    - Raspi 3 or 4 (good luck)
    - 7in Touch Screen Display
    - Smarti Pi Touch Pro Case (Small)
    - PMSA0031
    - SCD-40
    - SQP-30
    - Qwiic wire jumpers
    - Carrier PCB

Detailed discussion exctracted from the Blog posts goes here

## Software
(multiple balena/external blocks)
    - IAQ balena block
    - InfluxDB docker container
    - dashboard balena block
    - connector balean block
    - MQTT docker container
    - wifi-connect balena block
    - bowser balean block

Detailed discussion including balean Cloud options and variables goes here.


## Configuration

### Basic Setup
- Changes to various config files shouldn't be necessary
- Change device name

### Additional Devices
- 
## Missing 

All of the above :) ^^^^

