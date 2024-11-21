# -*- coding: utf-8 -*-
"""speech to text and sum.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dNW4sqBCezVdYrUcX96cGyZbSNnZpy1m

**Install the Python packages needed to use Whisper models and evaluate the transcription results**
"""

!pip install textsum
! pip install git+https://github.com/openai/whisper.git
!pip install --upgrade pip
!pip install pydub
!pip install streamlit-audiorecorder

from IPython.display import Audio
import torch
from pydub import AudioSegment
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from textsum.summarize import Summarizer
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast



"""**II- SPEECH TO TEXT**"""

def transcribe (audio) :
  device = "cuda:0" if torch.cuda.is_available() else "cpu"
  torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
  model_id = "openai/whisper-large-v3-turbo"
  model = AutoModelForSpeechSeq2Seq.from_pretrained(
      model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
      )
  model.to(device)
  processor = AutoProcessor.from_pretrained(model_id)
  pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
    )
  generate_kwargs = {
    "max_new_tokens": 400,
    "num_beams": 1,
    "condition_on_prev_tokens": False,
    "compression_ratio_threshold": 1.35,  # zlib compression ratio threshold (in token space)
    "temperature": (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
    "logprob_threshold": -1.0,
    "no_speech_threshold": 0.6,
    "return_timestamps": True,
    }
  result = pipe(audio,generate_kwargs=generate_kwargs)
  return result["text"]


"""**III-SUMMURIZE TEXT**"""

def summarize (text):
  model_name = "pszemraj/led-large-book-summary"
  summarizer = Summarizer(
      model_name_or_path=model_name,
      token_batch_length=4096,
      )
  return summarizer.summarize_string(text)


"""**IV-TRANSLATE TO FRENCH**"""

def translate(text):
  model = MBartForConditionalGeneration.from_pretrained("SnypzZz/Llama2-13b-Language-translate")
  tokenizer = MBart50TokenizerFast.from_pretrained("SnypzZz/Llama2-13b-Language-translate", src_lang="en_XX")
  model_inputs = tokenizer(text, return_tensors="pt")
  # translate from English to french
  generated_tokens = model.generate(
      **model_inputs,
      forced_bos_token_id=tokenizer.lang_code_to_id["fr_XX"]
      )
  return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)



"""**V-DEPLOYMENT ON GRADIO**"""

# Define the processing pipeline
def process_audio(audio):
  transcription = transcribe(audio)
  summary = summarize(transcription)
  translation = translate(summary)
  return translation

