# 🎙️ Deepgram Asynchronous Live Transcriber

This project provides an asynchronous WebSocket based Python implementation that streams live audio to the Deepgram API for real-time transcription and speaker diarization.
It demonstrates how to capture, transmit, and process live audio in real time making it suitable for applications like virtual meetings, live captioning, and voice analytics.

## Similarity to Pyannote Speaker Diarization

While Pyannote performs offline speaker diarization using prerecorded audio and neural embeddings, this project achieves a live equivalent by leveraging Deepgram's realtime diarization API through a WebSocket stream.
This means you get diarized speaker segments as the conversation unfolds, without waiting for post processing.


## Features

- Asynchronous WebSocket Connection
Efficiently handles streaming audio and receiving transcriptions simultaneously using Python’s asyncio and websockets.

- Live Audio Streaming
Uploads audio in real time to Deepgram for continuous transcription.

- Speaker Diarization
Automatically separates speakers (similar to pyannote-audio's
 diarization capabilities), enabling multi-speaker conversation analysis.

- Real-time Transcription
Streams transcribed text back instantly as audio is processed.


## Requirements

Python 3.8+

Deepgram API key
(Get one at Deepgram Dashboard)

## Running the Project
- pip install -r requirements.txt
- python main_asynchronous.py # for pre-recorded and live audio stream
- python main_asynchronous.py # for pre-recorded audio
