
 ![The Whole Home Air Quality Monitoring Project](https://github.com/wjlove/WHAQM/blob/main/documentation/images/two-display-v2.jpg?raw=true)

**An extension of the balenAIR project that allows for multiple sensors in various location within your home or any indoor location**

#Whole Home Air Quality Monitoring Project

## Reasoning

I was wondering if the quality of the air in my office was affecting my work and was looking to measure the levels of hazardous gasses while my office door was closed.   There are many products out there that one can purchase that will monitor indoor air quality but as a tinkerer I wanted to build one myself.  After some online research I came across the excellent baleaAIR (https://github.com/balena-io-playground/balena-iaq) project and thought this might be fun to build so I started constructing one.  

During the process of testing my device I noticed that my measurements were wildly different throughout the day and often in the danger zones while working in my office.  I thought I’d done everything correctly so what was wrong?  As a test I moved my device to another room in my home and what a difference, these measurements were stable and “safe”.  With those results in hand, I went to several other rooms in my home and noticed each one produced results that were slightly different generally and fluctuated during the day.   It is from here I wondered if having a small sensor in each room, monitored by a central location might be useful and thus this project was born.

## New Features

At its core, this project is simply an extension of the great work done on the balenAIR project and adds the following features:

- A standalone balenAIR like device with a touchscreen display
- A centralized balenAIR like device with a touchscreen display
- Ability to collect data from multiple air quality devices
- Ability to display aggregated measurements from multiple devices
- Ability to predict air quality conditions based on previous measurement
 