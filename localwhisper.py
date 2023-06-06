import streamlit as st
import whisper
import io
import tempfile


def transcribe_audio(file, model):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".tmp") as temp_file:
        temp_file.write(file.getvalue())
        temp_file.flush()
    model = whisper.load_model(model)
    transcript = model.transcribe(temp_file.name)
    return transcript


st.title("Whisper local speech-to-text")
st.divider()
option = st.selectbox('Please select a model for transcription', ('small', 'base', 'tiny'))
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a", "ogg"])
st.markdown("[![test.mp3](app/static/test.mp3)](https://streamlit.io)")
st.divider()
if uploaded_file is not None:
    st.audio(uploaded_file)
    with st.spinner("Transcribing audio..."):
        transcript = transcribe_audio(uploaded_file, option)
    st.text_area("Transcript:",transcript["text"], height=250)
else:
    st.write("Please upload an audio file to transcribe.")
