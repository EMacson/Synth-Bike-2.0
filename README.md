# Synth-Bike-2.0

## Concept
This is my new and improved synth bike. This was a project where I iterated on my old synth bike design, by tring to impove the embodiment of the bike. The first improvement to embodiment was to make it so a user could actually ride around on the bike,instead of the previous design that required the bike to be connected via USB to a laptop. 

To do this I switched from using am Arduino uno to a Raspberry pi pico w. This is because the Arduino uno does not have a native WiFI component. The bike and laptop now communicate through a socket program connected over a shared local network. The laptop acts as a server, recieving messages from the pico acting as a client. The programming language also changed as the pico runs on micropython, and I wrote the laptop server code in python as I am no longer using supercollider for sound generation. The general communication structure is relatively the same though, with the bike generating values based on user inputs and then sending these values to the laptop which interprets them into sound.

the user input was also modified. Instead of using, flat, capacitive touch sensors, I created three-dimemsional foam buttons. 

## Circuit Schema

## Photos

## Video Explanation and Demo
[![IMAGE ALT TEXT HERE]()](https://youtu.be/bunlOOHyu5c)
[Video](https://youtu.be/bunlOOHyu5c)

## Functionality
The components for this project are
- a Raspberry Pi Pico W

To run the code, import 

## References
### Tutorials Used for the Project


### Image Sources from Video
