# Synth-Bike-2.0

## Concept
This is my new and improved synth bike. This was a project where I iterated on my old synth bike design, by tring to impove the embodiment of the bike. The first improvement to embodiment was to make it so a user could actually ride around on the bike,instead of the previous design that required the bike to be connected via USB to a laptop. 

To do this I switched from using am Arduino uno to a Raspberry pi pico w. This is because the Arduino uno does not have a native WiFI component. The bike and laptop now communicate through a socket program connected over a shared local network. The laptop acts as a server, recieving messages from the pico acting as a client. The programming language also changed as the pico runs on micropython, and I wrote the laptop server code in python as I am no longer using supercollider for sound generation. The general communication structure is relatively the same though, with the bike generating values based on user inputs and then sending these values to the laptop which interprets them into sound.

The user input was also modified. Instead of using, flat, capacitive touch sensors, I created three-dimemsional foam buttons. Feedback from my previous deisgn mentioned that the flat keys maybe hard to locate while riding around, these new keys should help this. I also added an additional key, making the total key count 5. The bike still takes the back tire speed as input, however it affects the sound volume instead of the sound pitch, I will explain why a bit later. When the user presses some keys the pico will record each press as a note on the C major scale. Since there are only 5 keys, the available notes are middle c, d, e, f, and g. The pico will send this record in a message with the following form

  a-wheel speed-note 1-note 2-...-b

This message format made it easier for the laptop program to deliminate each of the note values.

As mentioned I am no longer using supercollider, instead I am using the scamp library for audio generation. This library lets me create instruments as python variables, where I can play a note or chord on the instrument by calling play_chord(). play_chprd() takes as input a list of notes to play, the sound volume, and the note length. The note list is easily extracted from the message sent from the pico. The volume is a value between 0.0 and 1.0, with 1.0 being th maximum. This is where the new wheel speed mapping comes in as play_chord() does not have any default parameters for changiong the pitch. In this new mapping we have the following ranges of wheel RPM (rotations per minute) to volume level,
- 0.4 for under 60rpm
- 0.6 for 60 to 80 rpm
- 0.8 for 80 to 120rpm
- 1.0 for over 120rpm

Finally, I added glow sticks as I thought they would improve the aesthetic of the bike. I could see people riding this bike around music festivals or events happening at night. Someone at the live demo said they could see people riding the bike around Buring Man, and I think that would be the prefect setting for this bike.

## Circuit Schema

## Photos
<img src="./images/IMG_3854.jpg" alt="" />
<img src="./images/IMG_3857.jpg" alt="" />
<img src="./images/IMG_3887.jpg" alt="" />

<img src="./images/IMG_3888.jpg" alt="" />
<img src="./images/IMG_3889.jpg" alt="" />
<img src="./images/IMG_3895.jpg" alt="" />
<img src="./images/keys.jpg" alt="" />

<img src="./images/IMG_3880.jpg" alt="" />
<img src="./images/IMG_3881.jpg" alt="" />
<img src="./images/IMG_3882.jpg" alt="" />
<img src="./images/IMG_3883.jpg" alt="" />

## Video Explanation and Demo
[![IMAGE ALT TEXT HERE](./images/title.png)](https://youtu.be/bunlOOHyu5c)
[Video](https://youtu.be/bunlOOHyu5c)

## Functionality
The components for this project are
- a Raspberry Pi Pico W
- 5 push buttons
- a photoresistor
- a 10k ohm resistor
- jumper wires
- a bike
- a laptop

To run the code, import client.mpy to the pico. You will need to create a config file that contains youe WiFi SSID and password. Next, begin running server.py, it should print out the server's IP address, you will need to make sure this aligns with the IP address the pico is tryong to connect to. From this you can begin running client.mpy on the pico and the two devices should begin to connect. Once connected the terminal running server.py will print the notes in the messages it recieves from the pico, and will print blanks if it has not reieved a note yet. Once a note is recieved the laptop will play the note over your speaker of choice.

## References
### Tutorials Used for the Project


### Image Sources from Video
