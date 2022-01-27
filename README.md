# Halloween Lights ALT-4 Project

## Table of Contents
- [1.1: Initial Ideas](#11-initial-ideas)
- [1.2: Required Objects](#12-required-objects)
- [1.3: Online Resources](#13-online-resources)
- [1.4: Writing the Code](#14-writing-the-code)
- [1.5: Conclusions](#15-conclusions)

___

###    1.1 Initial Ideas

1. A device to scare passers-by, record their voices, and then play them back to the next person.
    > _This idea was considered but put aside due to considerations of the complexity of the required setup and the necessity of a device capable of both recording and playing back sound._

2. A device which detects vibrations and turns on a strip of appropriately-colored LED lights, maybe playing a pre-recorded sound clip.
    > _This idea was chosen due to its relatively low hardware requirements, its simple yet rewarding concept, and the general interest of the group._

It should be noted that we revised our input to sound as opposed to vibration, as the microbit has a microphone embedded within it and native support for sound input.

###     1.2 Required Objects

 - BBC Microbit
    > _This will play the role of both sound input and output, as well as containing the script (written in python) to control the artefact's behaviour_
 - LED Strip
    > _For displaying colored lights when a sound is detected_
 - Connecting board
    > _used to connect the Microbit to the LED Strip, allowing it to send signals and interact with the LEDs on it_
 - Battery pack
    > _used to power the artefact to allow sustained use without maintenance_

###     1.3 Online Resources

 - [microbit.org - Python sound input documentation](https://microbit.org/get-started/user-guide/python/#microphone)
 - [readthedocs - NeoPixel Documentation](https://microbit-micropython.readthedocs.io/en/v1.0.1/neopixel.html)
 - [w3schools - HTML color picker](https://www.w3schools.com/colors/colors_picker.asp)

###     1.4 Writing the Code

1. Firstly, we delegated roles in the group, which were as follows:

    - I (Colin) would be focusing on the LED strip's output and the artefact's decay timer mechanism
    - Javkhlan would focus on sound input/output using the microbit's microphone and speakers
    - Faouzi would focus on the media required for the project (LED color/transition, outputted sound, etc.)

2. Then we tried to determine how we wanted the LED strip to act as a part of the completed artefact. A brief summary of the  properties we decided to design is as follows:

    - The LED strip will run on a decay timer, meaning that when activated it will remain "on" so long as it is stimulated frequently enough. A summary of this behaviour is in [decay_timer.py](/src/decay_timer.py).

    - The LED strip (when activated) will change colors along a gradient between two shades of orange (#5A1E00 and #1E0A00) along a sine function (for a smooth and 'breathing' transition).

        > NOTE (Faouzi): _The color schematics used needed to radiate the theme of halloween. The colors we decided on using were colors associated with the holiday, and thus the color we decided on using was Orange. The colors selected would fluctuate from dark to light Orange._

        > _An alternative approach to coloring the LEDs was originally preferred in which there was a single base color and the change was implemented by sampling from a sinewave fitted to a minimum and maximum scale factor and multiplying the RGB by that scale factor. For reasons mostly involving the microbit's low RGB fidelity this idea was scrapped, but a proof-of-concept [program](/src/sineSampler.py) which outputs an [image](/src/materials/color_cycles.png) showing the resulting strip colors was left in this repository for posterity._

3. We then split off and independently worked on our own sections, Faouzi and I consulting together on the operation of the LED strip using the neopixel module, and Javkhlan researching and developing a sound/vibration detection and output mechanism supported by the native components of the microbit.

 - In researching sound output, however, we found that due to the nature of microbit's native music output (it must play the entire sound before moving on to the next line) and the high TPS required for the operation of the light gradient it was impossible to combine the two using a single microbit. As such we settled for a solely lights-based design and scrapped the idea of having music output.

4. After having written several prototype files (see the ["src"](/src) folder) we combined them into a complete [script](/src/main.py) to control the artefact, and tested it to make sure it exhibited the behaviour we wanted.

###     1.5 Conclusions

 - In the process of designing an artefact certain limitations will be encountered based on the hardware and software used, and the responsibility of the developer is to overcome these limitations either by changing the components causing the limitations or by removing the affected features entirely. In some cases the former is possible, but in others, not.

 - When working in a group it is necessary to properly delegate roles between members in order to efficiently complete the task at hand and to maximise the productivity of each person. At the same time, strong communication must be maintained between members of the group in order to allow their individual parts to combine and function seamlessly
 
 - As a group we were incredibly efficient with how we spent the delegated time to the project. We had the roles delegated within the first 10 minutes of the first class. We spent all given class time on our project and when there was any free time we worked on our python skills and coding.

 - Although limited by the resources available to us in this project, the effective use and excecution of available recources is essential to maximise productivity and minimise waste.

___
