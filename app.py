import streamlit as st
from pydub import AudioSegment
import os
from audiorecorder import audiorecorder
from util import process_audio



header = st.container()
body = st.container()

st.markdown("<h1 style='text-align: center; color: red;'> 🎧 Speech to Summary 📑</h1>", unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)


state = "Uploader"

if "state" not in st.session_state :
    st.session_state["state"] = "Uploader"
    
    

def change_state_uploader() :
    st.session_state["state"] = "Uploader"


def change_state_record() :
    st.session_state["state"] = "record"
    

    
with body :

    _, colb1, colb2 = st.columns([0.2, 0.7, 1])

    if colb1.button("Upload an audio", on_click=change_state_uploader) :
        pass
    
    elif colb2.button("Record audio", on_click=change_state_record) :
        pass

    if st.session_state["state"] == "Uploader" :
        audio = (st.file_uploader("Upload your audio file", type=["mp3", "wav"]))
    elif st.session_state["state"] == "record" :
      audio = audiorecorder("Click to record", "Click to stop recording")
      if len(audio) > 0:
        st.audio(audio.export().read())
        audio.export("audio.wav", format="wav")
        st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")


    if audio :
      st.audio(audio)
      audio = AudioSegment.from_file(audio)
      with st.form("Result"):
        result=st.text_area("the summary of your audio 🔎", value = process_audio(audio))
        d_btn= st.form_submit_button("Download")
        if d_btn:
          envir_var = os.environ
          usr_loc= envir_var.get("USERPROFILE")
          loc=usr_loc+"\Downloads\\Summary.txt"
          with open(loc, "w") as file:
            file.write(result)
          st.success("Downloaded successfully")
