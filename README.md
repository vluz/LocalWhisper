# Local Whisper
### A Python streamlit app to perform speech-to-text with a local model
<hr>

Uses OpenAI Whisper lib https://github.com/openai/whisper 
<br>
to transcribe a uploaded audio file to text.
<br>
Uses Streamlit as GUI.

<hr>

Open a command prompt and `cd` to a new directory of your choosing:

(optional; recommended) Create a virtual environment with:
```
python -m venv "venv"
venv\Scripts\activate
```

To install do:
```
git clone https://github.com/vluz/LocalWhisper.git
cd LocalWhisper
pip install -r requirements.txt
```

On first run it may download several models.
<br>
The GUI may be blank or unresponsive for the duration of the setup
<br>
It will take quite some time, both on reqs above and on first run.
<br>
Please allow it time to finish.
<br>
All runs after the first are then faster to load.

To run do:<br>
`streamlit run localwhisper.py`

Gui will open on your default browser

<hr>

Online version: https://localwhisper.streamlit.app/
<br>
It may not run depending on Stramlit servers.

<hr>

Note: Do not use this for production, it's untested


