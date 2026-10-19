# Mechatronics, robotics and embedded engineering

## Foundation
Math/physics, circuit analysis, sensors, ADC/DAC, interrupts, MCU memory, timers, UART/I2C/SPI/CAN, motor drives, PID and state-space control, RTOS scheduling, robotics kinematics, embedded C/C++, firmware testing and functional safety.

## Safety first
Separate simulation from physical actuation. For energized circuits, high voltage, high-speed machinery or mobile robots require physical supervision, guards, E-stop, current limits and safe test facilities. Never assume a text-only plan is safe for untested hardware.

## Experiment template
Schematic and pinout -> power budget -> hazard analysis -> test bench -> instrument calibration -> expected waveform/telemetry -> firmware -> measurement -> failure injection at safe energy -> revision and regression.

## Micro / nano
Interrupt jitter, task priority inversion, bus contention, metastability, ADC quantization, sensor aliasing, numerical stability, PWM frequency, DMA ownership, stack usage, EMI, grounding, race conditions and actuator saturation.

## Learn with simulation
Start with SPICE and ROS 2 simulation where appropriate; test low-voltage microcontroller labs before physical actuators.
