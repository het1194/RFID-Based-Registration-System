# RFID-Based Attendance System

This project implements an RFID-based attendance system for universities. Students can register their details and tap their RFID cards on a sensor to mark their attendance.
### NOTE: For in-depth detail of the working of the streamlit UI, please refer to the project documentation attached. 

## Features

* User registration with name, phone number, and registration number.
* RFID card scanning for attendance/registration marking.
* Data storage of registered students and attendance records in an Excel spreadsheet ("Data/student_data.xlsx").
* User feedback with success/failure messages for registration/attendance.

## Hardware Requirements

* Arduino Uno or compatible microcontroller board
* RFID reader module (e.g., MFRC-522)
* RFID tags for students

## Software Requirements

* Python 3.x
* Streamlit library (`pip install streamlit`)
* openpyxl library (`pip install openpyxl`)
* pyserial library (`pip install pyserial`)

## Running the Project

1. **Installation:**
   * Ensure you have the necessary hardware and software installed.

2. **Hardware Setup:**
   * Connect the RFID reader module to your Arduino board according to its specific wiring instructions.
   * Connect the Arduino board to your computer via USB cable.

3. **Arduino Code:**
   * Upload the provide Arduino_IDE code for reading RFID tags to your Arduino board. 

4. **Run the Application:**
   * Open a terminal or command prompt and navigate to the project directory.
   * Run the application using the following command:
   
     ```bash
     streamlit run home.py
     ```
   * A web interface will launch in your default web browser.
