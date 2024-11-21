# SPEECH-TO-SUMMARIZE :Transcription, Summarization, and Translation

This project processes audio files by transcribing speech to text, summarizing the transcription, and translating the summary into French. It uses OpenAI's Whisper for transcription, a LED-based summarizer for summarization, and MBart for multilingual translation on https://huggingface.co/

**Features**
Speech-to-Text:
Converts spoken words from audio into textual format using OpenAI's Whisper model.

Text Summarization:
Generates concise summaries from the transcribed text using the pszemraj/led-large-book-summary model.

Text Translation:
Translates the summary into French using Facebook's MBart model.

**Installation**
To set up the project, follow these steps:
Clone the repository
bash
Copy code
git clone https://github.com/your-username/SPEECH-TO-SUMMARIZE.git
cd SPEECH-TO-SUMMARIZE
Install dependencies and requierements
Ensure you have Python 3.9+ installed, then run:

**Usage**
Place your audio file (e.g., audio.mp3) in the project directory.
Update the file path in the script as needed.
Run the main script:
bash
Copy code
python main.py
Outputs:
Transcription: Displayed in the console or saved as transcription.txt.
Summary: Displayed in the console or saved as summary.txt.
Translation: Displayed in the console or saved as translation.txt.

