import sys
import json

file = sys.argv[1]

print(f"Transcribing: {file}")



def transcribe(file: str):
  import whisper

  model = whisper.load_model("base")
  result = model.transcribe(file, verbose=True)

  segments = result["segments"]
  with open("results.json", "w") as resultFile:
    json.dump(segments,resultFile, indent= 4)

  text = result['text']
  print(text)
  with open("result.txt", "w") as resultFile:
    resultFile.write(text)

transcribe(file)