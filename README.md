# Assistive Smart Device for Visually Impaired  
**Capstone Project – University of Washington ECE Department**

---

## Overview

This project presents a wearable assistive device designed to enhance navigation and environmental awareness for visually impaired users. Integrating real-time navigation and computer vision, the device provides spoken guidance and object detection through local processing, supporting independent and safe mobility in both indoor and outdoor environments.
### Watch the Demo!
Watch a video of the device working in action at this youtube link: 

(https://youtube.com/shorts/SWpah7KVuFU?feature=share)

<img src="https://github.com/user-attachments/assets/99a87804-ff0f-48a1-992f-74e050e4d4a7" alt="IMG_1050" width="250">
<img src="https://github.com/user-attachments/assets/9228e252-7659-4d01-a083-9e61c72315ea" alt="IMG_1048" width="250">

---


## Table of Contents

- [Team](#team)
- [Project Goals](#project-goals)
- [System Architecture](#system-architecture)
- [Key Features](#key-features)
- [Hardware Components](#hardware-components)
- [Software Components](#software-components)
- [Engineering Constraints & Standards](#engineering-constraints--standards)
- [Development & Testing](#development--testing)
- [Experimental Outcomes](#experimental-outcomes)
- [Impact & Future Work](#impact--future-work)
- [Acknowledgements & Licensing](#acknowledgements--licensing)

---

## Team

| Name                        | Role                                         |
|-----------------------------|----------------------------------------------|
| Kyshawn Savone-Warren       | Project Manager, Depth Sensing & Obstacle Avoidance |
| Carlos Alberto Morelos Escalera | Object Detection, STM32 Hardware Integration |
| Luke Liu                    | Computer Vision, AI Optimization             |
| Santos Zaid                 | STM32 Hardware Integration, System Communication |
| Nathan Cannell              | Navigation System, Audio Feedback            |

---

## Project Goals

- **Enable safe navigation** for visually impaired users via real-time GPS guidance and obstacle avoidance.
- **Detect and identify key objects** (e.g., street signs, crosswalks, vehicles, pedestrians) using computer vision (YOLOv11).
- **Deliver real-time audio feedback** for navigation and environmental awareness.
- **Operate as a standalone, wearable device** with all computation performed locally for privacy and efficiency.

---

## System Architecture

- **Wearable Helmet Design:** Sensors and cameras are mounted on a helmet frame; processing units are housed on top.
- **Processing Units:** STM32 microcontroller (sensor integration, audio output) and Raspberry Pi (object detection, navigation).
- **Sensor Suite:** Arducam Time-of-Flight (ToF) camera for depth sensing, USB RGB camera for object detection, GPS module for navigation.
- **Audio Output:** Speaker and amplifier for real-time voice feedback.
- **Power:** Portable battery pack for all-day use.

**Data Flow Diagram:**

- Cameras and GPS feed data to Raspberry Pi.
- Raspberry Pi runs navigation and object detection algorithms.
- STM32 handles sensor integration and audio output.
- Communication between Raspberry Pi and STM32 via USB/UART.
- Audio cues delivered to the user in real time.

---

## Key Features

- **Obstacle Avoidance:** ToF camera detects obstacles (2–4m range) and provides spatial alerts.
- **Navigation:** GPS-based turn-by-turn guidance with spoken instructions.
- **Object Detection:** YOLOv11 model identifies street signs, crosswalks, vehicles, and pedestrians.
- **Audio Feedback:** Real-time speech output for navigation and object alerts.
- **Local Processing:** All computation is performed on-device, ensuring privacy and low latency.
- **Indoor/Outdoor Use:** Optimized for urban navigation and large indoor spaces.

---

## Hardware Components

| Component           | Function                     | Cost     |
|---------------------|-----------------------------|----------|
| Arducam ToF Camera  | Depth/Obstacle Sensing      | $109.98  |
| USB Camera          | Object Detection            | $15.99   |
| Audio Amplifier     | Audio Output                | $5.19    |
| Speaker             | Audio Output                | N/A*     |
| GPS Module          | Navigation                  | $12.99   |
| Buck Converter      | Power Regulation            | $9.99    |
| Power Supply        | Battery                     | N/A*     |

*Items marked N/A were already available in lab supply.

---

## Software Components

- **YOLOv11:** Real-time object detection (trained on custom and public datasets).
- **OSMnx:** Offline route planning and navigation.
- **Custom Depth Sensing Scripts:** For obstacle detection and spatial cueing.
- **Audio Subsystem:** Text-to-speech and audio output via STM32 and CS43L22 codec.
- **Inter-device Communication:** USB/UART protocols for data exchange between Raspberry Pi and STM32.

---

## Engineering Constraints & Standards

- **Processing Power:** Embedded hardware (Raspberry Pi, STM32) with optimized models for real-time performance.
- **Power Consumption:** Battery-powered for portability; power management is critical.
- **Environmental Factors:** IP54 water/dust resistance; operates in varied lighting and weather.
- **Safety:** Compliance with ISO 13482:2014 for assistive devices and ANSI S3.5-1997 for speech intelligibility.
- **Wireless Communication:** IEEE 802.11 for debugging and logging during development.

---

## Development & Testing

**Subsystems:**
- *Navigation*: GPS integration, OSMnx route planning, turn-by-turn audio cues.
- *Object Avoidance*: ToF camera integration, spatial analysis (left/right detection), real-time alerts.
- *Computer Vision*: YOLOv11 training and optimization, real-time inference on Raspberry Pi.
- *Audio*: STM32 audio output via CS43L22 codec, text-to-speech, latency testing.

**Integration:**
- Synchronized data flow between navigation, object detection, and audio feedback.
- Local processing; no cloud reliance for privacy.
- Iterative testing in real-world urban and indoor environments, including low-light scenarios.

---

## Experimental Outcomes

- **Object Detection:** Achieved >70% accuracy for key street signs and objects in optimal conditions.
- **Obstacle Avoidance:** Reliable detection within 2–4m; two-part spatial analysis (left/right) provided effective alerts.
- **Navigation:** Turn-by-turn guidance functional; GPS accuracy limited indoors.
- **Audio Feedback:** Real-time spoken cues with <500ms latency.
- **System Integration:** All subsystems operated cohesively in prototype testing, with successful real-world trials.

---

## Impact & Future Work

- **Social Impact:** Promotes independence and inclusion for visually impaired individuals in urban and campus environments.
- **Commercial Potential:** Viable for further development and commercialization, especially in collaboration with industry partners.
- **Future Improvements:**
  - Enhance processing efficiency and battery life.
  - Refine AI models for improved accuracy in challenging conditions.
  - Integrate with existing navigation apps.
  - Conduct broader user testing and collect feedback for iterative design.

---

## Acknowledgements & Licensing

Special thanks to Professor Hussein, the ECE Department, and the UW teaching staff for their support and funding.

**Licensing:**  
This project uses open-source components (YOLOv11, OSMnx, Arducam ToF API) under their respective licenses. All original hardware, software, and documentation are © the project team. For any use or reproduction, proper attribution is required.

---

**Contact:**  
For questions or collaboration, please contact the project team via the UW ECE Department.

---
