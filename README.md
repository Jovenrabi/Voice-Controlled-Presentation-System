Voice‑Controlled Remote (Arduino + Python)
This project connects an Arduino with a Voice Recognition V3 module to a PC running Python. Spoken commands are sent via Bluetooth (HC‑05) and translated into keyboard actions like Next and Back for presentations, media players, or any app that uses arrow keys.

⚙️ System Overview
Arduino Side (C++)

Uses VoiceRecognitionV3 module to detect trained commands.

Normalizes mis‑hearings (e.g., “bak”, “bck” → “back”).

Debounces repeated commands (ignores duplicates within 1s).

Sends framed commands <next> or <back> via HC‑05 Bluetooth.

PC Side (Python / EXE)

Auto‑detects the HC‑05 COM port.

Reads framed commands from serial.

Deduplicates repeated commands (ignores duplicates within 0.5s).

Simulates Right Arrow for <next> and Left Arrow for <back> using pynput.

Sends acknowledgment (ack:next, ack:back) back to Arduino.

Packaged as a standalone .exe for easy use without installing Python.

🛠 Hardware Setup
Arduino Uno (or compatible board)

HC‑05 Bluetooth module

RX → Arduino pin 10

TX → Arduino pin 11

Voice Recognition V3 module

RX → Arduino pin 2

TX → Arduino pin 3

PC with Bluetooth paired to HC‑05

📂 Software Components
Arduino Code (arduino_step_remote.ino)
Initializes HC‑05 and VoiceRecognitionV3.

Loads trained slots for “next” and “back”.

Recognizes commands, debounces, and sends framed messages.

Python Code (voice_remote.py)
Auto‑detects HC‑05 COM port.

Reads framed commands <next> / <back>.

Simulates arrow key presses.

Sends ACK back to Arduino.

Executable (voice_remote.exe)
Packaged version of the Python script.

Allows end‑users to run the software without installing Python or dependencies.

Double‑click to start listening for commands once HC‑05 is connected.

🔄 Workflow
User speaks → VoiceRecognitionV3 detects “next” or “back”.

Arduino normalizes → sends <next> or <back> via HC‑05.

Python/EXE receives → interprets command, simulates arrow key.

PC responds → sends ack:command back to Arduino.

Arduino logs ACK → confirms successful transmission.

🎯 Why This Project is Useful
Hands‑free control of slides, videos, or media players.

Demonstrates hardware/software integration (Arduino ↔ Python).

Shows how to package Python scripts into portable executables.

Easy to extend (add more commands, map to other keys, or integrate with apps).
