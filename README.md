# robotics-trajectory-planning
# Robotics Project – Trajectory Planning and Simulation

This project was developed as part of a university course on Robotics. It involves the mathematical modeling, trajectory planning, and simulation of a mobile robot's movement and orientation using cubic polynomials and trapezoidal velocity profiles.

## Authors
- Christodoulou Christos 
- Tsakiris Dimitris  
- Laloutsos Nikolaos 

## Overview

The project focuses on:
- Computing robot orientation using the `atan2` function to face a final point `(xf, yf)`.
- Designing motion trajectories using **cubic polynomials** for both orientation and linear displacement.
- Calculating angular and linear velocities and accelerations with respect to time.
- Creating visual plots to verify constraints and ensure the robot reaches the desired position and orientation.
- Implementing motion in **ROS1**, including verification through simulations.
- Handling discrepancies in simulation outputs across different environments (e.g., local VM vs lab PC).

## Sections

### 1. Motion Planning

- Orientation calculated with:
  - θ(t), θ′(t), θ′′(t) using cubic polynomials
- Linear displacement along the X-axis
  - x(t), x′(t), x′′(t) derived similarly
- Combined rotation and translation to reach desired final position `(5.4, 2.7, 1.54)`

### 2. Joint Space Trajectory

- Joint angles `q1` and `q2` computed from student IDs:
  - q1 = 67.5°, q2 = -45°
- Trajectory planned using **trapezoidal velocity profile**
- Final equations for angular position, velocity, and acceleration were derived and validated

## Tools & Environments
- **Octave** for mathematical computations and plotting
- **ROS1** for robotic simulation
- Issues were encountered in non-native environments (e.g., VMs), affecting real-time simulation accuracy

## Observations
- All kinematic constraints were satisfied.
- Both joints reached their target angles within the specified time.
- Simulation visualizations confirmed theoretical expectations despite some discrepancies in virtual environments.

## License
This project is for educational purposes and is not licensed for commercial use.

