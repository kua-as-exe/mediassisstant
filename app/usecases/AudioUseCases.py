from rich import print as rprint
from os.path import join
from dataclasses import dataclass

from app.services.ItemService import *

class AudioUseCases():

  def __init__(self, itemService: ItemService) -> None:
    self.itemService = itemService
    pass

  def transcribe(self, model: str, item: ItemModel, asset: AssetModel, language: str):

    assetsPath = self.itemService.getAssetsPathById(item.id) 
    
    assetPath = join(assetsPath, asset.basename)
    transFilename = f"transcription.{model}.txt"
    transcriptionPath = join(assetsPath, transFilename)

    import whisper

    whisperModel = whisper.load_model(model)
    result = whisperModel.transcribe(
      assetPath, 
      verbose=False, 
      language = language
    )

    # segments = result["segments"]
    # with open("results.json", "w") as resultFile:
    #   json.dump(segments,resultFile, indent= 4)

    text = result['text']
    with open(transcriptionPath, "w", encoding="utf-8") as resultFile:
      resultFile.write(text)

    
