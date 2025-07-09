 #  Smart Security System

A smart and affordable door lock solution that combines **password-based access**, **Bluetooth control**, and **real-time camera surveillance** using Arduino UNO, ESP32-CAM, and Python Flask.

---

##  Project Overview

This project demonstrates a multi-layered smart security system for homes, labs, or offices. It enables:

-  **Keypad-based Password Entry**
-  **Image capture on wrong attempts**
-  **Mobile App Bluetooth Unlock**
-  **Email alerts with captured images**

---

##  Components Used

| Component         | Quantity |
|-------------------|----------|
| Arduino UNO       | 1        |
| ESP32-CAM         | 1        |
| 4x4 Keypad        | 1        |
| HC-05 Bluetooth   | 1        |
| Jumper Wires      | ~18      |
| Breadboard        | 1        |
| 330Ω Resistors    | 2        |
| LEDs (Red & Green)| 2        |
| DC Adapter (12V)  | 1        |

---

##  Software & Tools

- **Arduino IDE** (for coding Arduino & ESP32)
- **Python 3** with:
  - `Flask`
  - `NumPy`
  - `Pillow`
  - `smtplib` (for email)
- **Mobile Bluetooth App** (any serial terminal or custom app)

---

##  Working Logic

1. User enters a 4-digit code on the 4x4 keypad.
2. If the code is correct:
   - Green LED turns ON.
   - Door unlock signal (optional) is triggered.
3. If the code is incorrect:
   - Red LED blinks.
   - ESP32-CAM captures an image.
   - Python Flask server sends image to preconfigured email.
4. As an alternative, the door can be unlocked via **Bluetooth command** from a mobile app.

---

##  Circuit Connections (Summary)

### Arduino UNO ↔ HC-05 Bluetooth
| HC-05 Pin | Arduino Pin |
|-----------|-------------|
| VCC       | 5V          |
| GND       | GND         |
| TXD       | D0 (RX)     |
| RXD       | D1 (TX)     |

### Arduino UNO ↔ ESP32-CAM
| ESP32-CAM Pin | Arduino Pin |
|---------------|-------------|
| GPIO 13       | D7          |
| GND           | GND         |
| 5V            | 5V          |

### Arduino UNO ↔ Keypad
- R1–R4 → D2, D3, D4, D5
- C1–C4 → D6, D10, D11, D12

### LEDs
- Green LED → D9  
- Red LED → D8

---

##  Setup Instructions

### 1. Upload Arduino Code
- Upload keypad and Bluetooth logic to Arduino UNO.

### 2. Upload ESP32-CAM Code
- Program the ESP32-CAM to capture and stream images on receiving a signal from GPIO 13.

### 3. Run Python Flask Server
- Use the provided `flask_server.py` to:
  - Receive image from ESP32
  - Convert it to JPEG
  - Email it to the user

### 4. Power the System
- Use a 12V DC Adapter to power Arduino UNO via the barrel jack.

### 5. Mobile App
- Connect your phone to **HC-05** using a Bluetooth terminal app and send unlock commands.

---

##  Email Setup Notes

Ensure to:
- Enable **"Less Secure Apps"** (or use App Passwords if 2FA is on).
- Replace `sender_email`, `receiver_email`, and `password` in Python code with your credentials.

---

## Images 

![image](https://github.com/user-attachments/assets/6b9c84e8-04e4-4425-948d-8c17c6434205)
![image](https://github.com/user-attachments/assets/bebb63d2-d52b-4dba-a882-0ec3f727fd5a)
![image](https://github.com/user-attachments/assets/867e6abd-1f66-4e80-ba92-38ac8bfa3a63)


##  Future Scope

- Face recognition via ESP32-CAM
- Mobile App GUI
- OTP/email-based remote unlock
- Cloud sync for access logs
- Integration with IoT platforms like Firebase

---


## Project Report
[securitySystemReport (3).pdf](https://github.com/user-attachments/files/21148484/securitySystemReport.3.pdf)

---
## Developed By 
- [**Md Ayman Siddique**](https://github.com/aymanthegod)
- [**Subhrajit Saha**](https://github.com/subhoxsaha)
- [**Souvik Pal**](https://github.com/souvikpal7)

---

## Under Mentorship of 
**Deep Rudra**

##  Developed Under
This project was developed under the guidance and mentorship of **KGEC-Robotics Society**,
