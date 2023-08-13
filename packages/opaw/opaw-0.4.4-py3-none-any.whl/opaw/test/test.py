import json

import whisper_timestamped as wt

audio = wt.load_audio("radio_short.mp3")
model = wt.load_model("tiny", device="cpu")
result = wt.transcribe(model, audio)

print(json.dumps(result, indent=2, ensure_ascii=False))
