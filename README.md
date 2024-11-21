# SPEECH-TO-SUMMARIZE :Transcription, Summarization, and Translation

This project processes audio files by transcribing speech to text, summarizing the transcription, and translating the summary into French. It uses OpenAI's Whisper for transcription, a LED-based summarizer for summarization, and MBart for multilingual translation on https://huggingface.co/

#**Features**
Speech-to-Text:
Converts spoken words from audio into textual format using OpenAI's Whisper model.

Text Summarization:
Generates concise summaries from the transcribed text using the pszemraj/led-large-book-summary model.

Text Translation:
Translates the summary into French using Facebook's MBart model.

#**Installation**
To set up the project, follow these steps:

git clone https://github.com/Martialkouass/SPEECH-TO-SUMMARIZE.git
cd SPEECH-TO-SUMMARIZE
pip install -r requirements.txt  
Ensure you have Python 3.9+ installed,
GPU recommended for faster inference
Libraries: transformers, torch, textsum, gradio, and whisperthen run:

#**Usage**
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

#**Future Enhancements**
Add support for multiple languages in transcription.
Incorporate additional summarization and translation models.
Improve GUI for a better user experience.

**License**
This project is licensed under the MIT License.

