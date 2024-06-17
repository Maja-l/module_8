import serial
import winsound  # For playing sound on Windows

# For other platforms, use a different method to play sound

# Configure the serial port
port = 'COM7'  # Update this to the correct port on your system (e.g., 'COM3' on Windows)
baudrate = 9600  # Update this to match the baud rate of your device

# Initialize the serial connection
ser = serial.Serial(port, baudrate, timeout=1)


def play_sound():
    # Example of playing a sound on Windows using winsound
    winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 milliseconds


try:
    while True:
        # Read data from the serial port
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {data}")
            play_sound()

except KeyboardInterrupt:
    print("Program interrupted by user. Closing serial port.")
finally:
    # Close the serial port
    ser.close()
