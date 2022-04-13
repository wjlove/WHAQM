
 ![The Whole Home Air Quality Monitoring Project](https://github.com/wjlove/WHAQM/blob/main/documentation/images/two-display-sidebyside.jpg?raw=true)

*An extension of the balenAIR project that allows for multiple sensors in various location within your home or any indoor location*

# Whole Home Air Quality Monitoring Project

## Reasoning

I was wondering if the quality of the air in my office was affecting my work and was looking to measure the levels of hazardous gasses while my office door was closed.   There are many products out there that one can purchase that will monitor indoor air quality but as a tinkerer I wanted to build one myself.  After some online research I came across the excellent baleaAIR (https://github.com/balena-io-playground/balena-iaq) project and thought this might be fun to build, so I started constructing one.  

During the process of testing my device I noticed that my measurements were wildly different throughout the day and often in the danger zones while working in my office.  I thought I’d done everything correctly so what was wrong?  As a test I moved my device to another room in my home and what a difference, these measurements were stable and “safe”.  With those results in hand, I went to several other rooms in my home and noticed each one produced results that were slightly different generally and fluctuated during the day.   It is from here I wondered if having a small sensor in each room, monitored by a central location might be useful and thus this project was born.

## New Features

At its core, this project is simply an extension of the great work done on the balenAIR project and adds the following features:

- A standalone balenAIR like device with a touchscreen display
- A centralized balenAIR like device with a touchscreen display
- Ability to collect data from multiple air quality devices
- Ability to display aggregated measurements from multiple devices
- Ability to predict air quality conditions based on previous measurement
 
## Hardware Selection

 There are a number of options when it comes to selecting hardware for the IAQ. Cost, availability and performance are some factors to consider when choosing the parts below.

### Choosing your Pi




This project currently runs on a Raspberry Pi, so you'll need one of the following compatible devices:

- [Pi 3B](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)
- [Pi 3B+](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/)
- [Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

Note: If you plan on having a significant number of remote sensor devices like those from the balenAIR project you should consider using a Pi 4 as the prediction software can be rather compute intensive.

### The Display and Case

There are many options for choosing a case that will house the Raspberry Pi, the touchscreen device and all the sensors or you can make your own.  After some review I settled on the [SmartiPi Touch Pro - Small](https://smarticase.com/products/smartipi-touch-pro) and the original [Raspberry Pi Touch Display](https://www.raspberrypi.com/products/raspberry-pi-touch-display/).  Both are easily available for purchase and well supported.  

![](https://github.com/wjlove/WHAQM/blob/main/documentation/images/case-display.jpg?raw=true)

### Sensors

The sensors evaluate your air and return data that is used to deterime your air quality score. This project, like balenAIR,  supports the three different sensors listed below. You can choose to have one, two, or all three present in your device, depending on your budget and air quality analysis needs.

| Sensor | Detects | Description |  Specifications (approx.) |
| ------------ | ----------- | ----------- | ----------- |
| [PMSA003I](https://www.adafruit.com/product/4632) | Smoke, dust, dirt, pollen particles | laser-scattering type  | 0.3-1.0,1.0-2.5, 2.5-10 Micrometer particles |
| [SCD-40](https://www.adafruit.com/product/5187) | Exhaled breath and burning fossil fuels |  CO2 photoacoustic sensor CO2 (plus temp and humidity)  | 400 - 2000 PPM |
| [SGP-30](https://www.adafruit.com/product/3709) | Gasses emitted by solid and liquid products  |  VOC (and eCO2) Hot-plate MOX sensor | eCO2 400-60,000 ppm, TVOC 0-60,000 ppb |

All of these sensors use the popular I2C protocol to communicate with the Pi and include [Qwiic](https://www.sparkfun.com/qwiic) connectors so you don't need to do any soldering to use these sensors.

### Sensor Carrier Board

### Miscellaneous Items