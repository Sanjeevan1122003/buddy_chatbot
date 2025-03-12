# Buddy Chatbot

Buddy Chatbot is a voice-enabled AI chatbot that interacts with users through speech recognition and text-to-speech synthesis. It uses Google's Gemini AI to generate responses dynamically and can perform basic web-based tasks like opening Google and YouTube.

## Features
- Voice input using Speech Recognition
- AI-powered responses using Google's Gemini API
- Text-to-speech output using pyttsx3
- Web browsing capabilities (open Google, YouTube, etc.)

## Technologies Used
- Python 3.12
- SpeechRecognition
- pyttsx3
- google.generativeai (Gemini API)
- re (Regular Expressions)
- webbrowser (for opening URLs)

## Installation

### Prerequisites
Ensure you have Python 3.12 installed.

### Clone the Repository
```sh
git clone https://github.com/Sanjeevan1122003/buddy_chatbot.git
cd buddy_chatbot
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Configuration
### Set Up Gemini API Key
Create a file named `apikey.py` in the project folder and add:
```python
API_KEY = "your-gemini-api-key-here"
```
Replace `your-gemini-api-key-here` with your actual API key.

## Usage
Run the chatbot with:
```sh
python buddy.py
```
Once started, the chatbot will listen for your voice input and provide AI-generated responses.

## Commands
- **"Open Google"** → Opens Google in the web browser
- **"Open YouTube"** → Opens YouTube
- **"Bye"** → Exits the chatbot

## Troubleshooting
- If speech recognition is not working, check if your microphone is properly connected.
- Ensure the Gemini API key is correct and active.
- If the chatbot does not respond, restart the program.

## License
This project is open-source and available under the MIT License.

## Author
[Sanjeevan](https://github.com/Sanjeevan1122003)

