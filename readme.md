
 ![The Whole Home Air Quality Monitoring Project](https://github.com/wjlove/WHAQM/blob/main/documentation/images/two-display-sidebyside.jpg?raw=true)

_An extension of the balenAIR project that allows for multiple sensor devices in various location within your home or any indoor location_

# Whole Home Air Quality Monitoring Project
**_Both this code and documentation are currently under construction)_**

## Reasoning

My office door is often closed and I was wondering if the quality of the air in my office was affecting my health. I wanted to measure/understand the levels of hazardous gasses and overall CO2 concentrations in my office during working hours as those are good indicators of the quality of the air in an enclosed space.   There are many products on the market that individuals can purchase that will monitor indoor air quality, however as a tinkerer I wanted to explore building one myself.  After some online research into DIY and open source projects I came across the excellent baleaAIR (https://github.com/balena-io-playground/balena-iaq) endeavor and thought this might be interesting to build.  I started collecting the necessary components and proceeded constructing one following the guidelines provided inline.  

During the process of testing my initial build device I noticed that the measurements reported were wildly different throughout the day and often those measurement readings were in the described danger or warning zones.  I thought I’d done everything correctly, and indeed the values were changing over time, so what was possible explanation?  As one of several tests, I moved my device to another room in my home and noted markedly different results, these measurements were stable and “safe” and changed very slowly over time.  With those results in hand, I visited several other rooms in my home and noticed each one produced results that were generally slightly different by location and fluctuated only mildly during the day.  

 It is from here I wondered if having a sensor device in each room, monitored by a central location might be useful and thus this project was born. (And of course, I also stopped closing my office door!)

## New Features

At its core, this project is simply an extension of the great work done on the balenAIR project and adds the following features:

- A balenAIR like device with a touchscreen display
- Ability to collect data from multiple balenaAIR and WHAQM devices
- Ability to display aggregated measurements from all devices
- Ability to predict air quality conditions based on previous measurements - _not completed_
 
## Hardware Selection and Setup

The hardware items selected for use in this project are mostly defined by the balenAIR project and its original recommendations. There are a number of options when it comes to choosing these devices and cost, availability plus performance are some factors to consider when reviewing the parts below.

### Choosing your Pi

This project currently runs on a Raspberry Pi, so you'll need one of the following compatible devices:

- [Pi 3B](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)
- [Pi 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/)
- [Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

If you plan on having a significant number of sensor devices in multiple locations I would recommend that you consider using a Pi 4 as the main device. The air quality prediction software can be rather compute intensive over time and a Pi 4 also provides a "snappier" experience when using the touch screen.

### The Display and Case

There are several options for choosing a physical case that will house the Raspberry Pi, the touchscreen device and all the sensors. You can even consider making your own for a personal touch.  After some review and consideration I committed to the [SmartiPi Touch Pro - Small](https://smarticase.com/products/smartipi-touch-pro). It supports the original [Raspberry Pi Touch Display](https://www.raspberrypi.com/products/raspberry-pi-touch-display/) which I have selected as my prefered touchscreen device and has plenty of internal space to house all the necessary sensors.  Both are easily available for purchase, well supported and currently reasonably priced.  

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/case-display.jpg?raw=true)

### Sensors

The sensors used in this project evaluate the air surrounding the device and return data that is used to determine your air quality index or AQI. You can find more about how this number and how it is calculated at [AirNow](https://www.airnow.gov/aqi/aqi-basics/). Like balenAIR, WHAQM supports the three different sensors listed below. You can choose to have one, two, or all three present in your device, depending on your budget and air quality analysis needs.

| Sensor | Detects | Description |  Specifications (approx.) |
| ------------ | ----------- | ----------- | ----------- |
| [PMSA003I](https://www.adafruit.com/product/4632) | Smoke, dust, dirt, pollen particles | laser-scattering type  | 0.3-1.0,1.0-2.5, 2.5-10 Micrometer particles |
| [SCD-40](https://www.adafruit.com/product/5187) | Exhaled breath and burning fossil fuels |  CO2 photoacoustic sensor CO2 (plus temp and humidity)  | 400 - 2000 PPM |
| [SGP-30](https://www.adafruit.com/product/3709) | Gasses emitted by solid and liquid products  |  VOC (and eCO2) Hot-plate MOX sensor | eCO2 400-60,000 ppm, TVOC 0-60,000 ppb |

All of these sensors use the popular I2C protocol to communicate with the Pi and include [Qwiic](https://www.sparkfun.com/qwiic) connectors so you don't need to do any soldering to use these sensors.

### Sensor Carrier Board

Installing the sensors inside the SmartiPi case requires a seperate sensor carrier board.  Ideally and ultimately this will be a 3D printed part but considering the time involved in that process I simply fabricated one using a spare blank PCB.  You can read about that process [here](https://fix.this.later) along with details about its dimensions and hole locations.
![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/carrier-board.jpg?raw=true) _Carrier board with holes_

As it currently stands this design is not ideal as the amount of heat generated internally by both the Raspi and the touchscreen affect  the temperature measurements provided by the SCD-40 by as much as 5 degrees.  Various insulating mitigations can be applied to the case and carrier board to reduce this effect but my results to date have been varied.   The case does come with an optional fan which does resolve the issue but the additional noise created by it was unacceptable to me.
### Miscellaneous Items

Additionally you will need some SparkFun qwiic cables to connect the sensors together [100mm QT to QT cable](https://www.adafruit.com/product/4210) and a qwiic to female header cable to connect the sensors to the Raspberry Pi you selected [Qwiic to female header cable](https://www.adafruit.com/product/4397).  Lastly you will need a way to affix the sensors to the carrier board, I used some M2 screws and bolts but you could also use plastic spacers or double sided tape but I wouldn’t recommend the latter.

### Putting it All Together

I won’t go into much detail about setting up the SmartiPi case and installing the Raspberry Pi touchscreen as those details can be found on the [SmartiCase web site](https://smarticase.com/)  Installing your Raspberry Pi of choice and the sensor carrier board on the rear of the case is done using the supplied screws.  You may want to attach the power adapter before installing the carrier board as it is significantly harder to do so with that installed. 

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/case-with-power-pi.jpg?raw=true) *Install power connector first...*
![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/case-power-pi-sensors.jpg?raw=true) *...then the sensors.*

Don’t put the back cover on just yet, we have to install the software and that requires access to the Raspberry Pi in the back.  

## Software Setup

This project assumes a fairly advanced level of knowledge about BalenaCloud and the steps to necessary to create a new fleet and new devices. If this is your first time deploying a project and you want to learn more about balena Cloud, I recommend familiarizing yourself by following the steps in this [Getting Started](https://www.balena.io/docs/learn/getting-started/raspberrypi4-64/nodejs/) tutorial.   While working with the tutorial keep in mind the Raspberry Pi device type you choose to use while building your WHAQM display as you will need to select the appropriate one while creating your fleet. After you have created a fleet with devices in your balenaCloud dashboard you can `balena push` this code to it the traditional way.

**_Or…._**

You can deploy this project in one click using the button below:

[![balena deploy button](https://www.balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/wjlove/WHAQM)

This will automagiclly allow you to create (or use an existing) fleet, install the appropriate software and prepare everything for your first device deployment.  Pressing the button will walk you thru the necessary steps to get started. After providing the needed information balena Cloud will collect and build the appropriate software for your devices.  This will take some time, but you can follow the progress in the “Releases” window on the right:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/Screenshot-Build-in-Progress.jpg?raw=true) _Build in progress_

When everything is complete you should see:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/Screenshot-waiting-for-device.jpg?raw=true) _Ready for your first device!_

Now you can add your first device by clicking on the “+ Add device” button.  While following the Instructions on the right be sure to remember the device type you used to build your display.  If you plan on using your device’s wireless networking ability be sure to select “Network Connection -> Wifi + Ethernet” and enter the appropriate network information.

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/Screenshot-add-device.jpg?raw=true)

((this section of my docuemnt needs work as the Instructions on the right are not completely clear on how to flash a device/SD card.  You need to either press the “Flash" button which automatically starts Etcher (if it is installed, if it is not installed then there are more steps), or select from the pull down nest to the "Flash" button to download the image file, ...and then flash it to the SD card with your software of choice.))

Once you have your freshly flashed SD card, install it in the Raspberry Pi:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/install-sd.jpg?raw=true)_SD card in back of the Raspberry Pi_

Power on the device and wait for it to boot up.  The first time the device powers up will take a significant amount of time as it needs to get an initial copy of the WHAQM software.  During this first step you should see the balena splash screen on your device:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/touch_balena_logo_no_keyboard.jpg) _Nice Logo…_

You can also verify that the software is being loaded on the device correctly by going to the balena Cloud dashboard and looking for a new device in the balena fleet you created.  In this example case, there is a device called “autumn-rock” and the “Status” is currently “Updating”:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/Screenshot-updating-device.jpg?raw=true) 

When the initial software has completed the loading process the “Status” will change to “Online” and you can click on the device name to get more detailed information about the device and the software that is running:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/Screenshot-device-running.jpg?raw=true)_…you should see something like this…_

…and you should see the General/Top Screen on your WHAQM device:

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/better-first-boot.jpg?raw=true) _…nothing more to do here!_



### Using the WHAQM software

outline

brief overview of menus
    top
    main summery page
    detailed sensor information
        location measurement details
        measurements by locaiton

review some of the buttons
    time period
    manual refresh
    automatic refresh slection
    view mode - add warning about touchscreen 
### Adding more devices....

outline

currently suppoerted devices
    balenaAIR
    WHAQM

need WHAQM_SENSOR_NAME
need modify mosquitto.conf file in MQTT container with WHAQM_COLLECTOR_URL
for WHAQM devices, point borwser block to WHAQM_COLLECTOR_URL

### Troubleshooting



