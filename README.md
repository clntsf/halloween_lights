# Poetry CS work

Contained in this repository are several projects created over the span of Poetry 2021-2022 in Computer Science Class. A list of them and descriptions will be included in this file.


 - [Project 1: Halloween Lights](#project-1-halloween-lights)
    - [1.1: Initial Ideas](#11-initial-ideas)
    - [1.2: Required Objects](#12-required-objects)
    - [1.3: Online Resources](#13-online-resources)
    - [1.3: Writing the Code](#14-writing-the-code)

___

## Project 1: Halloween Lights

###    1.1 Initial Ideas

1. A device to scare passers-by, record their voices, and then play them back to the next person.</p>
    > _This idea was considered but put aside due to considerations of the complexity of the required setup and the necessity of a device capable of both recording and playing back sound._

2. A device which detects vibrations and turns on a strip of appropriately-colored LED lights, maybe playing a pre-recorded sound clip.
    > _This idea was chosen due to its relatively low hardware requirements, its simple yet rewarding concept, and the general interest of the group._

It should be noted that we revised our input to sound as opposed to vibration, as the microbit has a microphone embedded within it and native support for sound input

###     1.2 Required Objects

 - BBC Microbit
    > _This will play the role of both sound input and output, as well as containing the script (written in python) to control the artefact's behaviour_
 - LED Strip
    > _For displaying colored lights when a sound is detected_
 - Connecting board
    > _used to connect the Microbit to the LED Strip, allowing it to send signals and interact with the LEDs on it_

###     1.3 Online Resources

 - [microbit.org - Python sound input documentation](https://microbit.org/get-started/user-guide/python/#microphone)
 - [readthedocs - NeoPixel Documentation](https://microbit-micropython.readthedocs.io/en/v1.0.1/neopixel.html)
 - [w3schools - HTML color picker](https://www.w3schools.com/colors/colors_picker.asp)

###     1.4 Writing the Code

1. Firstly, we delegated roles in the group, which were as follows:

    - I (Colin) would be focusing on the LED strip's output
    - Javkhlan would focus on sound input/output using the microbit's microphone and speakers
    - Faouzi would focus on the media required for the project (LED color/transition, outputted sound, etc.)

2. Then we tried to determine how we wanted the LED strip to act as a part of the completed artefact. A brief summary of the  properties we decided to design is as follows:

    - The LED strip will run on a decay timer, meaning that when activated it will remain "on" so long as it is stimulated frequently enough. A summary of this behaviour is in [decay_timer.py](/halloween_lights/decay_timer.py).

    - The LED strip (when activated) will change colors along a gradient between two shades of orange (#5A1E00 and #1E0A00) along a sine function (for a smooth and 'breathing' transition)

3. We then split off and independently worked on our own sections, Faouzi and I consulting together on the operation of the LED strip using the neopixel module, and Javkhlan researching and developing a sound/vibration detection and output mechanism supported by the native components of the microbit.

