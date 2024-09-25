# LED Brightness Control Using OpenCV and Arduino

This project demonstrates how to control the brightness of an LED connected to an Arduino based on the distance between the index finger and thumb using hand gesture recognition in OpenCV. The project uses Python, OpenCV for hand detection, and the pyFirmata library to interface with the Arduino Uno for controlling the LED brightness.


## Components
* Arduino Uno
* LED
* 220Ω Resistor
* Jumper Wires
* Breadboard
* Python (with OpenCV and pyFirmata libraries)

## Features
* Hand Gesture Control: Detects the distance between the index finger and thumb to control the LED brightness.
  
* Real-Time Adjustment: The brightness changes dynamically based on finger movement in front of the camera.
  
* Arduino Integration: Uses the pyFirmata library to communicate between Python and Arduino for controlling the LED.


## Circuit Diagram
1. Connect the positive terminal of the LED to Pin 9 of the Arduino through a 220Ω resistor.
2. Connect the negative terminal of the LED to the GND pin of the Arduino.

### Pin Connections:
* LED: Positive to Pin 9, Negative to GND

![image](https://github.com/user-attachments/assets/2c16c6d9-448c-4584-8d61-e9095bf247ca)

## Prerequisites

### Arduino Setup

Before running the Python script, ensure your Arduino is ready for communication with the pyFirmata library.

1. Upload the StandardFirmata sketch to your Arduino Uno:
     * Open the Arduino IDE.
     * Go to File > Examples > Firmata > StandardFirmata.
     * Select your Arduino board and port.
     * Click Upload.
  
 ###  Python Libraries
 You’ll need the following Python libraries:
   * opencv-python
   * mediapipe
   * pyFirmata

You can install the required libraries using pip:
```
pip install opencv-python mediapipe pyfirmata

```
     
## How It Works

1. Hand Detection: The program uses the MediaPipe library (via OpenCV) to detect the user's hand and identify the position of the index finger and thumb.
2. Distance Calculation: The distance between the tip of the index finger and the thumb is calculated. This distance is mapped to a value between 0 and 255, which represents the LED brightness.
3. Brightness Control: The pyFirmata library sends the mapped brightness value to the Arduino, which adjusts the LED brightness accordingly.

## Future Enhancements

* Add a graphical user interface (GUI) to display more information and control parameters.
* Implement gesture-based control for multiple devices, like controlling multiple LEDs or other actuators.
* Add error handling for connection issues with the Arduino.

   ## Feel free to fork the repository and contribute! If you like the project, consider giving it a ⭐ on GitHub!


