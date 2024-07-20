# NeoSlider4XPlane
NeoSlider4XPlane transforms your flight simulation experience by integrating the Adafruit NeoSlider into X-Plane, allowing for precise manipulation of aircraft control systems such as the rudder or brake controls with visually engaging, customizable LED feedback. Customization of the LED feedback requires modifications to the `code.py` file, which necessitates a basic understanding of Python programming.

## Prerequisites
- X-Plane 11 or later installed
- An Adafruit NeoSlider I2C QT Slide Potentiometer with 4 NeoPixels, programmed with CircuitPython, including the following libraries:
  - `adafruit_hid` for HID device communication
  - `neopixel` for controlling NeoPixels
  - `touchio` for touch input
  - `analogio` for analog input
  - `usb_hid` for USB HID support

These libraries can be downloaded from the [CircuitPython Library Bundle](https://circuitpython.org/libraries).

Learn more about the [Adafruit NeoSlider](https://learn.adafruit.com/adafruit-neoslider/overview)

# Repository Contents

This repository includes essential files for operating the Adafruit NeoSlider: `boot.py` and `code.py`.

- **boot.py**: This file is executed only once when the device powers up or is reset. It's crucial for setting up the device's environment before any other code runs. In the context of NeoSlider4XPlane, `boot.py` configures the USB HID (Human Interface Device) profile necessary for the NeoSlider to function as a gamepad. This setup includes defining a custom gamepad report descriptor that specifies the data format the device will send to the computer. This configuration allows the NeoSlider to communicate with X-Plane (or any other software that accepts gamepad input), enabling it to send button presses and slider positions as gamepad inputs.

- **code.py**: This is the main script file that CircuitPython runs after `boot.py`. It contains the core functionality of the NeoSlider4XPlane project. The script continuously reads the state of a touch sensor and the position of a slider, translating these inputs into gamepad reports sent over USB. Additionally, it dynamically adjusts the color of onboard NeoPixels based on the slider's position, providing visual feedback to the user. This file effectively bridges the physical inputs from the NeoSlider to X-Plane, allowing for precise control of aircraft systems like the speed brake, and enhances the user experience with visual feedback through LEDs.

## Installation

Follow these steps to install the files on your Adafruit NeoSlider:

1. **Clone the repository**: First, clone this repository to your local machine using `git clone`.

    ```bash
    git clone https://github.com/1090MHz/NeoSlider4XPlane
    ```

2. **Install Adafruit's CircuitPython**: Make sure you have Adafruit's CircuitPython installed on your NeoSlider. If not, follow the instructions at the Adafruit website.

3. **Copy the files**: Connect your NeoSlider to your computer. It should show up as a flash drive named `CIRCUITPY`. Copy the `boot.py` and `code.py` files from the cloned repository to the `CIRCUITPY` drive.

4. **Reset the board**: After the files are copied, press the reset button on your NeoSlider. The board will automatically pick up the new files and start running your code.

## Usage

Once the `boot.py` and `code.py` files are installed, the NeoSlider should start running the code automatically whenever it is powered on.

## Device Recognition in X-Plane

Once the Adafruit NeoSlider is configured with the `boot.py` and `code.py` files and connected to your computer, X-Plane will recognize it as a custom gamepad device. Here's what to expect and how to configure it within X-Plane:

### How X-Plane Recognizes the Device

- **Custom Gamepad Device**: The NeoSlider, with its configured USB HID profile, will appear in X-Plane's joystick and equipment settings as a custom gamepad. It will be listed by its device name, which is determined by the USB HID configuration in `boot.py`.

### Configuring the Device in X-Plane

1. **Accessing Joystick Settings**: Open X-Plane, navigate to the settings menu, and select the "Joystick" section. Here, you will find a list of connected devices, including the NeoSlider.

2. **Assigning Functions**: Select the NeoSlider from the list to assign functions to its buttons and slider. X-Plane allows for a wide range of controls to be mapped, from simple button presses to complex multi-axis movements.

3. **Calibration**: If necessary, you can calibrate the slider to ensure accurate input detection within X-Plane. This step ensures that the full range of the slider is utilized, from minimum to maximum positions.

4. **Testing**: After configuration, it's recommended to test the NeoSlider within a flight scenario to ensure all mappings are responding as expected. This can be done in a controlled environment within X-Plane, such as on the runway or in a simple flight.

### Tips for Optimal Configuration

- **Sensitivity Settings**: Adjust the sensitivity settings for the slider within X-Plane to match your preferred control feel. Some users may prefer a more responsive setup, while others may opt for a smoother, less sensitive control.

- **Multiple Devices**: If using multiple input devices, ensure that each device is correctly identified and configured within X-Plane to avoid conflicts or misassignments.

By following these steps, you can seamlessly integrate the Adafruit NeoSlider into your X-Plane setup, enhancing your flight simulation experience with precise control over aircraft systems and immersive visual feedback.