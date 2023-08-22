# The_distance_between_two_fingers
# Hand Distance Detector

A simple Python application that detects hands using a webcam and calculates the distance between specific landmarks on the detected hand.

## Overview

The program captures live video feed from the default camera, detects hands using the `handTrackingModule`, and computes the distance between landmarks 4 and 8 on the detected hand. The calculated distance (referred to as "volume" in the code) is then displayed on the live feed at a position between the two landmarks.

## Prerequisites

- Python 3
- Mediapip
- OpenCV (`cv2`)
- `handTrackingModule` (Ensure this module is properly accessible)

## How to Run

1. Ensure you have all the prerequisites installed and set up.
2. Clone the repository and navigate to the directory containing the script.
3. Run the The_distance_between_two_fingers,py 
4. A window displaying the video feed will pop up. Show your hand to the camera, and the program will display the distance between landmarks 4 and 8.
5. To exit, press the 'q' key.

## Author

**Arman Neyestani**
- GitHub: [https://github.com/A8neyestani](https://github.com/A8neyestani)
- Email: A8neyestani@protonmail.com

## License

This project is open source. Feel free to use, modify, and distribute the code as you see fit. However, it's always a good practice to give credit where it's due.

## Acknowledgements

Special thanks to the developers of the `handTrackingModule` and the OpenCV community.

