# RoboticArm
Designed a 3 Degrees of Freedom (DOF) robotic arm controlled by an ESP32 microcontroller. The robotic arm will have a stepper motor for base rotation and two servos for arm movement, allowing it to perform tasks such as picking, placing, and other manipulations.

Components:
ESP32 Microcontroller:

Acts as the brain of the robotic arm, processing commands and controlling the motors.
Provides Wi-Fi/Bluetooth capabilities for remote control and programming.
Stepper Motor:

Controls the base rotation of the robotic arm.
Provides precise control over the arm's horizontal movement.
Servos:

Two servos control the vertical movements of the arm.
The first servo moves the lower arm (shoulder joint), and the second servo moves the upper arm (elbow joint).
Power Supply:

Provides the necessary power to the ESP32, stepper motor, and servos.
Structural Components:

Arm segments, base, and joints made of materials such as aluminum, plastic, or 3D-printed parts.
Methodology:
1. Hardware Setup:
Assemble the robotic arm using the structural components, attaching the stepper motor at the base and the servos at the designated joints.
Connect the stepper motor and servos to the ESP32 microcontroller using appropriate drivers (e.g., A4988 stepper driver for the stepper motor).
Ensure all connections are secure and the power supply is adequate for all components.
2. ESP32 Programming:
Use the Arduino IDE or ESP-IDF to write the control code for the ESP32.
Implement libraries for controlling the stepper motor and servos.
Develop functions for moving the robotic arm to specific positions based on input commands.
3. Control Algorithms:
Implement inverse kinematics to calculate the necessary angles for the servos and the stepper motor position to achieve the desired end-effector position.
Develop a user interface (e.g., web interface or mobile app) for remote control and command input.
