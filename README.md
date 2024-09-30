# Desktop Assistant

**Desktop Assistant (DA)** is a Python-based voice-activated application that automates everyday tasks such as opening apps, setting reminders, fetching weather data, and interacting with the system using voice commands. Built with user-friendly features, it supports both text and voice inputs, making interaction seamless and efficient.

## Features
- **Voice Interaction**: Execute commands using speech recognition.
- **Automated Tasks**:
  - Open web applications (Google, YouTube, ChatGPT, etc.).
  - Open local applications (Notepad, Camera, etc.).
  - Play music and control playback.
  - Manage screen brightness.
  - Take screenshots.
- **Reminders & Scheduling**: Schedule events and receive timely notifications.
- **Weather Forecast**: Get current weather conditions for any city.
- **Date & Time Information**: Provides the current date and time upon request.

## Technologies Used
- **Python 3.x**: Core programming language.
- **Speech Recognition**: For converting speech to text.
- **Pyttsx3**: For text-to-speech (TTS) functionality.
- **Tkinter**: For creating the graphical user interface (GUI).
- **Plyer**: For sending desktop notifications.
- **Requests**: For making HTTP requests to external APIs (e.g., weather API).
- **PyAutoGUI**: For taking screenshots.
- **Screen Brightness Control**: For controlling screen brightness.
- **PyInstaller**: To package the application into an executable file.
- **PIL (Pillow)**: For handling images.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/desktop-assistant.git
   cd desktop-assistant
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python assistant.py
   ```

## How to Use
- **Activate Voice Command**: Simply speak into the microphone after running the application. DA will respond to commands like:
  - "Friday, open Google"
  - "Friday, play any song"
  - "Friday, take a screenshot"
  - "Friday, tell me today's date"
- **Reminder Feature**: Add event reminders with a date and time, and DA will notify you when it's time.

## Example Commands
- "Friday, open Google"
- "Friday, play a Hindi song"
- "Friday, tell me today's date"
- "Friday, increase brightness"
- "Friday, open weather app"
- "Friday, open notepad"

## Project Structure
```plaintext
📦desktop-assistant
 ┣ 📂images
 ┃ ┗ weather_icon.png
 ┣ 📜assistant.py
 ┣ 📜README.md
 ┣ 📜requirements.txt
```

## Libraries Required
The project utilizes the following Python libraries:
- `speech_recognition`: For voice recognition.
- `pyttsx3`: For text-to-speech.
- `tkinter`: For GUI creation.
- `requests`: For weather API requests.
- `pyautogui`: For capturing screenshots.
- `plyer`: For desktop notifications.
- `screen_brightness_control`: For brightness control.

To install all required dependencies, run:
```bash
pip install -r requirements.txt
```


