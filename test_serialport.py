import serial
import time

# Configure the serial port
port = 'COM7'  # Update this to the correct port on your system
baudrate = 9600  # Update this to match the baud rate of your device

# Initialize the serial connection
ser = serial.Serial(port, baudrate, timeout=1)


def send_sound_command(command):
    ser.write(command.encode('utf-8'))
    #ser.write(b'\r\n')  # Sending a carriage return and newline if needed by the device
    time.sleep(0.1)  # Slight delay to ensure the command is processed


try:
    while True:
        # Read data from the serial port
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {data}")
            if data == "play sound 1":
                send_sound_command("SOUND1")  # Replace "SOUND1" with the actual command for your device
            elif data == "play sound 2":
                send_sound_command("SOUND2")  # Replace "SOUND2" with the actual command for your device

        # Example of sending a command to the serial device manually
        send_sound_command("SOUND1")
        time.sleep(1)  # Wait for a second before sending the next command

except KeyboardInterrupt:
    print("Program interrupted by user. Closing serial port.")
finally:
    # Close the serial port
    ser.close()
