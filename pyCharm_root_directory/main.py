from serial import Serial
from serial.tools import list_ports
from pynput.keyboard import Key, Controller
import time

# Initialize Keyboard
keyboard = Controller()

# --- Auto-detect the HC-05 Bluetooth serial port ---
ports = list_ports.comports()
bt_port = None
for port in ports:
    print(f"Found port: {port.device} - {port.description}")  # Debug listing
    if "HC-05" in port.description or "Bluetooth" in port.description:
        bt_port = port.device
        break

if not bt_port:
    raise Exception("HC-05 Bluetooth serial port not found. Make sure it's paired and connected.")

# Open the serial connection
ser_hc05 = Serial(bt_port, 9600, timeout=1)
print(f"Connected to HC-05 on {bt_port}")

# De-duplication variables
last_cmd = None
last_time = 0
dedupe_ms = 500  # ignore same command within 0.5s

try:
    while True:
        if ser_hc05.in_waiting > 0:
            raw_line = ser_hc05.readline().decode('utf-8', errors='ignore').strip().lower()
            if not raw_line:
                continue

            # Ignore ACK lines entirely
            if raw_line.startswith("ack:"):
                print(f"Ignored ACK: {raw_line}")
                continue

            print(f"Command from HC-05: {raw_line}")

            # Extract command after colon if present
            command = raw_line.split(":")[-1].strip() if ":" in raw_line else raw_line

            # De-duplication to prevent double-trigger
            now = time.time() * 1000
            if command == last_cmd and (now - last_time) < dedupe_ms:
                print(f"Ignored duplicate command: {command}")
                continue
            last_cmd, last_time = command, now

            # Process commands
            if command in ['play', 'pause']:
                print("Simulating Play/Pause media key.")
                keyboard.press(Key.media_play_pause)
                time.sleep(0.1)
                keyboard.release(Key.media_play_pause)

            elif command == 'next':
                print("Simulating Right Arrow key (next).")
                keyboard.press(Key.right)
                time.sleep(0.1)
                keyboard.release(Key.right)

            elif command == 'back':
                print("Simulating Left Arrow key (back).")
                keyboard.press(Key.left)
                time.sleep(0.1)
                keyboard.release(Key.left)

            elif command == 'stop':
                print("Simulating Stop (Play/Pause).")
                keyboard.press(Key.media_play_pause)
                time.sleep(0.1)
                keyboard.release(Key.media_play_pause)

            else:
                print("Unknown command received.")

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nExiting program.")
    ser_hc05.close()
