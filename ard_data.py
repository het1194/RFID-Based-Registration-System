import serial

def scanning_card():
    try:
        ser = serial.Serial("COM9", 9600)
        while True:
            data = ser.readline().strip().decode()
            if data:  # Check if data is not empty
                print(data)
                return data  # Return the UID once it's read
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
    except KeyboardInterrupt:
        print("Program terminated.")
