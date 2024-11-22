# SPEECH-TO-SUMMARIZE :Transcription, Summarization, and Translation


This project processes audio files by transcribing speech to text, summarizing the transcription, and translating the summary into French. It uses OpenAI's Whisper for transcription, a LED-based summarizer for summarization

#**Features**

Speech-to-Text:

Converts spoken words from audio into textual format using OpenAI's Whisper model.

Text Summarization:

Generates concise summaries from the transcribed text using the pszemraj/led-large-book-summary model.



#**Installation**

To set up the project, follow these steps:

git clone https://github.com/Martialkouass/Speech-to-summarize.git

cd speech-to-summarize

pip install -r requirements.txt  

for MacOS
brew install portaudio
pip install pyaudio

Ensure you have Python 3.9+ installed,

GPU recommended for faster inference

Libraries: transformers, torch, textsum, and whisperthen run:


Note: This package uses ffmpeg, so it should be installed for this audiorecorder to work properly.

On Ubuntu/Debian: sudo apt update && sudo apt install ffmpeg
On Mac: brew install ffmpeg


#**Usage**

Place your audio file (e.g., audio.mp3) in the project directory.

Update the file path in the script as needed.


Outputs:


Summary: Displayed in the console or saved as summary.txt.


#**Future Enhancements**

Add support for multiple languages in transcription.
Incorporate additional summarization and translation models.
Improve GUI for a better user experience.



**License**
This project is licensed under the MIT License.

